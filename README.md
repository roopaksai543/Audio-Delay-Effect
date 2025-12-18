# Audio Delay Effect

An interactive digital signal processing demo that applies a discrete-time delay (echo) to an uploaded audio file.

Users can adjust the delay time and amplitude, listen to the result, and inspect the system’s impulse and frequency responses.

Live Website: [Audio Delay Effect](https://audio-delay-effect-pt3y2klpcw9nflwmia2oty.streamlit.app/#audio-delay-effect-dsp-demo)

## DSP Model

The system implements:

y[n] = x[n] + a · x[n − D]

Where:
- D is the delay (in samples)
- a is the gain applied to the delayed copy

This is a linear time-invariant (LTI) FIR system.

## Features
- Upload a WAV file
- Adjustable delay time (ms)
- Adjustable amplitude (gain)
- Audio playback and download
- Impulse response visualization
- Frequency response magnitude plot

## Live Demo
This app is designed to be deployed on Streamlit Cloud.
