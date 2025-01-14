import os
import random
from pydub import AudioSegment
from pydub.generators import Sine

def add_silent_gap(audio_path, gap_duration_ms=200, min_gap_position_ms=500):
    audio = AudioSegment.from_file(audio_path)
    gap_duration_ms = min(gap_duration_ms, len(audio))
    max_position = len(audio) - gap_duration_ms
    if max_position < min_gap_position_ms:
        print(f"Warning: Audio file '{audio_path}' is too short to insert the gap at the desired position.")
        return audio  
    gap_position_ms = random.randint(min_gap_position_ms, max_position)
    
    silence = AudioSegment.silent(duration=gap_duration_ms)
    first_part = audio[:gap_position_ms]
    second_part = audio[gap_position_ms:]
    new_audio = first_part + silence + second_part
    return new_audio

def process_audio_files(input_folder, output_folder, gap_duration_ms=200):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(('.wav', '.mp3', '.flac', '.ogg')):
            print(f"Processing file: {filename}")
            
            modified_audio = add_silent_gap(file_path, gap_duration_ms)
            
            output_file_path = os.path.join(output_folder, filename)
            modified_audio.export(output_file_path, format="wav")  
            print(f"Saved modified file to: {output_file_path}")

if __name__ == "__main__":
    input_folder = '/Users/johannasmriti/Downloads/musicnet/Denoising_Audio/noise_data_clean'  
    output_folder = '/Users/johannasmriti/Downloads/musicnet/data_with_gaps'  
    
    gap_duration_ms = 200  
    
    process_audio_files(input_folder, output_folder, gap_duration_ms)
