# Audio Delay Effect 🎛️ 

Audio Delay Effect is a web-based digital signal processing demo that applies a discrete-time delay (echo) effect to uploaded audio files.  

Upload a WAV file, adjust the delay time and amplitude, and immediately hear the processed result, with optional signal analysis available.

Live Demo: [Audio Delay Effect](https://audio-delay-effect-pt3y2klpcw9nflwmia2oty.streamlit.app/#audio-delay-effect-dsp-demo)

## Description

Audio Delay DSP is a browser-based audio processing system designed to demonstrate core digital signal processing concepts through an interactive experience. Rather than only presenting equations or static plots, this project allows users to directly hear and visualize the behavior of a discrete-time delay system.

Users upload a WAV audio file, and the system applies a configurable delay effect based on a user-defined delay time and amplitude (gain). The processed audio can be played back instantly and downloaded for offline use.

For users interested in the theory, an expandable **More Info** section provides visualizations of the system’s impulse response and frequency response, directly connecting the mathematical model to its audible effect. This project emphasizes clarity, intuition, and real-world DSP understanding.

## Usage Instructions

1. Open the Audio Delay DSP web app  
2. Upload a WAV audio file  
3. Adjust the delay time (in milliseconds)  
4. Adjust the delay amplitude (gain)  
5. Listen to the delayed audio output  
6. Download the processed audio file if desired  
7. (Optional) Expand "More Info" to view:
   - Impulse response of the delay system  
   - Frequency response magnitude  

## DSP Model

The system implements the following discrete-time model:

y[n] = x[n] + a · x[n − D]
   - D is the delay in samples  
   - a is the amplitude (gain) applied to the delayed signal  

This system is a linear time-invariant (LTI) finite impulse response (FIR) filter. The impulse and frequency response plots are generated directly from this formulation.

## Developer Notes

This project is built entirely in Python and deployed as a cloud-hosted web application using Streamlit. Audio processing and DSP analysis are handled server-side using NumPy, SciPy, and SoundFile. The interface enables real-time parameter control, audio playback, and optional visualization of underlying DSP characteristics directly in the browser.

The repository is designed to be fully self-contained and deployable directly from GitHub without requiring any local setup.

Built by **Roopaksai Sivakumar**  
Computer Engineering @ UC Irvine
