import streamlit as st
import whisper
from tempfile import NamedTemporaryFile

# Initialize Whisper model
model = whisper.load_model("base")

# Set app title
st.set_page_config(
    page_title="Digital Transcriber", 
    layout="wide", 
    page_icon="💬")
st.title("Digital Transcriber")

# Create a UI tabs
tab1, tab2 = st.tabs(["📂 Upload & Transcribe", "🎧 Playback"])

# Tab for uploading and transcribing audio
with tab1:
    st.header("Upload Audio File")
    
    # Upload audio file
    audio_file = st.file_uploader("Choose a file (mp3, wav, m4a)", type=["wav", "mp3", "m4a"])

    # Button to start transcription
    if st.button("Transcribe Audio"):
        if audio_file is not None:
            with st.spinner("Processing audio..."):
                # Save audio file temporarily
                with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                    temp_file.write(audio_file.read())
                    temp_file_path = temp_file.name
                
                # Transcribe audio using Whisper
                transcription = model.transcribe(temp_file_path)
                
            st.success("Transcription Complete!")
            st.markdown("### Transcribed Text:")
            st.write(transcription["text"])
        else:
            st.error("Please upload an audio file before transcribing.")
            
# Tab for audio playback
with tab2:
    st.header("Play Audio")
    
    # Show the uploaded file in the audio player if available
    if audio_file is not None:
        st.audio(audio_file, format="audio/wav")
    else:
        st.warning("Please upload an audio file to play.")
