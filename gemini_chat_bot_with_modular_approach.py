import google.generativeai as genai
import logging

# --------------------- Configuration ---------------------

API_KEY = "AIzaSyDykTo_wFomfAt8zPKH7mJnEKYVWIy5S2s"
MODEL_NAME = "gemini-2.0-flash"

# --------------------- Setup Logging ---------------------

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
# )
# logger = logging.getLogger(__name__)

# --------------------- Gemini Chat Class ---------------------


class GeminiChatBot:
    def __init__(self, api_key: str, model_name: str = MODEL_NAME):
        self.api_key = api_key
        self.model_name = model_name
        self.chat = None
        self._initialize()

    def _initialize(self):
        try:
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel(self.model_name)
            self.chat = model.start_chat()
            logging.info(f"Initialized Gemini model: {self.model_name}")
        except Exception as e:
            logging.error(f"Failed to initialize Gemini model: {e}")
            raise

    def get_response(self, message: str) -> str:
        try:
            response = self.chat.send_message(message)
            return response.text.strip()
        except Exception as e:
            logging.error(f"Error while sending message: {e}")
            return "Error: Failed to get a response from the model."

# --------------------- Main CLI Interface ---------------------


def run_chat():
    bot = GeminiChatBot(api_key=API_KEY)

    print("Welcome to the Gemini Chat Bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting Gemini Chat Bot. Goodbye!")
            break

        if not user_input:
            print("Please enter a message.")
            continue

        response = bot.get_response(user_input)
        print("Gemini:", response)

# --------------------- Entry Point ---------------------


if __name__ == "__main__":
    run_chat()
