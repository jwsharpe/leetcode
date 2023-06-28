class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            pts.append([dist, x, y])

        heapq.heapify(pts)
        res = []
        for i in range(k):
            ele = heapq.heappop(pts)
            x, y = ele[1], ele[2]
            res.append([x,y])
        return res
