from selection_sort import selection_sort
import unittest

class TestInsertionSort(unittest.TestCase):
    # Test an unsorted list
    def test_unsorted_list(self):
        unsorted_list = [4, 2, 1, 3]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(selection_sort(unsorted_list), expected_output)

    # Test a list that's already sorted
    def test_sorted_list(self):
        sorted_list = [1, 2, 3, 4]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(selection_sort(sorted_list), expected_output)

    # Test a list with duplicate elements
    def test_duplicate_elements_list(self):
        duplicate_list = [4, 2, 1, 3, 3, 2, 4, 1]
        expected_output = [1, 1, 2, 2, 3, 3, 4, 4]
        self.assertEqual(selection_sort(duplicate_list), expected_output)

    # Test an empty list
    def test_empty_list(self):
        empty_list = []
        expected_output = []
        self.assertEqual(selection_sort(empty_list), expected_output)


if __name__ == "__main__":
    unittest.main()