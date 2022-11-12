"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""


# Initial thinking. Insertion Sort. Gets TLE.
"""
class MedianFinder:
    def __init__(self):
        self.store = []

    def addNum(self, num: int) -> None:
        def binarySearch(arr, key):
            l, r = 0, len(arr)
            while l<r:
                m = l + (r-l)//2
                if arr[m] < key:
                    l = m + 1
                else:
                    r = m
            return l
        
        self.store.append(num)
        j = len(self.store) - 1
        if j < 1:
            return
        pos = binarySearch(self.store[:-1], num)
        #print(self.store)
        #print(pos)
        #print(j)
        while pos < j:
            self.store[j] = self.store[j-1]
            j -= 1
        self.store[pos] = num
        
        
            
    def findMedian(self) -> float:
        #print(self.store)
        n = len(self.store)
        if n & 1 : 
            return self.store[n//2]
        else:
            return (self.store[n//2 - 1] + self.store[n//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
"""

class MedianFinder:
    def __init__(self):
        self.shp, self.lhp = [], []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.shp, -1*num)
        if self.shp and self.lhp and -1*self.shp[0] > self.lhp[0]:
            val = -1 * heapq.heappop(self.shp)
            heapq.heappush(self.lhp, val)
        if len(self.shp) > len(self.lhp) + 1:
            val = -1 * heapq.heappop(self.shp)
            heapq.heappush(self.lhp, val)
        if len(self.shp) + 1 < len(self.lhp):
            val = heapq.heappop(self.lhp)
            heapq.heappush(self.shp, -1 * val)
        
    def findMedian(self) -> float:
        #print(self.shp)
        #print(self.lhp)
        if len(self.shp) < len(self.lhp):
            return self.lhp[0]
        elif len(self.shp) > len(self.lhp):
            return -1 * self.shp[0]
        else:
            return (self.lhp[0]+ -1* self.shp[0])/2