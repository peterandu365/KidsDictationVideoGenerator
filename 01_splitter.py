import os

WORD_NUMBER = 10

def split_txt_file(filename):
    with open(filename, 'r') as file:
        words = file.readlines()

    total_files = len(words) // WORD_NUMBER
    if len(words) % WORD_NUMBER != 0:
        total_files += 1

    base_filename = os.path.splitext(filename)[0]  # Extracts the base name of the file without extension

    # Create a folder with the same name as the original txt file name except for the .txt extension
    if not os.path.exists(base_filename):
        os.mkdir(base_filename)

    # Move the original txt file into that folder
    os.rename(filename, os.path.join(base_filename, filename))
    
    for i in range(total_files):
        start_index = i * WORD_NUMBER
        end_index = start_index + WORD_NUMBER

        new_filename = f"{base_filename}_{str(i+1).zfill(3)}.txt"
        with open(new_filename, 'w') as subfile:
            subfile.writelines(words[start_index:end_index])

if __name__ == "__main__":
    # Get all txt files in the current directory
    txt_files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.txt')]

    # Process each txt file
    for txt_file in txt_files:
        split_txt_file(txt_file)
