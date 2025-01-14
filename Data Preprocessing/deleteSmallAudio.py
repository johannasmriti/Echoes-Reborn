import os
from pydub import AudioSegment

def delete_short_wav_files(folder_path, min_duration=5000):
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            file_path = os.path.join(folder_path, filename)
            
            try:
                audio = AudioSegment.from_file(file_path)
                duration = len(audio)  
                
                if duration < min_duration:
                    print(f"Deleting {filename} ({duration / 1000} seconds)")
                    os.remove(file_path)
            except Exception as e:
                print(f"Could not process {filename}: {e}")

if __name__ == "__main__":
    folder_path = "/Users/johannasmriti/Downloads/musicnet/data_with_gaps"
    
    delete_short_wav_files(folder_path)
