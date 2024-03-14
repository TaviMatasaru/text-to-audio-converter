import os
from gtts import gTTS
import sys

# function that converts a phrase into a .mp3 file


def convert_line_to_audio(line, output_file):
    output_sound = gTTS(text=line, lang='ro', slow=False)
    output_sound.save(output_file)


# function that searches every .txt file from the input dir and for each line of text, calls convert_line_to_audio function
def read_and_process_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            print(file)
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        output_file = os.path.join(
                            output_dir, f'{line.strip()}.mp3')
                        convert_line_to_audio(line.strip(), output_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilizare: python convert_to_sound.py <director_input> <director_output>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    read_and_process_files(input_directory, output_directory)

# python3 convert_to_sound.py script-input script-output
