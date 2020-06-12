import sys  # sys.maxsize
import pandas as pd


def reader(source: str) -> pd.DataFrame:
    df = pd.read_csv(source, sep=" ", skiprows=1, header=None)
    df.columns = [x for x in range(len(df.columns) - 1, -1, -1)]
    return df


class Vertex:
    def __init__(self, node: int):
        self.id: int = node
        self.adjacent = {}
        self.distance: int = sys.maxsize
        self.visited: bool = False
        self.previous = None

    def add_neighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def get_weight(self, neighbour: 'Vertex') -> float:
        return self.adjacent[neighbour]


class Graph:
    def __init__(self, input_file):
        self.source: pd.DataFrame = reader(input_file)
        self.vert_dict = {}
        self.num_vertices: int = len(self.source.columns)
        # Create vertices
        for v in range(0, len(self.source.columns)):
            self.vert_dict[v] = Vertex(v)
        # Make connections
        for col in range(self.num_vertices-1, -1, -1):   # Read weights from a superior triangle adjacency matrix
            for row in range(col-1, -1, -1):
                self.vert_dict[col].add_neighbour(self.vert_dict[row], float(self.source[col][row]))
                self.vert_dict[row].add_neighbour(self.vert_dict[col], float(self.source[col][row]))

    def __iter__(self):
        return iter(self.vert_dict.values())

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def get_vertices(self):
        return self.vert_dict.keys()

def shortest(v: Vertex, path):
    if v.previous:
        path.append(v.previous.id)
        shortest(v.previous, path)
    return



