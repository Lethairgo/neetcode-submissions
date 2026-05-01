class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point

        for (x, y), cnt in self.points.items():
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue

            result += cnt * self.points.get((x, py), 0) * self.points.get((px, y), 0)

        return result

        
