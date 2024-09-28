import logger_setup
from chatgpt_client import send_prompt_to_chatgpt
from image_client import generate_image

# Call the function to configure logging
logger_setup.setup_logging()

# Example of using the logger instance
logger = logger_setup.logger

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
    print("2. Generate an image")
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
            user_input = input("Enter your prompt for ChatGPT: ")

        elif user_choice == '2':
            user_input = input("Enter your prompt for image generation: ")
            # Generate image based on the prompt and display the URLs
            generate_image(user_input, logger)

            # Send prompt to ChatGPT and display the response
            send_prompt_to_chatgpt(user_input, logger)

        else:
            print("Invalid choice. Please select a valid option.")