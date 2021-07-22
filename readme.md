# “Easy” Computer Speech Recognition with Azure Cognitive Services and Python

Azure Cognitive Speech Services allow you to easily add speech services to your device or app with an API call. In this class I show how to use Python, but many languages can be used, and different languages have the ability to access different resources on Azure.

## Azure Cognitive Services

### What is Azure Cognitive Services?

Cognitive Services brings AI within reach of every developer—without requiring machine learning expertise. All it takes is an API call to embed the ability to see, hear, speak, search, understand, and accelerate decision-making into your apps. Enable developers of all skill levels to easily add AI capabilities to their apps.

### Serverless Architecture

Compute in the cloud Send Cloud Function/ Azure Function file and requirements, get back results in json Azure Speech Services

### Languages and SDK Compatibility

### SSML – Language Style

Speech Synthesis Markup Language (SSML) Speech to Text from Mic

### Continuous Speech

- Add while True: 
- Need to Trigger to Turn On 
- Need Trigger to Turn Off 
### Continuous Speech with Trigger

- Add if state meant and conditional to text variable 
- Capitalization issues with text 

### Control Raspberry Pi with Azure/ Python

### Speech to Text from File

- Can be read out load 
- Can be saved to .wav file to be used by other applications 

### Text to Speech to .wav

## Continuous Speech Recognition Code:
This Python code uses while True: to continuously loop. It also has trigger words so that is someone says “hipster” they get a verbal warning from the script, and if they say “close” the script will exit.
[View Code](https://github.com/Silicon-Dojo/Easy-Azure-Speech/blob/main/ContinuousSpeechRecognition.py)

## Trigger Fan Python Script: 
This script sends commands using GET to a Raspberry Pi based on trigger words. This allows the script to control a fan being turned on or off.

This script also reads the value from a webpage if you use the proper trigger word and tells you the current value on that page.
[View Code](https://github.com/Silicon-Dojo/Easy-Azure-Speech/blob/main/VoiceControlFan.py)