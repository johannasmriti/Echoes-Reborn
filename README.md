# **Echoes Reborn: Audio Restoration Pipeline**

*Echoes Reborn* is an advanced, end-to-end audio restoration pipeline designed to restore and enhance historical recordings. It combines deep learning with LPC (Linear Predictive Coding)-based inpainting techniques to remove noise, fill gaps, and preserve the fidelity of musical details. This pipeline ensures that clean audio remains untouched while seamlessly restoring degraded sections.

---

## **Project Structure**

audioInpainter/ ├── audio_inpainting_model_LPC.ipynb # Notebook for LPC-based audio inpainting ├── lpc_ml.ipynb # Supporting LPC implementation details ├── classifier/ │ ├── class-epoch-8.pth # Pre-trained classifier model weights │ ├── classifier.ipynb # Classifier model usage notebook │ └── classifier_training.ipynb # Notebook for classifier model training ├── denoiser/ │ ├── weights/ │ │ └── autoencoder/ # Directory for autoencoder weights │ ├── cleaned_audio.wav # Example denoised output │ ├── denoisingAudio5sec2.h5 # Pre-trained autoencoder weights │ ├── DenoisingAudioMSEOriginalFinal.ipynb # Denoising process notebook │ ├── denoisingLoader.ipynb # Denoising audio loader │ └── noisy_example.wav # Example noisy audio input ├── pipeline.ipynb # Full pipeline combining classification, denoising, and inpainting └── README.md # Documentation for the project


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

