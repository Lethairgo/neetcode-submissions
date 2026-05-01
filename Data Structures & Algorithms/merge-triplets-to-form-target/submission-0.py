class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        x_valid = y_valid = z_valid = False

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue

            if a == x:
                x_valid = True
            if b == y:
                y_valid = True
            if c == z:
                z_valid = True

        return x_valid and y_valid and z_valid
        