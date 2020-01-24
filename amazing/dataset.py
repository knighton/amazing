from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.solve.BacktrackingSolver import BacktrackingSolver
import numpy as np
import torch
from torch.utils.data import Dataset


def pad_maze(s):
    ss = s.split('\n')
    ss = list(map(lambda s: s + ' ', ss))
    ss.append(' ' * len(ss[0]))
    return '\n'.join(ss)


def make_class_grid(s):
    s = s.encode('utf-8')
    ss = s.split(b'\n')
    x = np.zeros((len(ss), len(ss[0])), np.uint8)
    for i, s in enumerate(ss):
        x[i] = np.frombuffer(s, np.uint8)
    return x


def to_one_hot(indices, num_classes, dtype):
    x = np.eye(num_classes, dtype=dtype)[indices.reshape(-1)]
    return x.reshape(indices.shape + (num_classes,))


def ascii_to_sample(text):
    s = text.replace('+', ' ')
    for i, c in enumerate(' #SE'):
        s = s.replace(c, chr(i))
    x = make_class_grid(s)
    x = to_one_hot(x, 4, np.float32)
    x = x.transpose(2, 0, 1)
    x = torch.tensor(x)

    s = text
    for c in ' #SE':
        s = s.replace(c, chr(0))
    s = s.replace('+', chr(1))
    y = make_class_grid(s)
    y = y.astype(np.float32)
    y = np.expand_dims(y, 0)
    y = torch.tensor(y)

    return x, y


class MazeDataset(Dataset):
    @classmethod
    def is_hw_ok(cls, hw):
        return isinstance(hw, int) and 2 <= hw and not hw % 2

    def __init__(self, height, width, size=32768):
        super().__init__()
        assert self.is_hw_ok(height)
        assert self.is_hw_ok(width)
        self.height = height
        self.width = width
        self.size = size
        maze = Maze()
        maze.generator = Prims(height // 2 - 1, width // 2 - 1)
        maze.solver = BacktrackingSolver()
        self.maze = maze

    def __len__(self):
        return self.size

    def generate(self):
        x = self.maze
        x.generate()
        x.generate_entrances()
        x.solve()
        s = x.tostring(True, True)
        s = pad_maze(s)
        return s, ascii_to_sample(s)

    def __getitem__(self, index):
        return self.generate()


WALL_CHRS = {
    (False, False, False, False): '+',  # None.

    (True, False, False, False): '|',   # Up.
    (False, True, False, False): '|',   # Down.
    (False, False, True, False): '-',   # Left.
    (False, False, False, True): '-',   # Right.

    (True, True, False, False): '|',    # Up and down.
    (False, False, True, True): '-',    # Left and right.
    (True, False, True, False): '+',    # Up and left.
    (True, False, False, True): '+',    # Up and right.
    (False, True, True, False): '+',    # Down and left.
    (False, True, False, True): '+',    # Down and right.

    (True, False, True, True): '+',     # Up and left and right.
    (False, True, True, True): '+',     # Down and left and right.
    (True, True, True, False): '+',     # Left and up and down.
    (True, True, False, True): '+',     # Right and up and down.

    (True, True, True, True): '+',      # All.
}


def show(background, x):
    background = background.replace('+', ':')
    ss = background.split('\n')
    height = len(ss)
    width = len(ss[0])
    tt = list(ss)
    for i in range(height):
        tt[i] = list(ss[i])
        for j in range(width):
            c = ss[i][j]
            if c != '#':
                continue
            up = (ss[i - 1][j] == '#') if 1 <= i else False
            down = (ss[i + 1][j] == '#') if i < height - 1 else False
            left = (ss[i][j - 1] == '#') if 1 <= j else False
            right = (ss[i][j + 1] == '#') if j < width - 1 else False
            tt[i][j] = WALL_CHRS[(up, down, left, right)]
        tt[i] = ' '.join(tt[i]).replace(':', '#')
    background = tt

    x = x.squeeze(0)
    x = (x * 10).type(torch.uint8)
    x = x + ord('0')
    x = x.detach().cpu().numpy()

    ss = []
    for i in range(len(x)):
        s = x[i].tobytes().decode('utf-8')
        s = s.replace('0', ' ')
        s = ' '.join(list(s))
        ss.append(s)
    foreground = ss

    ss = []
    for bg_line, fg_line in zip(background, foreground):
        s = list(bg_line)
        for i, c in enumerate(fg_line):
            if c != ' ':
                s[i] = c
        s = ''.join(s)
        ss.append(s)
    s = '\n'.join(ss)

    print()
    print(s)
    print()
