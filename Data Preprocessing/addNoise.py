import os
import numpy as np
from pydub import AudioSegment

def add_noise_to_data(data):
    RMS = np.sqrt(np.mean(np.abs(data**2)))  
    noise = np.random.normal(0, RMS, data.shape)  
    data_noisy = data + noise
    return data_noisy

clean_folder = '/Users/johannasmriti/Downloads/musicnet/Denoising_Audio/noise_data_clean' 
noisy_folder = '/Users/johannasmriti/Downloads/musicnet/Denoising_Audio/noise_data_noisy1'  
if not os.path.exists(noisy_folder):
    os.makedirs(noisy_folder)

for filename in os.listdir(clean_folder):
    if filename.endswith((".wav", ".mp3", ".flac")): 
        clean_file_path = os.path.join(clean_folder, filename)
        
        audio = AudioSegment.from_file(clean_file_path)
        
        data = np.array(audio.set_channels(1).get_array_of_samples(), dtype=np.float32)
        
        data_noisy = add_noise_to_data(data)
        
        data_noisy = np.clip(data_noisy, -32768, 32767).astype(np.int16)  
        
        noisy_file_path = os.path.join(noisy_folder, filename)
        
        noisy_audio = AudioSegment(
            data_noisy.tobytes(), 
            frame_rate=audio.frame_rate, 
            sample_width=audio.sample_width, 
            channels=1
        )
        noisy_audio.export(noisy_file_path, format="wav")
        
        print(f'Noisy file saved: {noisy_file_path}')
