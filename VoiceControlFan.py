# This script continuously listens and turns speech to text in command line.  
# The script turns the input into a string varible, and that variable is tested against predefined trigger words
# in if statements

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
# Code modified by Eli Etherton/ Eli the Computer Guy for Silicon Dojo

import azure.cognitiveservices.speech as speechsdk
import requests
import urllib.request

speech_key, service_region = "YOUR_KEY", "REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

trigger_on = "fan on"
trigger_off = "fan off"
trigger_temp = "what is the temperature"

exit_word = "close"

alert_fan_on = "The fan has been turned on"
alert_fan_off = "The fan is now off"
goodbye = "Goodbye.  Thanks for Playing."

while True:
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        text_string = ("Recognized: {}".format(result.text))
        
        if trigger_on in text_string:
            speech_synthesizer.speak_text_async(alert_fan_on).get()
            requests.get("http://[your ip]/iot.php?command=on")

        if trigger_off in text_string:
            speech_synthesizer.speak_text_async(alert_fan_off).get() 
            requests.get("http://[your ip]/iot.php?command=off")

        if trigger_temp in text_string:
            alert = requests.get("http://[your ip]/current_temp.html")
            print(alert.text)
            speech_synthesizer.speak_text_async(alert.text).get() 

        if exit_word in text_string:
            speech_synthesizer.speak_text_async(goodbye).get()
            print("Script Closed")  
            quit()   

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))