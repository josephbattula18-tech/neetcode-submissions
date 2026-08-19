class TimeMap:

    def __init__(self):
        self.data={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key]=[]
        self.data[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        arr = self.data[key]
        l,r=0,len(arr)-1
        ans=""
        while l<=r:
            m=(l+r)//2
            if arr[m][0]<=timestamp:
                ans=arr[m][1]
                l=m+1
            else:
                r=m-1
        return ans
