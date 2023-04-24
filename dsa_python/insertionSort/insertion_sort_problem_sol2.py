class computeRunningMedian:
    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def get_median(self, nums):
        n = len(nums)
        medians = [0] * n

        for i in range(n):
            arr = nums[:i+1]
            self.insertion_sort(arr)
            print(f'The sorted array after insertion sort is {arr}')

            mid = i // 2
            if i % 2 == 0:
                medians[i] = arr[mid]
            else:
                medians[i] = (arr[mid] + arr[mid+1]) / 2
            print(f'The running median is {medians[i]}')

        return medians


if __name__ == '__main__':
    array = [2, 1, 5, 7, 2, 0, 5]
    running_median = computeRunningMedian()

    medians = running_median.get_median(array)
    print(f'The running medians are {medians}')
