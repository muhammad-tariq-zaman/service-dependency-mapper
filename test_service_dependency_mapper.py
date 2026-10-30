import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import order


class TestDependencyMapper(unittest.TestCase):
    def test_dependency_first(self):
        result = order({"web": ["db"], "db": []})
        self.assertLess(result.index("db"), result.index("web"))

    def test_cycle_detected(self):
        with self.assertRaises(ValueError):
            order({"a": ["b"], "b": ["a"]})

    def test_independent_services_kept(self):
        self.assertEqual(sorted(order({"a": [], "b": []})), ["a", "b"])
