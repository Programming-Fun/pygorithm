import unittest
import random

from pygorithm.sorting import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    counting_sort,
    bucket_sort,
    shell_sort,
    heap_sort)


class TestSortingAlgorithm(unittest.TestCase):
    def setUp(self):
        # to test numeric numbers
        self.array = list(range(15))
        random.shuffle(self.array)
        self.sorted_array = list(range(15))

        # to test alphabets
        string = 'pythonisawesome'
        self.alphaArray = list(string)
        random.shuffle(self.alphaArray)
        self.sorted_alpha_array = sorted(string)


class TestBubbleSortTest(TestSortingAlgorithm):
    def test_bubble_sort(self):
        self.result = bubble_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = bubble_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestInsertionSortTest(TestSortingAlgorithm):
    def test_insertion_sort(self):
        self.result = insertion_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = insertion_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestSelectionSortTest(TestSortingAlgorithm):
    def test_selection_sort(self):
        self.result = selection_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = selection_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestMergeSortTest(TestSortingAlgorithm):
    def test_merge_sort(self):
        self.result = merge_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = merge_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestQuickSortTest(TestSortingAlgorithm):
    def test_quick_sort(self):
        self.result = quick_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = quick_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestCountingSortTest(TestSortingAlgorithm):
    def test_counting_sort(self):
        # counting sort is an integer based sort
        self.result = counting_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)


class TestBucketSortTest(TestSortingAlgorithm):
    def test_bucket_sort(self):
        self.result = bucket_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = bucket_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestShellSortTest(TestSortingAlgorithm):
    def test_shell_sort(self):
        self.result = shell_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = shell_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestHeapSortTest(TestSortingAlgorithm):
    def test_heap_sort(self):
        self.result = heap_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = heap_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)

if __name__ == '__main__':
    unittest.main()
