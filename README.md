# **Echoes Reborn: A Comprehensive Pipeline for Historic Piano Audio Restoration**

*Echoes Reborn* is an advanced, end-to-end audio restoration pipeline designed to restore and enhance historical recordings. It combines deep learning with LPC (Linear Predictive Coding)-based inpainting techniques to remove noise, fill gaps, and preserve the fidelity of musical details. This pipeline ensures that clean audio remains untouched while seamlessly restoring degraded sections.
For a detailed report on the methodology, results, and performance of this restoration pipeline, please refer to the [Echoes Reborn Restoration Report](https://github.com/johannasmriti/Echoes-Reborn/blob/main/Report/NuerIPS_Echoes_Reborn.pdf).

---

## **Project Structure**

```plaintext
Echoes-Reborn/
├── audioInpainter/
│   ├── audio_inpainting_model_LPC.ipynb      # Notebook for LPC-based audio inpainting
│   ├── lpc_ml.ipynb                          # Supporting LPC implementation details
│   ├── lpc_arch.png                          # Diagram of the Architecture of the Audio Inpainter
├── classifier/
│   ├── class-epoch-8.pth                     # Pre-trained classifier model weights
│   ├── classifier.ipynb                      # Classifier model usage notebook
│   └── classifier_training.ipynb             # Notebook for classifier model training
│   └── spectrogram_classifier.png            # Diagram of the Architecture of the Classifier
├── denoiser/
│   ├── weights/
│   │   └── autoencoder/                      # Directory for autoencoder weights
│   ├── cleaned_audio.wav                     # Example denoised output
│   ├── denoisingAudio5sec2.h5                # Pre-trained autoencoder weights
│   ├── DenoisingAudioMSEOriginalFinal.ipynb  # Denoising process notebook
│   ├── denoisingLoader.ipynb                 # Denoising audio loader
│   └── noisy_example.wav                     # Example noisy audio input
│   └── audio_denoiser.png                    # Diagram of the Architecture of the Denoiser
├── pipeline.ipynb                            # Full pipeline combining classification, denoising, and inpainting
├── pipelineArchitechture.png                 # Pipeleine Architecture - Workflow Diagram
├── Data Preprocessing                        # Directory for dataPreprocessing done for throughout the project
│   ├── addNoise.py                           # Adds noise to a given audio folder with .wav files
│   ├── addSilentGap.py                       # Adds a silent gap in the audio (for inpainting)
│   ├── deleteSmallAudio.py                   # Deltes scmall audios less than 5secs to ensure consistency in the dataset
│   ├── denoiseTriming.py                     # Trims all audio in the files to be 5 seconds
└── README.md
```

---

## **Pipeline Overview**

The pipeline consists of the following components:

1. **Audio Classification**  
   - Identifies whether input audio is `Noisy` or `Clean` using a CNN-based classifier.
   - Input: Mel spectrogram of the audio.
   - Output: Classification label (`Noisy` or `Clean`).

2. **Denoising**  
   - Applies an autoencoder to remove noise from audio classified as `Noisy`.
   - Preserves the integrity of `Clean` audio by bypassing the denoising step.

3. **Audio Inpainting**  
   - Detects and fills silent gaps in the audio using LPC-based techniques.
   - Ensures smooth transitions and restores missing content without artifacts.

4. **Visualization**  
   - Displays waveforms and spectrograms of both the original and processed audio for comparison.

---

## **Installation**

To set up the project, ensure the following dependencies are installed:

```bash
pip install torch torchaudio tensorflow librosa matplotlib soundfile opencv-python scipy spectrum
```

---

## **Usage**
### **Run the Full Pipeline**
   
Use the pipeline.ipynb notebook to process audio through all pipeline stages:
   - Input: Path to an audio file.
   - Output: Restored audio with noise removed and gaps filled.
     
**Steps:**
   1. Open the pipeline.ipynb file.
   2. Configure the paths for:
      - Classifier weights (classifier/class-epoch-8.pth).
      - Autoencoder weights (denoiser/weights/autoencoder/denoisingAudio5sec2.h5).
      - Input audio file.
   3. Execute the cells sequentially.

      
### **Individual Modules**

Run specific modules independently for targeted tasks:

   - Audio Classification: Use classifier/classifier.ipynb to classify input audio.
   - Denoising: Use denoiser/denoisingLoader.ipynb for noise removal.
   - Audio Inpainting: Use audio-inpainter/audio_inpainting_model_LPC.ipynb to fill gaps in degraded audio.
     

