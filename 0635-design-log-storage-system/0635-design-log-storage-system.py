class LogSystem:

    def __init__(self):
        self.logs = []
        self.granularity_index = {
            'Year': 4, 
            'Month': 7, 
            'Day': 10, 
            'Hour': 13, 
            'Minute': 16, 
            'Second': 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        slice_index = self.granularity_index[granularity]
        return [
            log_id 
            for log_id, timestamp in self.logs 
            if start[:slice_index] <= timestamp[:slice_index] <= end[:slice_index]
        ]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)