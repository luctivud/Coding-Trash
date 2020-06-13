class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans, n = [], len(arr)     
        prefix_sum = {}
        curr = 0
        for i in range(n):
            curr += arr[i]
            if curr == target:
                ans.append([0, i])
            elif curr-target in prefix_sum:
                ans.append([prefix_sum[curr-target]+1, i])
            prefix_sum[curr] = i
            
        ans.sort(key = lambda x: (x[1] - x[0], x[0]))
        mn = float('inf')
        i, j = 0, 1
        while j < len(ans):
            if ans[i][0] < ans[j][0]:
                if ans[i][1] < ans[j][0]:
                    mn = min(ans[i][1] + ans[j][1] - ans[i][0] - ans[j][0] + 2, mn)
            elif ans[i][0] > ans[j][0]:
                if ans[i][0] > ans[j][1]:
                    mn = min(ans[i][1] + ans[j][1] - ans[i][0] - ans[j][0] + 2, mn)
            j += 1
        if mn != float('inf'):
            return mn
        return -1
            
            
        