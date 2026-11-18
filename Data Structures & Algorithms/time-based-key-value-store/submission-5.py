class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ([value], [timestamp])
        else:
            self.store[key][0].append(value)
            self.store[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:

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