class UndergroundSystem:

    def __init__(self):
        # key = id, 
        # value = [startStation, startTime]
        self.customer_history = {}

        # key = startStation, value = {endStation: (total time, total customers)}
        self.average_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_history[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.customer_history[id]

        if startStation not in self.average_times:
            self.average_times[startStation] = {}

        if stationName not in self.average_times[startStation]:
            self.average_times[startStation][stationName] = [0, 0]
        
        self.average_times[startStation][stationName][0] += t - startTime
        self.average_times[startStation][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, customers = self.average_times[startStation][endStation]

        return total_time / customers

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)