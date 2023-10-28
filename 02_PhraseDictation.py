import os
import sys
from gtts import gTTS
from pydub import AudioSegment
from moviepy.editor import TextClip, concatenate_videoclips
import time
from pydub.utils import mediainfo
from moviepy.editor import concatenate_videoclips, AudioFileClip, VideoFileClip

# Constants
SILENCE_DURATION = 3000
INTERVAL_PER_EXTRA_CHAR = 500
FPS = 2  # Video frames per second

def get_first_letter(s):
    for char in s:
        if char.isalpha():
            return char
    return ''

def text_to_audio_and_video(phrase):
    first_letter = get_first_letter(phrase)
    
    # Generate Audio
    audio_filename = f"temp_audio_{first_letter}_{time.time()}.mp3"
    tts = gTTS(phrase, lang="en")
    tts.save(audio_filename)
    
    # Get Audio Duration
    audio_info = mediainfo(audio_filename)
    audio_duration = float(audio_info['duration'])
    
    # Generate Video
    video_clip = TextClip(phrase, fontsize=500, color='black', bg_color='white', font="KG-Primary-Penmanship-Lined").set_duration(audio_duration)
    video_clip = video_clip.resize(1.2)  # This doubles the resolution
    video_filename = f"temp_video_{first_letter}_{time.time()}.mp4"
    video_clip.write_videofile(video_filename, fps=FPS)
    
    return audio_filename, video_filename

def main(input_txt, output_audio, output_video):
    concatenated_audio = AudioSegment.empty()
    video_clips = []
    with open(input_txt, 'r') as f:
        for line in f:
            phrase = line.strip()
            if not phrase:
                continue

            audio_filename, video_filename = text_to_audio_and_video(phrase)
            audio_segment = AudioSegment.from_mp3(audio_filename)
            
            for i in range(3):  
                concatenated_audio += audio_segment
                
                video_clip = VideoFileClip(video_filename)
                video_clips.append(video_clip)
                
                if i == 2:
                    silence_duration = SILENCE_DURATION + max(0, len(phrase) - 3) * INTERVAL_PER_EXTRA_CHAR
                else:
                    silence_duration = SILENCE_DURATION
                
                silent_video = TextClip(phrase, fontsize=500, color='black', bg_color='white', font="KG-Primary-Penmanship-Lined").set_duration(silence_duration / 1000.0)
                silent_video = silent_video.resize(1.2)
                video_clips.append(silent_video)
                
                # Add silence to audio
                silence = AudioSegment.silent(duration=silence_duration)
                concatenated_audio += silence
            
            os.remove(audio_filename)
            os.remove(video_filename)

    concatenated_audio.export(output_audio, format="mp3")

    final_video = concatenate_videoclips(video_clips, method="compose")
    audio = AudioFileClip(output_audio)
    final_video = final_video.set_audio(audio)
    final_video.write_videofile(output_video, audio_codec='aac')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_txt_path = sys.argv[1]
        if not input_txt_path.endswith('.txt'):
            print(f"Error: {input_txt_path} is not a .txt file.")
            sys.exit(1)
        
        output_audio_path = os.path.splitext(input_txt_path)[0] + ".mp3"
        output_video_path = os.path.splitext(input_txt_path)[0] + ".mp4"
        main(input_txt_path, output_audio_path, output_video_path)
    else:
        for file in os.listdir("."):
            if file.endswith(".txt"):
                input_txt_path = file
                output_audio_path = os.path.splitext(file)[0] + ".mp3"
                output_video_path = os.path.splitext(file)[0] + ".mp4"
                main(input_txt_path, output_audio_path, output_video_path)
