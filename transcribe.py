import os
from config import GEMINI_API_KEY, model
import google.generativeai as genai

print("Script started")

genai.configure(api_key=GEMINI_API_KEY)

def transcribe_audio(audio_file_path):
      # Create a more detailed prompt
    prompt = """
    Generate a transcript of the podcast conversation about Sara Zare.
    Identify the speakers as 'Man' and 'Woman', and format the transcript in SSML as follows:
    
    <speak>
    <voice name="Man">
    [Man's dialogue]
    </voice>
    <voice name="Woman">
    [Woman's dialogue]
    </voice>
    </speak>
    
    Please ensure accurate speaker attribution and maintain the flow of the conversation.
    Wrap each speaker's entire dialogue in the appropriate voice tags.
    """
    print(f"Attempting to transcribe file: {audio_file_path}")
    
    if not os.path.exists(audio_file_path):
        print(f"Error: The file '{audio_file_path}' does not exist.")
        return

    try:
        print("Uploading file...")
        audio_file = genai.upload_file(audio_file_path)
        print("File uploaded successfully")
        
        print("Starting transcription...")
        result = model.generate_content([prompt, audio_file])
        print("Transcription completed")
        
        print("Transcription result:")
        print(result.text)
        
        # Save the transcription to a file
        output_file_path = "transcription_output.txt"
        with open(output_file_path, "w") as f:
            f.write(result.text)
        print(f"Transcription saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

# Update this line to use the correct path to your audio file
audio_file_path = "my_resume_podcast.wav"

print(f"Current working directory: {os.getcwd()}")
print(f"Full path of audio file: {os.path.abspath(audio_file_path)}")

# Call the function with the correct file path
transcribe_audio(audio_file_path)

print("Script completed")
