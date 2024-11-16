### AI-Based Voice Penetration Testing Assistant

#### Introduction
This AI-based voice assistant helps users conduct basic penetration testing on their home networks through voice commands. Users can instruct the assistant to run reconnaissance, port scans, and vulnerability assessments. The tool uses Nmap to conduct network testing and a combination of voice recognition and synthesis to provide a voice-controlled user experience.

#### Features
- **Voice Command Recognition**: Uses Google Speech Recognition to understand user commands for network testing.
- **Reconnaissance Scans**: Performs network reconnaissance to identify active hosts.
- **Port Scanning**: Scans specified IP addresses for open ports (1-1024).
- **Vulnerability Scanning**: Runs basic vulnerability tests using Nmap scripts.
- **Logging**: Logs all network scanning activities and voice interactions.

#### Usage Instructions
1. **Setup Dependencies**: Install necessary Python packages using `pip`.
    ```sh
    pip install speechrecognition pyttsx3 nmap
    ```
2. **Install Nmap**: Install Nmap on your system (`sudo apt-get install nmap` or similar) and ensure it is available in your system's PATH.
3. **Run the Assistant**: Start the penetration testing assistant using the command.
    ```sh
    python ai_pen_testing_assistant.py
    ```
4. **Voice Commands**:
   - "Run reconnaissance scan"
   - "Port scan on [IP address]"
   - "Vulnerability scan on [IP address]"
   - "Exit" to quit the assistant.

#### Prerequisites
- **Python 3.6 or above**: Ensure you have Python installed on your system.
- **Nmap**: Install Nmap for network scanning capabilities.
- **Microphone**: A working microphone is required for voice commands.

#### How It Works
1. **Voice Recognition**: The assistant listens to the user's voice and interprets commands using Google Speech Recognition.
2. **Nmap Integration**: Based on user commands, the assistant runs different Nmap scans (e.g., reconnaissance, port scan, vulnerability scan).
3. **Voice Feedback**: The assistant provides spoken feedback, indicating the status of each command and any discovered information.
4. **Logging**: All commands and results are logged in `ai_pen_testing_assistant.log` for auditing and review.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Use `pip install -r requirements.txt` to install all necessary dependencies.
3. **Run the Tool**: Use `python ai_pen_testing_assistant.py` to start the voice assistant.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This tool is intended for educational purposes only. Users are responsible for ensuring compliance with applicable laws and regulations before using or modifying the assistant for penetration testing.
