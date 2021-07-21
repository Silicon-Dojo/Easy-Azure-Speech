# This script continuously listens and turns speech to text in command line.  
# The script turns the input into a string varible, and that variable is tested against predefined trigger words
# in if statements

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
# Code modified by Eli Etherton/ Eli the Computer Guy for Silicon Dojo

import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "YOUR_KEY", "REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

trigger_word = "hipster"
exit_word = "close"

warning = "Play Nice Everyone. This has gone on your permenant record."
goodbye = "Goodbye.  Thanks for Playing."

while True:
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        text_string = ("Recognized: {}".format(result.text))
        if trigger_word in text_string:
            speech_synthesizer.speak_text_async(warning).get()
            print("WARNING")

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