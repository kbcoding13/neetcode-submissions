class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #stores the key key and the value value at a given timestamp timestamp
        if key in self.store:
            self.store[key][0].append(value)
            self.store[key][1].append(timestamp)
        else:
            self.store[key] = ([value], [timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        #returns the value such that set was called previously with timestamp_prev <= timestamp. If there are multiple values, it returns the value associated with the largest timestamp_prev, if there are no values, it returns ""
        
        if key not in self.store or len(self.store[key][1]) == 0:
            return ""
        
        values, timestamps = self.store[key]
        l, r = 0, len(timestamps) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2

            if timestamps[m] <= timestamp:
                res = values[m]
                l = m + 1
            else:
                r = m - 1

        return res