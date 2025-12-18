import numpy as np
import streamlit as st
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import freqz
import tempfile

def delay_effect(x, D, a):
    y = np.zeros(len(x) + D)
    y[:len(x)] += x
    y[D:D+len(x)] += a * x
    return y

st.title("Audio Delay Effect (DSP Demo)")

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    x, fs = sf.read(tmp_path)

    if x.ndim > 1:
        x = x.mean(axis=1)

    st.subheader("Original Audio")
    st.audio(uploaded_file)

    D_ms = st.slider("Delay Time (ms)", 10, 1000, 200)
    a = st.slider("Amplitude (gain)", 0.0, 1.0, 0.7)

    D = int((D_ms / 1000) * fs)
    y = delay_effect(x, D, a)

    out_path = "output.wav"
    sf.write(out_path, y, fs)

    st.subheader("Delayed Audio")
    st.audio(out_path)

    with open(out_path, "rb") as f:
        st.download_button("Download output.wav", f, file_name="output.wav")

    with st.expander("More Info (DSP Analysis)"):
        impulse = np.zeros(2000)
        impulse[0] = 1
        h = delay_effect(impulse, D, a)

        fig1, ax1 = plt.subplots()
        ax1.stem(h)
        ax1.set_title("Impulse Response h[n]")
        ax1.set_xlabel("n")
        ax1.set_ylabel("h[n]")
        st.pyplot(fig1)

        b = [1] + [0]*D + [a]
        w, H = freqz(b, [1])

        fig2, ax2 = plt.subplots()
        ax2.plot(w, np.abs(H))
        ax2.set_title("Frequency Response |H(e^{jw})|")
        ax2.set_xlabel("Frequency (rad/sample)")
        ax2.set_ylabel("|H(e^{jw})|")
        ax2.grid(True)
        st.pyplot(fig2)
