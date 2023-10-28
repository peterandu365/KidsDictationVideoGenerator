# KidsDictationGenerator

Transform your list of words, phrases, or sentences into engaging audio-visual dictation materials tailored for kids! KidsDictationGenerator provides a sequence of scripts to process `.txt` files, converting text into repetitive dictation video clips and then formatting the text into structured Word documents for physical practice.

## Pipeline Steps:

### Step 01: Text Splitter (`01_splitter.py`):
- Segments larger `.txt` files into smaller files based on a specified number of words.
- Organizes the smaller files into directories named after the original file, ensuring easy management.

### Step 02: Multimedia Dictation Creator (`02_PhraseDictation.py`):
- Converts individual lines from a `.txt` file into audio using Google's Text-to-Speech.
- Renders corresponding video clips that display the text, synchronized with the audio duration.
- The audio and video are presented in repetitive sequences for better dictation and recall.
- Outputs a concatenated `.mp3` (audio) and `.mp4` (video) file for each `.txt` file, creating multimedia dictation resources.

### Step 03: Word Document Formatter (`03_txt_to_docx_four_line_grid.py`):
- Transforms `.txt` files into `.docx` documents.
- Text lines are formatted to avoid exceeding a set character limit, catering to young readers.
- Word documents come with a structured layout, including a blank line grid beneath each sentence, allowing kids to practice writing.

## Usage:

1. **Step 01**:
   - Place `01_splitter.py` in the directory with the `.txt` files containing your list of words, phrases, or sentences.
   - Execute the script.

2. **Step 02**:
   - After completing Step 01, place `02_PhraseDictation.py` in the directory with the segmented `.txt` files.
   - Execute the script to generate dictation audio and videos.

3. **Step 03**:
   - Place `03_txt_to_docx_four_line_grid.py` in the directory with the original or segmented `.txt` files.
   - Execute the script to produce practice Word documents.

## Dependencies:
- Ensure the required libraries are installed. Use pip:
  ```
  pip install docx gtts pydub moviepy textwrap
  ```
(Note: Always ensure compatibility and specific version requirements.)

## Citation

If you use this tool in your project or research, please cite:

```
Peter Xu, Kids Dictation Video Generator, https://github.com/peterandu365/KidsDictationVideoGenerator, 2023
```

## Future Enhancements:
- Seamless integration for a one-click pipeline execution.
- Introduction of varying difficulty levels for dictation.
- Potential for personalized themes and animations in video clips.

