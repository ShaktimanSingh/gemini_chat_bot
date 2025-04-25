# import google.generativeai as genai
# import logging
# import json

# API_KEY = "AIzaSyDykTo_wFomfAt8zPKH7mJnEKYVWIy5S2s"
# MODEL_NAME = "gemini-2.0-flash"
# genai.configure(api_key=API_KEY)

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# def get_gemini_response_stream(prompt: str):
#     """
#     Streams a Gemini response for a given prompt using send_message_stream().
#     Yields tokens one-by-one.
#     """
#     try:
#         model = genai.GenerativeModel(MODEL_NAME)
#         chat = model.start_chat()
#         response_stream = chat.send_message_async(prompt)

#         for chunk in response_stream:
#             yield chunk.text  # Each chunk contains part of the response

#     except Exception as e:
#         logger.error(f"Gemini streaming failed: {e}")
#         yield "Error: Could not generate response."

# # Local CLI Simulator
# def run_local_chat():
#     logger.info("Gemini Chat Bot")
#     logger.info("Type your message. Type 'exit' to quit.\n")

#     while True:
#         user_input = input("You: ").strip()
#         if user_input.lower() in {"exit", "quit"}:
#             print("👋 Exiting. Goodbye!")
#             break

#         event = {
#             "body": json.dumps({"message": user_input})
#         }

#         print("Gemini: ", end="", flush=True)
#         for token in get_gemini_response_stream(event):
#             print(token, end="", flush=True)
#         print("\n")


# # Entry Point
# if __name__ == "__main__":
#     run_local_chat()


import asyncio
import google.generativeai as genai

# Your Gemini API key
API_KEY = "AIzaSyDykTo_wFomfAt8zPKH7mJnEKYVWIy5S2s"
MODEL_NAME = "gemini-2.0-flash"

# Configure Gemini with your API key
genai.configure(api_key=API_KEY)


async def get_gemini_response_stream(prompt):
    # Async function to stream Gemini's response
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        chat = model.start_chat()

        # Send message and await the async stream
        response_stream = await chat.send_message_async(prompt)

        # Stream each token as it arrives
        async for chunk in response_stream:
            print(chunk.text, end="", flush=True)
        print()  # Finish line after stream

    except Exception as e:
        print(f"\nError: {e}")


async def main():
    # Entry point for the async terminal chat
    print("Welcome to Gemini Chat! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Goodbye 👋")
            break
        print("Gemini: ", end="")
        await get_gemini_response_stream(user_input)

# Start the async event loop
if __name__ == "__main__":
    asyncio.run(main())
