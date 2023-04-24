class computeRunningMedian:
    def __init__(self):
        self.array = []
        self.length = 0 

    def add_elements(self, item):
        self.array.append(item)
        self.length += 1

        # Insertion Sort to keep the array sorted
        i = self.length - 1
        key = self.array[i]
        j = i - 1

        while j >= 0 and self.array[j] > key:
            self.array[j+1] = self.array[j]
            j -= 1

        self.array[j+1] = key
        return self.array


    def get_median(self):
        if self.length % 2 == 0: 
            # Average of the two middle numbers
            mid = self.length // 2
            return (self.array[mid-1] + self.array[mid]) / 2
        else:
            # Middle number
            mid = self.length // 2
            return self.array[mid]


if __name__ == '__main__':
    numbers = [2, 1, 5, 7, 2, 0, 5]
    running_median = computeRunningMedian()

    for num in numbers:
        sorted_arr = running_median.add_elements(num)
        print(f'The sorted array after adding each element is: {sorted_arr}')

        median = running_median.get_median()
        print(f'The running median of {sorted_arr} is: {median}')
