class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        size = len(beginWord)
        
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(size):
                pattern = word[:i] + '*' + word[i + 1:]
                neighbors[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step
            
            for i in range(size):
                pattern = word[:i] + '*' + word[i + 1:]
                for neighbor in neighbors[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, step + 1))

        return 0