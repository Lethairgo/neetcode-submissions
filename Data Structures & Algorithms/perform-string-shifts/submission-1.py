class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # calculate the final moves, since it's either left or right
        move = 0
        for i in range(len(shift)):
            direction, steps = shift[i]
            if direction == 1:
                move -= steps
            else:
                move += steps
        n = len(s)
        move %= n 
        return s[move:] + s[:move]
        