class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if prereqMap[c] == []:
                return True
            
            visited.add(c)
            for pre in prereqMap[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            prereqMap[c] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        