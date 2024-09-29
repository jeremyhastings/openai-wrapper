from config import logging_setup
from openai_wrapper.text_client import TextClient
from openai_wrapper.image_client import ImageClient
from openai_wrapper.embedding_client import EmbeddingClient

# Create instances of the clients
text_client = TextClient()
image_client = ImageClient()
embedding_client = EmbeddingClient()

# Use the logger instance from one of the clients as they all share the same logger
logger = text_client.logger

def display_menu():
    """
    Displays the menu options to the user.

    This function prints the options available for the user to interact
    with the OpenAI API. The options include:
    1. Generating text using ChatGPT
    2. Generating an image based on a text prompt
    3. Creating vector embeddings from a text input
    The user can also type 'EXIT' to quit the program.
    """
    print("Menu:")
    print("1. Generate Text")
    print("2. Generate an Image")
    print("3. Create Vector Embeddings")
    print("Type 'EXIT' to quit")
    print()


# Prompt the user for input in a loop
if __name__ == '__main__':
    """
    Main loop for user interaction with the OpenAI API.

    This loop continuously displays the menu to the user, accepts user 
    input for various options, and processes the input accordingly. 
    The user can choose to:
    1. Send a prompt to ChatGPT for a text response
    2. Generate an image based on a text prompt 
    3. Create vector embeddings from a text input
    The loop continues until the user types 'EXIT'.
    """
    while True:
        display_menu()
        user_choice = input("Choose an option: ")

        # Check if the user wants to exit
        if user_choice.upper() == 'EXIT':
            print("Exiting the program...")
            break

        if user_choice == '1':
            user_input = input("Enter your prompt for text generation: ")
            # Send prompt to ChatGPT and display the response
            response = text_client.generate_text(user_input)
            if response:
                print(response)

        elif user_choice == '2':
            user_input = input("Enter your prompt for image generation: ")
            # Generate image based on the prompt and display the URLs
            urls = image_client.generate_image(user_input)
            if urls:
                for url in urls:
                    print(url)

        elif user_choice == '3':
            user_input = input("Enter your prompt for vector embeddings: ")
            # Create vector embeddings based on the input text
            response = embedding_client.create_vector_embeddings(user_input)
            if response:
                print(response)

        else:
            print("Invalid choice. Please select a valid option.")