#!/usr/bin/python
"""
Unittest to Test cases for file handling.

"""

from __future__ import print_function
import os
import shutil
import copy
import json
from common_test_class import AbstractPillarTest, MY_PATH
from common_test_data import EXAMPLE_FILE


class TestFileStorage(unittest.TestCase):
    """
    Test for storage
    """
    def setUp(self):
        self.storage = FileStorage('test')
        self.test_file = fileStorage()
        return

    @classmethod
    def setUpClass(cls):
        cls.usr = User()
        cls.usr.first_name = "John"
        cls.usr.last_name = "ALX"
        cls.path = "file.json"
        cls.usr.name = "My_First_Model"
        cls.usr.number = "89"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        del cls.usr

    def teardown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def TestPep8_fileStorage(self):
        """ Testing Method style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def TestDocString_fileStorage(self):
        """
        Test docstring
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_all(self):
        """
        Display testing method: all (returns dic <class>.<id> : <obj instance>)
        """
        fstorage = FileStorage()
        instances_dic = fstorage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, fstorage._FileStorage__objects)

    def test_constructor(self):
        """
        Does it set up the name and the BaseStorage parent?
        """
        storage = FileStorage(PATH)
        self.assertEqual(PATH, storage.path)
        return

    def test_write(self):
        self.storage._file = self.mock_file
        self.storage.write('alpha')
        self.mock_file.write.assert_called_with('alpha')

    def test_write_error(self):
        storage = FileStorage(PATH)
        self.assertRaises(ApeError, storage.write, ('',))
        return

    def test_writeline(self):
        self.storage._file = self.mock_file
        self.storage.writeline('beta')
        self.mock_file.write.assert_called_with('beta\n')
        return

    def test_writelines(self):
        text = 'gamma delta sigma rho'.split()
        self.storage._file = self.mock_file
        self.storage.writelines(text)
        self.mock_file.writelines.assert_called_with(text)
        return

    def test_writeable(self):
        mocked = mock_open()
        name = 'ummagumma.txt'
        full_name = 'test/' + name
        storage = FileStorage('test/')
        with patch('__builtin__.open', mocked):
            self.assertFalse(storage.writeable)
            opened = storage.open(name)
            self.assertTrue(opened.writeable)
            opened.close()
            self.assertFalse(opened.writeable)
        return

    def test_close(self):
        mock_file = MagicMock()
        self.storage._file = mock_file
        self.storage.closed = False
        self.storage.close()
        mock_file.close.assert_called_with()
        self.assertTrue(self.storage.closed)
        return

    def tearDown(self):
        if os.path.isdir(PATH):
            shutil.rmtree(PATH)
        return

if __name__ == "__main__":
    unittest.main()



