import streamlit as st
import whisper
import tempfile
import os

st.title("Whisper Audio Transcription Demo")

# File uploader
audio_file = st.file_uploader("Upload an audio file (mp3, wav, m4a, etc.)", type=["mp3", "wav", "m4a"])

if audio_file is not None:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.name)[1]) as tmp_file:
        tmp_file.write(audio_file.read())
        tmp_path = tmp_file.name

    st.audio(tmp_path)  # Optionally, play the audio in the app

    st.write("Transcribing... (this may take a while)")
    model = whisper.load_model("base")  # or "small", "medium", "large"
    result = model.transcribe(tmp_path)
    st.subheader("Transcription")
    st.write(result["text"])

    # Optionally, provide a download button for the transcript
    st.download_button("Download Transcript", result["text"], file_name="transcript.txt")

    # Clean up temp file
    os.remove(tmp_path)
import os
print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())
