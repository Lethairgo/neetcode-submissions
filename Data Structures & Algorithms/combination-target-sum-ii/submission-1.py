class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, current, total):
            if total == target:
                result.append(current[:])
                return
            elif i == len(candidates) or total + candidates[i] > target:
                return
            current.append(candidates[i])
            dfs(i + 1, current, total + candidates[i])
            current.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, current, total)
        dfs(0, [], 0)
        return result
        