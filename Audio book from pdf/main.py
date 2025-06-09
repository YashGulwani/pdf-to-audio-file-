import pyttsx3
from PyPDF2 import PdfReader

# Function to convert PDF text to speech and save it as an audio file
def pdf_to_audio(pdf_path, audio_path="output.mp3"):
    reader = PdfReader(pdf_path.strip('"'))  # Remove extra quotation marks
    engine = pyttsx3.init()
    
    full_text = ""
    
    # Extract text from all pages
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    
    # Convert text to speech
    engine.save_to_file(full_text, audio_path)
    engine.runAndWait()
    
    print(f"Audio saved as {audio_path}")

# Get user input for PDF file
pdf_file = input("Enter the path to your PDF file: ").strip('"')  # Remove extra quotes
audio_file = input("Enter the path to save the audio file (default: output.mp3): ") or "output.mp3"

pdf_to_audio(pdf_file, audio_file)