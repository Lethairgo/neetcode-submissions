class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        wordList.append(beginWord)
        n = len(beginWord)

        for word in wordList:
            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]
                d[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(n):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in d[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1

        return 0
