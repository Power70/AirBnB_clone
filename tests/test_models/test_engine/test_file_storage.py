#!/usr/bin/python3
"""FileStorage class unit tests"""
import io
import unittest
from contextlib import redirect_stdout
from datetime import datetime
from pycodestyle import Checker
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test class or BaseModel"""
    def test_pep8_compliance(self):
        """checks that code conforms to pep8 style"""
        files_to_check = [
                'models/engine/file_storage.py',
                'tests/test_models/test_engine/test_file_storage.py'
                ]

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            style = Checker(paths=files_to_check)
            result = style.check_all()

        output = stdout.getvalue().strip()
        self.assertFalse(output, f"PEP8 violations found:\n{output}")

    def test_file_path_exists(self):
        """Test to check that the __file_path attribute exists"""
        file_instance = FileStorage()
        self.assertTrue('_FileStorage__file_path' in dir(
            file_instance.__class__))

    def test_file_path_match(self):
        """Test to check if the __file_path name/value matches"""
        expected_file_path = "file.json"
        file_instance = FileStorage()

        # get the private attribute from the custom helper method
        returned_file_path = file_instance.file_path

        self.assertEqual(returned_file_path, expected_file_path)

    def test_objects_exists(self):
        """Test to check that the __objects attribute exists"""
        file_instance = FileStorage()
        self.assertTrue('_FileStorage__file_path' in dir(
            file_instance.__class__))

    def test_objects_reference(self):
        """Test to check if different file instances point to same object"""
        file_instance1 = FileStorage()
        file_instance2 = FileStorage()

        # get the private attributes from the custome helper method
        self.assertIs(file_instance1.objects, file_instance2.objects)

    def test_all(self):
        """The all method test"""
        file_instance = FileStorage()
        expected_objects = file_instance.objects
        returned_objects = file_instance.all()

        self.assertEqual(expected_objects, returned_objects)


if __name__ == '__main__':
    unittest.main()
