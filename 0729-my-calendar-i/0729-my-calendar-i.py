class MyCalendar:

    def __init__(self):
        # naive
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.intervals:
            if (s < endTime and startTime < e):
                return False
        
        self.intervals.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)