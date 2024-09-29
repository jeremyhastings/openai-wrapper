from config import logging_setup
from openai_wrapper.text_client import generate_text
from openai_wrapper.image_client import generate_image
from openai_wrapper.embedding_client import create_vector_embeddings

# Call the function to configure logging
logger = logging_setup.logger

def display_menu():
    """
    Displays the menu options to the user.

    This function prints the options available for the user to interact
    with the OpenAI API. Currently, the options include sending a
    question to ChatGPT and generating an image.
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
    The user can choose to send a prompt to ChatGPT for a text response 
    or generate an image. The loop continues until the user types 'EXIT'.
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
            response = generate_text(user_input, logger)
            if response:
                print(response)

        elif user_choice == '2':
            user_input = input("Enter your prompt for image generation: ")
            # Generate image based on the prompt and display the URLs
            urls = generate_image(user_input, logger)
            if urls:
                for url in urls:
                    print(url)

        elif user_choice == '3':
            user_input = input("Enter your prompt for vector embeddings: ")
            # Create vector embeddings based on the input text
            response = create_vector_embeddings(user_input, logger)
            if response:
                print(response)

        else:
            print("Invalid choice. Please select a valid option.")