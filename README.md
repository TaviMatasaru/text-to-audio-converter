# Text-to-Speech Conversion Project Documentation

## Overview

This project facilitates the conversion of text from `.txt` files to speech in the form of `.mp3` files using Google's Text-to-Speech API (gTTS). It also provides a graphical user interface (GUI) to play, pause, and navigate through the generated audio files. The project consists of three main Python scripts: `convert_to_sound.py`, `play_phrase.py`, and `main.py`.

## Scripts

### convert_to_sound.py

This script scans a specified directory for `.txt` files and converts each line of text into an `.mp3` file saved in a designated output directory.

#### Functions

- `convert_line_to_audio(line, output_file)`: Converts a single line of text to speech and saves it as an `.mp3` file.
- `read_and_process_files(input_dir, output_dir)`: Processes each `.txt` file in the specified input directory, converting lines to audio files in the specified output directory.

### play_phrase.py

Provides a GUI where users can enter a phrase, convert it to speech, and play it immediately.

#### Functions

- `play_button_clicked(input_text)`: Converts the text from an input field to an `.mp3` file and plays it.
- `create_gui(root_window)`: Builds the GUI components including labels, entry fields, and buttons.

### main.py

Integrates functionalities of `convert_to_sound.py` and `play_phrase.py` into a single GUI. It provides comprehensive controls for audio playback including play, pause, stop, next, and previous, along with capabilities to convert entire directories from text to speech.

#### Functions

- `update_sounds_list(sounds_dir_path)`: Updates the list of audio files in the GUI.
- `convert_to_sound_and_update_list()`: Converts text files to audio and updates the GUI list.
- `play_selected_sound()`: Plays the selected audio file from the list.
- `stop_playing()`: Stops audio playback.
- `pause_sound(is_paused)`: Toggles pause and unpause on the current audio.
- `play_previous()`: Plays the previous audio file in the list.
- `play_next()`: Plays the next audio file in the list.

## Running the Project

To run the project, execute the `main.py` script after navigating to the project directory:

```bash
python main.py
```bash
