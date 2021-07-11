import unittest
import utilities


class TestUtilities(unittest.TestCase):
    def test_id_valid(self):
        result = utilities.id_valid("9903155793082")
        self.assertTrue(result, "Id is invalid")

        result = utilities.id_valid("1999031793082")
        self.assertFalse(result, "Id is not invalid")

    def test_not_empty(self):
        result = utilities.not_empty("Not empty")
        self.assertTrue(result, "String is empty")

        result = utilities.not_empty("")
        self.assertFalse(result, "String is not empty")

    def test_user_exists(self):
        result = utilities.user_exists("Luyanda", "9903155793082")
        self.assertTrue(result, "User doesnt exist")

        result = utilities.user_exists("Peter", "9903155793082")
        self.assertFalse(result, "User exists")

    def test_admin_exists(self):
        result = utilities.admin_exists("Luyanda", "9903155793082")
        self.assertTrue(result, "User is not admin")

        result = utilities.admin_exists("Peter", "9903155793082")
        self.assertFalse(result, "User is admin")

