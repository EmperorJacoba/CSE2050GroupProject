import unittest
from hash import HashMap
from course import Course

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hm = HashMap()

    def test_set(self):
        self.hm[1] = "Hi"
        self.hm["foo"] = 10

    def test_get(self):
        self.hm[1] = "buzz"
        self.hm["foo"] = 10
        self.hm[(10,20,30)] = True

        self.assertEqual(self.hm[1], "buzz")
        self.assertEqual(self.hm["foo"], 10)
        self.assertEqual(self.hm[(10,20,30)], True)
        with self.assertRaises(KeyError):
            _ = self.hm["bar"]

    def test_len(self):
        self.assertEqual(0, len(self.hm))
        self.hm[1] = "foo"
        self.assertEqual(1, len(self.hm))

        self.hm[2] = "buzz"
        self.assertEqual(2, len(self.hm))

        self.hm[2] = "bar"
        self.assertEqual(2, len(self.hm))

class TestHashMap(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        pass

    def test_collision_handling(self):
        pass

    def test_rehashing(self):
        pass

class TestEnrollments(unittest.TestCase):
    def test_check_for_prerequisites(self):
        pass

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        pass

    def test_merge_sort(self):
        # test course correctly sorted by id, name, date
        # use setUp/test procedure from m2 testcases for other algs
        pass

    def test_quick_sort(self):
        # test course correctly sorted by id, name, date
        # use setUp/test procedure from m2 testcases for other algs
        pass

if __name__ == "__main__":
    unittest.main()