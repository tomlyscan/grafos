from graph.model import Vertex, Graph
import heapq


def dijkstra(aGraph: Graph, start: Vertex, target: Vertex):
    # INITIALIZE-SINGLE-SOURCE step
    # All nodes initialize with distance=sys.maxsize
    start.distance = 0

    unvisited_queue = [(v.distance, v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current: Vertex = uv[1]
        current.visited = True

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.distance + current.get_weight(next)

            if new_dist < next.distance:
                next.distance = new_dist
                next.previous = current

        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.distance, v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)