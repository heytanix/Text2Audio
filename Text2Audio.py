# Importing the necessary libraries
from gtts import gTTS  # Google's text-to-speech library
import os  # Library for handling file system operations

# Function to convert the provided text into speech and save it as an MP3 file
def text_to_speech(text, output_filename="output.mp3"):
    """
    Converts the given text into speech using Google TTS and saves it as an MP3 file.

    :param text: The text to be converted to speech.
    :param output_filename: The name of the output audio file (default is 'output.mp3').
    """
    try:
        # Creating a gTTS object with the provided text and English language
        tts = gTTS(text=text, lang='en')
        
        # Saving the generated speech to an MP3 file
        tts.save(output_filename)
        print(f"Audio saved as {output_filename}")  # Notify user that the file has been saved
    except Exception as e:
        # Handle any errors that occur during the text-to-speech conversion
        print(f"Error occurred: {e}")

# Function to read text content from a file
def read_text_file(file_path):
    """
    Reads text from a file and returns it as a string.

    :param file_path: Path to the text file.
    :return: The text content of the file, or None if an error occurs.
    """
    try:
        # Opening the file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()  # Return the content of the file
    except Exception as e:
        # Handle any errors that occur while reading the file
        print(f"Error reading file: {e}")
        return None  # Return None if reading the file fails

# Main function to manage user input and initiate text-to-speech conversion
def main():
    """
    Main function that allows users to either manually input text or upload a text file
    for conversion to speech.
    """
    print("Text-to-Speech Converter")
    print("Choose input method:")
    print("1. Enter text manually")
    print("2. Upload a text file")

    # Prompt the user to choose how they want to provide input
    choice = input("Enter your choice (1/2): ")

    # If user chooses to manually input text
    if choice == '1':
        text = input("Enter the text you want to convert to speech: ")  # Get text input from user
        output_filename = input("Enter the name of the output audio file (with .mp3 extension): ")  # Get desired output filename
        text_to_speech(text, output_filename)  # Convert the entered text to speech

    # If user chooses to upload a text file
    elif choice == '2':
        file_path = input("Enter the path to the text file: ")  # Get the file path from the user
        text = read_text_file(file_path)  # Read the text from the file
        if text:  # Check if text was successfully read
            output_filename = input("Enter the name of the output audio file (with .mp3 extension): ")  # Get desired output filename
            text_to_speech(text, output_filename)  # Convert the file's text to speech
    else:
        # Notify the user if they made an invalid choice
        print("Invalid choice. Please select 1 or 2.")

# Entry point of the script
if __name__ == "__main__":
    main()  # Start the text-to-speech conversion process
