# tests/test_model_bots.py
import unittest
from unittest.mock import patch, MagicMock

# Mock the base class to isolate the subclass logic
import src.chatbot_base as chatbot_base
chatbot_base.BaseChatbot.run = MagicMock() # Prevent the main loop from running

# Import the classes to be tested
from src.bot import OpenAIChatbot
from src.gem import GeminiChatbot
from src.plex import PerplexityChatbot
from src.anthropic import AnthropicChatbot
from src.grok import GrokChatbot

class TestModelBots(unittest.TestCase):

    @patch.dict('os.environ', {'OPENAI_API_KEY': 'fake_key'})
    @patch('src.bot.OpenAI')
    def test_openai_bot_initialization(self, mock_openai):
        """Tests that OpenAIChatbot initializes the OpenAI client correctly."""
        bot = OpenAIChatbot()
        mock_openai.assert_called_once_with(api_key='fake_key')
        self.assertIsNotNone(bot.client)

    @patch.dict('os.environ', {'GOOGLE_API_KEY': 'fake_key'})
    @patch('src.gem.genai')
    def test_gemini_bot_initialization(self, mock_genai):
        """Tests that GeminiChatbot configures the genai client."""
        bot = GeminiChatbot()
        mock_genai.configure.assert_called_once_with(api_key='fake_key')
        mock_genai.GenerativeModel.assert_called_once()
        self.assertIsNotNone(bot.client)

    @patch.dict('os.environ', {'PERPLEXITY_API_KEY': 'fake_key'})
    @patch('src.plex.OpenAI')
    def test_perplexity_bot_initialization(self, mock_openai):
        """Tests that PerplexityChatbot initializes the OpenAI client with the correct base URL."""
        bot = PerplexityChatbot()
        mock_openai.assert_called_once_with(api_key='fake_key', base_url='https://api.perplexity.ai')
        self.assertIsNotNone(bot.client)

    @patch.dict('os.environ', {'ANTHROPIC_API_KEY': 'fake_key'})
    @patch('src.anthropic.OpenAI')
    def test_anthropic_bot_initialization(self, mock_openai):
        """Tests that AnthropicChatbot initializes the OpenAI client with the correct base URL."""
        bot = AnthropicChatbot()
        mock_openai.assert_called_once_with(api_key='fake_key', base_url='https://api.anthropic.com/v1')
        self.assertIsNotNone(bot.client)

    @patch.dict('os.environ', {'GROK_API_KEY': 'fake_key'})
    @patch('src.grok.OpenAI')
    def test_grok_bot_initialization(self, mock_openai):
        """Tests that GrokChatbot initializes the OpenAI client with the correct base URL."""
        bot = GrokChatbot()
        mock_openai.assert_called_once_with(api_key='fake_key', base_url='https://api.x.ai/v1')
        self.assertIsNotNone(bot.client)

if __name__ == '__main__':
    unittest.main()
