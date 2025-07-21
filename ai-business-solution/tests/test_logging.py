import unittest
from src.logging_config import setup_logging
import logging

class TestLogging(unittest.TestCase):
    def test_logging(self):
        logger = setup_logging()
        self.assertIsInstance(logger, logging.Logger)
