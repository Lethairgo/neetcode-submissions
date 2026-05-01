class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()

        def dfs(cur):
            if len(cur) == len(nums):
                result.append(cur.copy())
                return
            
            for num in nums:
                if num in visited:
                    continue
                cur.append(num)
                visited.add(num)
                dfs(cur)
                visited.remove(num)
                cur.pop()


        dfs([])

        return result
        