import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.testmodel = BaseModel()

    def test_if_id_exist(self):
        self.assertIsNotNone(self.testmodel.id)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_add_method_returns_correct_result(self):
        self.assertEqual(8, 8)

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.testmodel.id,
                          "Hello", "World")

    def test_add_method_returns_correct_result_almost(self):
        print('Hello')
        self.assertAlmostEqual(2, 2)

    def test_assert_raises_attribute(self):
        with self.assertRaises(AttributeError):
            [].get

    # more examples of unit tests types

    def test_assert_equal(self):
        self.assertEqual(4, (2 + 2), msg=None)

    def test_assert_almost_equal_delta_0_5(self):
        self.assertAlmostEqual(1, 1.2, delta=0.5)

    def test_assert_almost_equal_places(self):
        self.assertAlmostEqual(1, 1.00001, places=4)

    def test_assert_raises(self):
        self.assertRaises(ValueError, int, "a")

    def test_assert_dict_contains_subset(self):
        expected = {'a': 'b'}
        actual = {'a': 'b', 'c': 'd', 'e': 'f'}
        self.assertGreaterEqual(actual.items(), expected.items())
        """
        # deprecated please use the above
        self.assertDictContainsSubset(expected, actual)
        """

    def test_assert_dict_equal(self):
        expected = {'a': 'b', 'c': 'd'}
        actual = {'c': 'd', 'a': 'b'}
        self.assertDictEqual(expected, actual)

    """
    Truth value:
    -----------
    0               False
    1               True
    -1              True
    “”              False
    “Hello, World!” True
    None            False
    """

    def test_assert_true(self):
        self.assertTrue(1)
        self.assertTrue("Hello, World")

    def test_assert_false(self):
        self.assertFalse(0)
        self.assertFalse("")

    def test_assert_greater(self):
        self.assertGreater(6, 3)

    def test_assert_less(self):
        self.assertLess(4, 7)

    def test_assert_less_equal(self):
        self.assertLessEqual(4, 5)

    def test_assert_greater_equal(self):
        self.assertGreaterEqual(2, 2)

    def test_assert_list_equal(self):
        self.assertListEqual([3, 1, 2], [3, 1, 2])

    def test_assert_set_equal(self):
        self.assertSetEqual(set([3, 1, 2]), set([3, 1, 2]))
    # Had to type cast a set

    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3, 4, 5])
    """
    assertIn(member, container, msg=None)
    With this method, you can check whether a value is in
    a container (hashable) such as a list or
    tuple. This method is useful when you don’t
    care what the other values are, you just wish to
    check that a certain value(s) is in the container.
    """

    def test_assert_is(self):
        self.assertIs("a", "a")
    """
    assertIs(expr1, expr2)
    Use this method to check that expr1 and expr2 are identical.
    That is to say they are the
    same object. For example, the python code []
    is [] would return False , as the creation
    of each list is a separate object.
    """

    def test_assert_is_not(self):
        self.assertIsNot([], [])

    def test_assert_is_instance(self):
        self.assertIsInstance(1, int)

    def test_assert_is_not_instance(self):
        self.assertNotIsInstance(1, str)

    def test_assert_is_none(self):
        self.assertIsNone(None)

    def test_assert_is_not_none(self):
        self.assertIsNotNone(1)

    """
    assertRaises(excClass, callableObj, *args, **kwargs, msg=None)
    This assertion is used to check that under certain conditions exceptions
    are raised. You pass
    in the exception you expect, the callable that will raise
    the exception and any arguments to
    that callable. In the earlier example,
    this pops the first item from an empty list and results in
    an IndexError .
    """

    def test_assert_raises_index(self):
        self.assertRaises(IndexError, [].pop, 0)
    """
    # more from:
    https://docs.python.org/3/library/unittest.html#unittest.TestCase
    """


if __name__ == '__main__':
    unittest.main()
