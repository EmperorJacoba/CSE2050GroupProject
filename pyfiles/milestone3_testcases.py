import unittest
from hash import HashMap

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

if __name__ == "__main__":
    unittest.main()