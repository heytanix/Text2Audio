#Importing the required libraries for the Pyhton script
from gtts import gTTS #This is a TTS(Text to speech library from Google)
import os

#Function for converting the text into speech
def text_to_speech(text, output_filename="output.mp3"): #defining a function within the script
    try:
        #Creating gTTS object
        tts = gTTS(text=text, lang='en')
        #Saving the converted speech into an mp3 file
        tts.save(output_filename)
        print(f"Audio saved as {output_filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

#Defining a function to read text from a file
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

#The main function to handle user's input or file uploads
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
