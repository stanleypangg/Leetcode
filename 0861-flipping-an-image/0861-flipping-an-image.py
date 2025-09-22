class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # n by n binary matrix image, flip horizontally, then invert it
        # reverse each row would be O(n^2), is there a quicker way?
        # invert each value (flip binary)

        n = len(image)
        # iterate over rows
        for row in image:
            # iterate each column
            # two pointers from each end, converging in middle
            # swap values, while also apply not operator
            i, j = 0, n - 1
            while i <= j:
                row[i], row[j] = 1 - row[j], 1 - row[i]
                i += 1
                j -= 1
        return image