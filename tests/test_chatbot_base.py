# tests/test_chatbot_base.py
import os
import unittest
from unittest.mock import patch, MagicMock
from src.chatbot_base import BaseChatbot

class ConcreteChatbot(BaseChatbot):
    """A concrete implementation of BaseChatbot for testing purposes."""
    def _initialize_client(self):
        return MagicMock()

    def _get_response(self):
        return "This is a test response."

@patch('src.chatbot_base.load_dotenv') # Prevent loading .env file during tests
class TestBaseChatbot(unittest.TestCase):

    @patch.dict(os.environ, {"TEST_API_KEY": "test_key", "TEST_MODEL": "test_model"})
    def test_initialization_with_env_vars(self, mock_load_dotenv):
        """Tests that the chatbot initializes correctly with environment variables."""
        chatbot = ConcreteChatbot(
            api_key_name="TEST_API_KEY",
            model_env_name="TEST_MODEL"
        )
        self.assertEqual(chatbot.api_key, "test_key")
        self.assertEqual(chatbot.model_name, "test_model")

    def test_missing_api_key_raises_error(self, mock_load_dotenv):
        """Tests that a ValueError is raised if the API key is not found."""
        with patch.dict(os.environ, {"TEST_MODEL": "test_model"}):
            if "TEST_API_KEY" in os.environ:
                del os.environ["TEST_API_KEY"]
            
            with self.assertRaises(ValueError) as context:
                ConcreteChatbot(api_key_name="TEST_API_KEY", model_env_name="TEST_MODEL")
            self.assertIn("TEST_API_KEY is not set", str(context.exception))

    def test_missing_model_raises_error(self, mock_load_dotenv):
        """Tests that a ValueError is raised if the model env var is not set."""
        with patch.dict(os.environ, {"TEST_API_KEY": "test_key"}):
            if "TEST_MODEL" in os.environ:
                del os.environ["TEST_MODEL"]

            with self.assertRaises(ValueError) as context:
                ConcreteChatbot(api_key_name="TEST_API_KEY", model_env_name="TEST_MODEL")
            self.assertIn("TEST_MODEL is not set", str(context.exception))

if __name__ == "__main__":
    unittest.main()
