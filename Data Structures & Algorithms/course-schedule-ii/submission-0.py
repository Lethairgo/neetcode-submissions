class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses  # indegree[i]: the number of pre courses i has
        adj = {i : [] for i in range(numCourses)} # map pre -> course

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        while queue:
            pre = queue.popleft()
            order.append(pre)

            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return order if len(order) == numCourses else []


        