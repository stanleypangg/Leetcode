class FrequencyTracker:

    def __init__(self):
        self.num_to_freq = defaultdict(int)
        self.freq_to_num = defaultdict(set)

    def add(self, number: int) -> None:
        old_count = self.num_to_freq.get(number, 0)
        if old_count != 0:
            self.freq_to_num[old_count].remove(number)
        
        self.num_to_freq[number] += 1
        self.freq_to_num[old_count + 1].add(number)

    def deleteOne(self, number: int) -> None:
        old_count = self.num_to_freq.get(number, 0)
        if old_count == 0:
            return
        
        self.num_to_freq[number] -= 1
        self.freq_to_num[old_count].remove(number)
        self.freq_to_num[old_count - 1].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freq_to_num[frequency]) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)