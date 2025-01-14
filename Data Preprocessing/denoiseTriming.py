import os
from pydub import AudioSegment

def split_audio(input_folder, output_folder, split_duration_ms=5000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if filename.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a')):
            try:
                audio = AudioSegment.from_file(file_path)
                audio_length_ms = len(audio)
                for start_time_ms in range(0, audio_length_ms, split_duration_ms):
                    end_time_ms = min(start_time_ms + split_duration_ms, audio_length_ms)
                    segment = audio[start_time_ms:end_time_ms]
                    base_name, ext = os.path.splitext(filename)
                    output_filename = f"{base_name}_part{start_time_ms // split_duration_ms + 1}{ext}"
                    output_path = os.path.join(output_folder, output_filename)
                    segment.export(output_path, format="mp3") 
                    print(f"Saved {output_filename} to {output_folder}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_folder = "/Users/johannasmriti/Downloads/musicnet/test_data"  
    output_folder = "/Users/johannasmriti/Downloads/musicnet/Denoising_Audio/noise_data_clean_test" 
    split_audio(input_folder, output_folder)
