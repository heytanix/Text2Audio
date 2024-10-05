# Import the required libraries
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, output_filename="output.mp3"):
    try:
        # Create gTTS object
        tts = gTTS(text=text, lang='en')
        # Save the converted speech to an mp3 file
        tts.save(output_filename)
        print(f"Audio saved as {output_filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Function to read text from a file
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Main function to handle user input or file upload
def main():
    print("Text-to-Speech Converter")
    print("Choose input method:")
    print("1. Enter text manually")
    print("2. Upload a text file")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        text = input("Enter the text you want to convert to speech: ")
        output_filename = input("Enter the name of the output audio file (with .mp3 extension): ")
        text_to_speech(text, output_filename)
    elif choice == '2':
        file_path = input("Enter the path to the text file: ")
        text = read_text_file(file_path)
        if text:
            output_filename = input("Enter the name of the output audio file (with .mp3 extension): ")
            text_to_speech(text, output_filename)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
