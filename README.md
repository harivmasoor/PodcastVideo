# Setting Up and Running the PodcastVideo Project
## Prerequisites
- Cursor: Download and install from [cursor.so](https://cursor.so)
- Git: Ensure git is installed on your system
- For Mac Users: Xcode command line tools
- Python 3.9

## Step-by-Step Instructions
1. **Cursor Setup**
   - Open the Cursor app 
   - Open "AI pane" (click the toggle left of the gear icon in the top right)
   - Activate Autosave from Cursor top menu, under ‘File’
2. **Terminal Setup**
   - Open a new Terminal 
3. **For Mac Users: Xcode Installation**
   - Check if Xcode is installed: `xcode-select -p`
   - If not installed or if you get an error, run: `xcode-select --install`
4. **Python 3.9 Installation**
   - For Mac: 
     ```
     brew install python@3.9
     ```
   - For Windows: Download and install from [python.org](https://www.python.org/downloads/release/python-3913/)

5. **Project Setup**
   - Navigate to Documents: `cd ~/Documents`
   - Create Projects folder: 
     ```
     mkdir Projects
     cd Projects
     ```
   - Clone the repository:
     ```
     git clone https://github.com/harivmasoor/PodcastVideo
     cd PodcastVideo
     ```
6. **Cursor Project Opening**
   - In Cursor, choose "Open Folder" from the top menu
   - Navigate to Documents -> Projects -> PodcastVideo
7. **Audio File Setup**
   - Download the NotebookLM output file
   - Save it as "my_resume_podcast.wav" in the PodcastVideo folder
8. **Environment Setup**
   - Create a .env file in the PodcastVideo folder
   - Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Add to .env: `GEMINI_API_KEY=your_api_key_here`
9. **Python Environment Setup**
   - Check Python version: 
```
python3 --version
```
   - If not 3.9.x, add Python 3.9 to PATH:
     ```
     echo 'export PATH="/usr/local/opt/python@3.9/bin:$PATH"' >> ~/.zshrc
     source ~/.zshrc
     ```
   - Verify: 
```
python3.9 --version
```
10. **Virtual Environment Setup**
   - Create: 
```
python3.9 -m venv myproject_env
```
   - Activate: 
```
source myproject_env/bin/activate
```
11. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```
12. **Code Customization**
    - Open transcribe.py
    - Replace ####ADD_YOUR_NAME_HERE#### with your full name
13. **Run the Code**
    ```
    python transcribe.py
    ```
Your transcript will be saved as "My_Podcast_Transcript.txt" in the PodcastVideo directory.

## Troubleshooting
If you encounter any errors:
Copy and paste the command and error message to the AI chat box, it will give you suggestions on how to fix it.

