"""
Test Suite for NLP_API
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock


class TestProject(unittest.TestCase):
    def setUp(self):
        """Setup all variables mocks and things for all test steps
        """
        return super().setUp()

    def test_hello_world(self):
        """Test the /api/hello_world endpoint
        """
        self.assertEqual(2+2, 4)

    def tearDown(self):
        """Undo all things setted up for those tests
        """
        return super().tearDown()
