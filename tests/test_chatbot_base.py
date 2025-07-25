# tests/test_chatbot_base.py
import os
import unittest
from unittest.mock import patch, MagicMock
from src.chatbot_base import BaseChatbot

class ConcreteChatbot(BaseChatbot):
    """A concrete implementation of BaseChatbot for testing purposes."""
    def _initialize_client(self):
        # In a real test, you might mock this client
        return MagicMock()

    def _get_response(self):
        # Mock a response
        return "This is a test response."

class TestBaseChatbot(unittest.TestCase):

    @patch.dict(os.environ, {"TEST_API_KEY": "test_key", "TEST_MODEL": "test_model"})
    def test_initialization_with_env_vars(self):
        """Tests that the chatbot initializes correctly with environment variables."""
        chatbot = ConcreteChatbot(
            api_key_name="TEST_API_KEY",
            model_env_name="TEST_MODEL",
            default_model="default"
        )
        self.assertEqual(chatbot.api_key, "test_key")
        self.assertEqual(chatbot.model_name, "test_model")

    @patch.dict(os.environ, {"TEST_API_KEY": "test_key"})
    def test_initialization_with_default_model(self):
        """Tests that the chatbot falls back to the default model if the env var is not set."""
        # Ensure the model env var is not set
        if "TEST_MODEL" in os.environ:
            del os.environ["TEST_MODEL"]
            
        chatbot = ConcreteChatbot(
            api_key_name="TEST_API_KEY",
            model_env_name="TEST_MODEL",
            default_model="default_model_name"
        )
        self.assertEqual(chatbot.model_name, "default_model_name")

    def test_missing_api_key_raises_error(self):
        """Tests that a ValueError is raised if the API key is not found."""
        # Ensure the API key env var is not set
        if "MISSING_API_KEY" in os.environ:
            del os.environ["MISSING_API_KEY"]

        with self.assertRaises(ValueError) as context:
            ConcreteChatbot(
                api_key_name="MISSING_API_KEY",
                model_env_name="ANY_MODEL",
                default_model="default"
            )
        self.assertTrue("MISSING_API_KEY is not set" in str(context.exception))

if __name__ == "__main__":
    unittest.main()
