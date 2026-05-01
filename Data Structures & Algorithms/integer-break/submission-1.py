class Solution:
    def integerBreak(self, n: int) -> int:
        # dfs, memoization
        products = {}
        def dfs(x):
            if x in products:
                return products[x]
                
            product = 0

            for i in range(1, x):
                no_cut = i * (x - i)
                keep_cut = i * dfs(x - i)
                product = max(product, no_cut, keep_cut)
            products[x] = product
            return product
        return dfs(n)
        