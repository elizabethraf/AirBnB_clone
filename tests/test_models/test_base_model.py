import unittest
import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.testmodel = BaseModel()

    def test_if_id_exist(self):
        self.assertIsNotNone(self.testmodel.id)

    def test_isupper(self):
        self.assertTrue('base_model.py'.isupper())
        self.assertFalse('base_model.py'.isupper())

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def re_Storage(self):
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_split(self):
        s = 'BaseModel'
        self.assertEqual(s.split(), ['Base', 'Model'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_add_method_returns_correct_result(self):
        self.assertEqual(8, 8)

    def test_class_docstring(self):
        """Display a  docstring for BaseModel"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.testmodel.id,
                          "Base", "Model")

    def test_add_method_returns_correct_result_almost(self):
        print('Hello')
        self.assertAlmostEqual(2, 2)

    def test_assert_raises_attribute(self):
        with self.assertRaises(AttributeError):
            [].get

class TestBaseModel(unittest.TestCase):
    """Difine test for  BaseModel class"""

    def test_attributes(self):
        """Test for objects"""
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "My First Model"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
        self.assertEqual(inst.name, "Alx")
        self.assertEqual(inst.number, 89)

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
    def test_datetime(self):
        """Test for BaseModel instances"""

        __dic = datetime.now()
        inst = BaseModel()
        doc = datetime.now()
        self.assertTrue(__dic <= inst.created_at <= doc)
        time.sleep()
        __dic = datetime.now()
        insta = BaseModel()
        doc = datetime.now()
        self.assertTrue(_dic <= insta.created_at <= doc)
        self.assertEqual(inst.created_at, inst.updated_at)
        self.assertEqual(insta.created_at, insta.updated_at)
        self.assertNotEqual(inst.created_at, insta.created_at)
        self.assertNotEqual(inst.updated_at, insta.updated_at)

    def test_uuid(self):
        """Test id is correct uuid"""
        inst = BaseModel()
        insta = BaseModel()
        for inst in [inst, insta]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst.id, inst.id)

    def test_to_dict(self):
        """Test for dictionary"""

        _model_ = BaseModel()
        _model_.name = "My First Model"
        _model_.my_number = 89
        a = _model_.to_dict()
        expected_attributes = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(a.keys(), expected_attributes)
        self.assertEqual(a['__class__'], 'BaseModel')
        self.assertEqual(a['name'], "My First Model")
        self.assertEqual(a['my_number'], 89)

    def test_to_dict_values(self):
        """test that values"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        b = BaseModel()
        prev_a = bm.to_dict()
        self.assertEqual(prev_a["__class__"], "BaseModel")
        self.assertEqual(type(prev_a"created_at"]), str)
        self.assertEqual(type(prev_a["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_str(self):
        """test string output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    @mock.patch('models.storage')
    def test_save(self, _storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(_storage.new.called)
        self.assertTrue(_storage.save.called)


if __name__ == "__main__":
    unittest.main()
