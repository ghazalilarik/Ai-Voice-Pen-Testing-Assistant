import speech_recognition as sr
import pyttsx3
import nmap
import logging
import os

# Set up logging
logging.basicConfig(filename='ai_pen_testing_assistant.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Setup text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Initialize Nmap scanner
nm = nmap.PortScanner()

# Voice-based Penetration Testing Assistant
class VoicePenTestAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_command(self):
        with sr.Microphone() as source:
            engine.say("Listening for your command. Please speak clearly.")
            engine.runAndWait()
            print("Listening for your command...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                logging.info(f"User command: {command}")
                return command.lower()
            except sr.UnknownValueError:
                engine.say("Sorry, I did not understand that. Could you please repeat?")
                engine.runAndWait()
                return None
            except sr.RequestError:
                engine.say("Network error. Please check your connection.")
                engine.runAndWait()
                return None

    def execute_command(self, command):
        if "reconnaissance" in command or "scan network" in command:
            self.run_reconnaissance()
        elif "port scan" in command:
            target_ip = self.extract_target_ip(command)
            if target_ip:
                self.run_port_scan(target_ip)
            else:
                engine.say("Please specify a target IP address.")
                engine.runAndWait()
        elif "vulnerability scan" in command:
            target_ip = self.extract_target_ip(command)
            if target_ip:
                self.run_vulnerability_scan(target_ip)
            else:
                engine.say("Please specify a target IP address.")
                engine.runAndWait()
        else:
            engine.say("Command not recognized. Please try something like reconnaissance, port scan, or vulnerability scan.")
            engine.runAndWait()

    def extract_target_ip(self, command):
        words = command.split()
        for word in words:
            if self.is_valid_ip(word):
                return word
        return None

    @staticmethod
    def is_valid_ip(ip):
        parts = ip.split('.')
        if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
            return True
        return False

    def run_reconnaissance(self):
        engine.say("Running network reconnaissance. Please wait.")
        engine.runAndWait()
        logging.info("Running network reconnaissance")
        nm.scan(hosts='192.168.1.0/24', arguments='-sn')
        for host in nm.all_hosts():
            if 'mac' in nm[host]['addresses']:
                logging.info(f"Host: {host}, MAC Address: {nm[host]['addresses']['mac']}")
                print(f"Host: {host}, MAC Address: {nm[host]['addresses']['mac']}")
        engine.say("Network reconnaissance complete. Please check the log file for details.")
        engine.runAndWait()

    def run_port_scan(self, target_ip):
        engine.say(f"Running port scan on {target_ip}. Please wait.")
        engine.runAndWait()
        logging.info(f"Running port scan on IP: {target_ip}")
        nm.scan(target_ip, arguments='-p 1-1024')
        for port in nm[target_ip]['tcp']:
            logging.info(f"Port {port}: {nm[target_ip]['tcp'][port]['state']}")
            print(f"Port {port}: {nm[target_ip]['tcp'][port]['state']}")
        engine.say("Port scan complete. Please check the log file for details.")
        engine.runAndWait()

    def run_vulnerability_scan(self, target_ip):
        engine.say(f"Running vulnerability scan on {target_ip}. Please wait.")
        engine.runAndWait()
        logging.info(f"Running vulnerability scan on IP: {target_ip}")
        nm.scan(target_ip, arguments='-sV --script vuln')
        for port in nm[target_ip]['tcp']:
            if 'script' in nm[target_ip]['tcp'][port]:
                logging.info(f"Vulnerabilities on port {port}: {nm[target_ip]['tcp'][port]['script']}")
                print(f"Vulnerabilities on port {port}: {nm[target_ip]['tcp'][port]['script']}")
        engine.say("Vulnerability scan complete. Please check the log file for details.")
        engine.runAndWait()

if __name__ == "__main__":
    assistant = VoicePenTestAssistant()
    engine.say("Welcome to the Voice Penetration Testing Assistant.")
    engine.runAndWait()
    while True:
        command = assistant.listen_command()
        if command:
            if "exit" in command or "quit" in command:
                engine.say("Goodbye. Stay safe!")
                engine.runAndWait()
                break
            assistant.execute_command(command)
