import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string

def process_input(input_text):
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 
               'do you have money', 'do you want something to drink', 'do you want tea or coffee', 
               'do you watch TV', 'dont worry', 'flower is beautiful', 'good afternoon', 'good evening', 
               'good morning', 'good night', 'good question', 'had your lunch', 'happy journey', 
               'hello what is your name', 'how many people are there in your family', 'i am a clerk', 
               'i am bore doing nothing', 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 
               'i dont understand anything', 'i go to a theatre', 'i love to shop', 
               'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 
               'lets go for lunch', 'my mother is a homemaker', 'my name is john', 'nice to meet you', 
               'no smoking please', 'open the door', 'please call me later', 'please clean the room', 
               'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 
               'shall I help you', 'shall we go together tomorrow', 'sign language interpreter', 'sit down', 
               'stand up', 'take care', 'there was traffic jam', 'wait I am thinking', 'what are you doing', 
               'what is the problem', 'what is todays date', 'what is your father do', 'what is your job', 
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 
               'when we will go', 'where do you stay', 'where is the bathroom', 'where is the police station', 
               'you are wrong', 'address', 'agra', 'ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 
               'badoda', 'banana', 'banaras', 'bangalore', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 
               'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara', 'deaf', 'december', 'deer', 
               'delhi', 'dollar', 'duck', 'february', 'friday', 'fruits', 'glass', 'grapes', 'gujarat', 'hello', 
               'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'karnataka', 'kerala', 'krishna', 
               'litre', 'mango', 'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 
               'orange', 'pakistan', 'pass', 'police station', 'post office', 'pune', 'punjab', 'rajasthan', 
               'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica', 'story', 'sunday', 
               'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 
               'village', 'voice', 'wednesday', 'weight']

    arr = list(string.ascii_lowercase)
    
    input_text = input_text.lower()

    for c in string.punctuation:
        input_text = input_text.replace(c, "")

    if input_text in isl_gif:
        display_gif(input_text)
    else:
        display_letters(input_text, arr)


def display_gif(phrase):
    class ImageLabel(tk.Label):
        """A label that displays images and plays them if they are GIFs"""
        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            self.loc = 0
            self.frames = []
            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image=None)
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)

    root = tk.Tk()
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load(f'ISL_Gifs/{phrase}.gif')
    root.mainloop()


def display_letters(text, arr):
    for letter in text:
        if letter in arr:
            ImageAddress = f'letters/{letter}.jpg'
            ImageItself = Image.open(ImageAddress)
            ImageNumpyFormat = np.asarray(ImageItself)
            plt.imshow(ImageNumpyFormat)
            plt.draw()
            plt.pause(1)
        else:
            continue
    plt.close()


def func():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("I am Listening")
        audio = r.listen(source)

        try:
            speech_text = r.recognize_google(audio).lower()
            print(f'You Said: {speech_text}')
            process_input(speech_text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, I could not request results.")


# Main program
while True:
    image = "signlang.png"
    msg = "HEARING IMPAIRMENT ASSISTANT"
    choices = ["Live Voice", "Input Text", "All Done!"]
    reply = buttonbox(msg, image=image, choices=choices)
    
    if reply == "Live Voice":
        func()
    elif reply == "Input Text":
        input_text = enterbox("Enter the text you want to convert:")
        if input_text:
            process_input(input_text)
    elif reply == "All Done!":
        quit()
