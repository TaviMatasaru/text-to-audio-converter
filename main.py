import play_phrase
import convert_to_sound
import os
from tkinter import *
from tkinter import ttk
from gtts import gTTS
import pygame

pygame.mixer.init()

# global variable to chck if the audio is paused or not
global paused
paused = False


# function to clear the audio_box and update it with the sounds from the output dir
def update_sounds_list(sounds_dir_path):
    sounds_list = os.listdir(sounds_dir_path)
    # clear the audio_box
    audio_box.delete(0, END)

    # repopulate the audio_box with the sounds from the output dir
    for sound in sounds_list:
        audio_box.insert(END, sound)


# calls the read_and_porocess_files funciton from convert_to_sound.py for the specified input/output dirs and updates the audio_box
def convert_to_sound_and_update_list():
    convert_to_sound.read_and_process_files(
        input_dir_field.get(), output_dir_field.get())
    update_sounds_list(output_dir_field.get())


# when the play button is clicked, the selected sound from audio_box is played
def play_selected_sound():
    # get the selected sound from the audio_box
    sound = audio_box.get(ACTIVE)
    sound = f'{output_dir_field.get()}/{sound}'

    # play the sound
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


# stops the current playing sound
def stop_playing():
    pygame.mixer.music.stop()


# pauses the current playing sound
def pause_sound(is_paused):
    global paused
    paused = is_paused

    # pause / unpause sound
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# plays the previeous sound in the audio-box
def play_previeous():
    # get the current sound tuple (to extract the index)
    previeous_song_index = audio_box.curselection()

    # get the previeous sound index
    previeous_song_index = previeous_song_index[0] - 1

    # get the title of the previeous sound in the audio-box
    previeous_song = audio_box.get(previeous_song_index)

    # compose the path of the previeous sound
    previeous_song = f'{output_dir_field.get()}/{previeous_song}'

    # load and play the previeous sound
    pygame.mixer.music.load(previeous_song)
    pygame.mixer.music.play(loops=0)

    # clear the selection of the current sound from the audio-box and select the previeous sound
    audio_box.selection_clear(0, END)
    audio_box.activate(previeous_song_index)
    audio_box.selection_set(previeous_song_index, last=None)


def play_next():
    # get the current song tuple (to extract the index)
    next_song_index = audio_box.curselection()

    # get the next sound index
    next_song_index = next_song_index[0] + 1

    # get the title of the next sound in the audio-box
    next_song = audio_box.get(next_song_index)

    # compose the path of the next sound
    next_song = f'{output_dir_field.get()}/{next_song}'

    # load and play the next sound
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play(loops=0)

    # clear the selection of the current sound from the audio-box and select the next sound
    audio_box.selection_clear(0, END)
    audio_box.activate(next_song_index)
    audio_box.selection_set(next_song_index, last=None)



main_root = Tk()
main_root.title('Text to Speech Convertor')
main_root.geometry('800x800')

# Add the play_phrase_frame Frame from play_phrase.py and pack() it into main_root
play_phrase_frame = play_phrase.create_gui(main_root)
play_phrase_frame.pack()


# Create a separator between functionalities
functionalities_separator = ttk.Separator(main_root, orient='horizontal')
functionalities_separator.pack(fill='x', pady=20)

# Create Convert an entire directory label
convert_directory_label = Label(
    main_root, text='Convert each line from all .txt files from a directory')
convert_directory_label.pack()

# Create sounds list
audio_box = Listbox(main_root, bg="gray", width=60, height=20)

# Create frame for input and output dirs fields
io_dirs_frame = Frame(main_root)
io_dirs_frame.pack(pady=25)

input_dir_field_label = Label(io_dirs_frame, text="Input Dir:")
output_dir_field_label = Label(io_dirs_frame, text="Output Dir:")
input_dir_field = Entry(io_dirs_frame, width=30, justify=CENTER)
input_dir_field.insert(END, 'script-input')
output_dir_field = Entry(io_dirs_frame, width=30, justify=CENTER)
output_dir_field.insert(END, 'script-output')
convert_button = Button(io_dirs_frame, width=20, text='Convert',
                        command=convert_to_sound_and_update_list)

input_dir_field_label.grid(row=0, column=0)
output_dir_field_label.grid(row=0, column=1)
input_dir_field.grid(row=1, column=0)
output_dir_field.grid(row=1, column=1)
convert_button.grid(row=2, columnspan=2)


# pack songs list box
audio_box.pack(pady=20)

# Create media player icons
rewind_icon = PhotoImage(file='images/rewind-button-50.png')
play_icon = PhotoImage(file='images/play-button-50.png')
pause_icon = PhotoImage(file='images/pause-button-50.png')
stop_icon = PhotoImage(file='images/stop-button-50.png')
forward_icon = PhotoImage(file='images/forward-button-50.png')

# Create media player control frame
media_controls_frame = Frame(main_root)
media_controls_frame.pack(pady=20)

# Create media player buttons
rewind_button = Button(media_controls_frame,
                       image=rewind_icon, borderwidth=0, padx=30, command=play_previeous)
play_button = Button(media_controls_frame,
                     image=play_icon, borderwidth=0, padx=30, command=play_selected_sound)
pause_button = Button(media_controls_frame,
                      image=pause_icon, borderwidth=0, padx=30, command=lambda: pause_sound(paused))
stop_button = Button(media_controls_frame,
                     image=stop_icon, borderwidth=0, padx=30, command=stop_playing)
forward_button = Button(media_controls_frame,
                        image=forward_icon, borderwidth=0, padx=30, command=play_next)

rewind_button.grid(row=0, column=0)
play_button.grid(row=0, column=1)
pause_button.grid(row=0, column=2)
stop_button.grid(row=0, column=3)
forward_button.grid(row=0, column=4)

main_root.mainloop()
