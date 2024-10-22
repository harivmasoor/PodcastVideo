# Podcast Transcription with SSML

This project transcribes audio files (specifically podcasts) into SSML-formatted text using Google's Gemini AI. The transcription identifies speakers and formats the output for use with text-to-speech systems like Eleven Labs.

## Prerequisites

- Python 3.9
- A Google Cloud account with access to the Gemini API
- An audio file to transcribe (e.g., "my_resume_podcast.wav")

## Installation

1. Clone this repository:
   ```
   git clone [your-repo-url]
   cd [your-repo-name]
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Place your audio file (e.g., "hari.wav") in the project directory.

2. Run the transcription script:
   ```
   python transcribe.py
   ```

3. The SSML-formatted transcript will be printed to the console.

## Files

- `transcribe.py`: Main script for audio transcription
- `config.py`: Configuration file for API key and model setup
- `requirements.txt`: List of Python package dependencies

## Notes

- The transcription accuracy depends on the Gemini model and audio quality.
- You may need to adjust the SSML format based on your specific text-to-speech API requirements.

## License

[Your chosen license]
