import google.generativeai as genai
from config import GEMINI_API_KEY, model
import os
genai.configure(api_key=GEMINI_API_KEY)
def transcribe_audio(audio_file_path):
    # Create a more detailed prompt
    prompt = """
    Generate a transcript of the podcast conversation about ####ADD_YOUR_NAME_HERE####.
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
    # Upload the audio file
    audio_file = genai.upload_file(audio_file_path)
    # Generate the transcript
    response = model.generate_content([prompt, audio_file])
    # Save the transcript to a file
    output_file_path = os.path.join(os.path.dirname(__file__), "My_Podcast_Transcript.txt")
    with open(output_file_path, "w") as f:
        f.write("SSML Transcript:\n")
        f.write(response.text)
    print(f"Transcript saved to: {output_file_path}")
if __name__ == "__main__":
    audio_file_path = "my_resume_podcast.wav"  # Make sure this file exists in your project directory
    transcribe_audio(audio_file_path)

