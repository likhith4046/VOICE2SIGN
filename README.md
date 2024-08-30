# VOICE2SIGN

This project is a software application designed to assist individuals with hearing impairments by translating spoken words and phrases into Indian Sign Language (ISL) animations and displaying corresponding alphabet images for text input. The application leverages speech recognition and image processing to provide an accessible way for people with hearing disabilities to understand spoken language or text.

Key Features:

Live Voice Recognition:

The application can capture live voice input using a microphone. It employs the speech_recognition library to process and transcribe the audio into text.
Once the spoken words are recognized, the application checks if the phrase is available in its predefined ISL GIF library.
If a matching GIF is found, it is displayed to convey the meaning of the spoken phrase through ISL.
Text Input Conversion:

The application also accepts text input from the user. The text can be directly typed into the program.
Similar to voice input, the text is analyzed to see if it matches any of the predefined phrases in the ISL library.
If a match is found, the corresponding GIF is displayed. If not, the application breaks down the text into individual letters and displays images representing each letter in sign language.
ISL GIF and Alphabet Display:

The project includes a library of GIFs that represent common phrases in ISL. When a phrase is recognized, the GIF is displayed in a new window using Tkinter.
For letters not covered by phrases, the application displays corresponding sign language images using Matplotlib.
