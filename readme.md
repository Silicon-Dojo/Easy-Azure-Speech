# “Easy” Computer Speech Recognition with Azure Cognitive Services and Python

Azure Cognitive Speech Services allow you to easily add speech services to your device or app with an API call. In this class I show how to use Python, but many languages can be used, and different languages have the ability to access different resources on Azure.

## Prerequisites
This article assumes:

- You have an Azure account and Speech service subscription. If you don't have and account and subscription -- [Try the Speech service for free](https://azure.microsoft.com/en-us/free/cognitive-services/)

- You have [Python](https://www.python.org/downloads/) installed.

## Setup

Open a terminal and use [pip](https://pip.pypa.io/en/stable/) to install Azure Voice SDK.

```bash
pip install azure-cognitiveservices-speech
```

## Usage
After downloading the git repository, replace the keys with your own.

```python
speech_key, service_region = "YOUR_KEY", "REGION"
```
After you can use this command in your terminal to launch the program.
```bash
./ContinuousSpeechRecognition.py
```

## Contributing
Too learn more about this project and more. Visit [Silicon Dojo](https://www.SiliconDojo.com/).
