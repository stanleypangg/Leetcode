class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space_count = text.count(' ')

        if len(words) == 1:
            return words[0] + ' ' * space_count
        else:
            extra_spaces = ' ' * (space_count % (len(words) - 1))
            adjacent_spaces = ' ' * (space_count // (len(words) - 1))
            return adjacent_spaces.join(words) + extra_spaces