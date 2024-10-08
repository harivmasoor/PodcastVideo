import google.generativeai as genai
from config import GEMINI_API_KEY, model

genai.configure(api_key=GEMINI_API_KEY)

def transcribe_audio(audio_file_path):
    # Create a more detailed prompt
    prompt = """
    Generate a transcript of the podcast conversation about Hari Masoor.
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

    # Print the transcript
    print("SSML Transcript:")
    print(response.text)

if __name__ == "__main__":
    audio_file_path = "hari.wav"  # Make sure this file exists in your project directory
    transcribe_audio(audio_file_path)
