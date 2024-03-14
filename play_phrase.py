import os
from tkinter import *
from gtts import gTTS
import pygame


# when the play button is clicked the phrase from the input filed is turned into .mp3 file and is played
def play_button_clicked(input_text):
    # transform the text into audio
    output_sound = gTTS(text=input_text, lang='ro', slow=False)
    output_sound.save('play-phrase-output/output_sound.mp3')

    # play the audio
    pygame.mixer.music.load('play-phrase-output/output_sound.mp3')
    pygame.mixer.music.play(loops=0)


# function to create the GUI
def create_gui(root_window):
    # the main frame of the GUI
    frame = Frame(root_window)
    frame.pack(pady=20)

    # Add input field label
    input_field_label = Label(frame, text='Enter a Phrase below and play it:')
    input_field_label.grid(row=0, column=0)

    # Add input field
    input_field = Entry(frame, width=50)
    input_field.grid(row=1, column=0)

    # Add play button
    play_button = Button(
        frame, text="Play", command=lambda: play_button_clicked(input_field.get()))
    play_button.grid(row=1, column=2)

    return frame


if __name__ == "__main__":
    root = Tk()
    root.title('Phrase to Sound')
    root.geometry("800x150")
    pygame.mixer.init()
    create_gui(root)
    root.mainloop()
