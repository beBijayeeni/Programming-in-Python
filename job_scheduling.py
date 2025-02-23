from collections import defaultdict
class Solution:
   def solve(self, intervals):
      d = defaultdict(list)
      n = 0
      for start, end, profit in intervals:
         if end > n:
            n = end
         d[end].append([start, profit])
      A = [0 for i in range(n + 1)]
      for end in range(len(A)):
         if end in d:
            for start, profit in d[end]:
               A[end] = max(A[end], A[start] + profit, A[end - 1])
         else:
            A[end] = A[end - 1]
      return A[-1]
ob = Solution()
intervals = [[1, 2, 100],[3, 5, 40],[6, 19, 150],[2, 100, 250]]
print(ob.solve(intervals))