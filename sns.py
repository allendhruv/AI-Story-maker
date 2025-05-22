from dotenv import load_dotenv
from datetime import datetime
import os
# Import namespaces
# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def sns_initialize():
    try:
        global speech_config,text_analytics_client

        # Get Configuration Settings
        load_dotenv()
        ai_key_speech = os.getenv('SPEECH_KEY')
        ai_region_speech = os.getenv('SPEECH_REGION')
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key_speech, ai_region_speech)

        text_analytics_client = TextAnalyticsClient(ai_endpoint, AzureKeyCredential(ai_key))
        # print('Ready to use speech service in:', speech_config.region)
        # content = listen()
        # say(sentiment(content))
        # intro="Starting the game"
        # say(intro)

    except Exception as ex:
        print(ex)

def sentiment(content):
    cont=[content]
    sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=cont)[0]
    print("\nSentiment: {}".format(sentimentAnalysis.sentiment))
    txt= sentimentAnalysis.sentiment
    return txt
def listen(ques=None,player="Player"):
    command = ''
    # Configure speech recognition
    # speech_config.set_property(speech_sdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "5000")
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    if(ques!=None):
        say(ques)
    print('Speak now...'+" : ",end="")
    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        # say("times up! ")
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command

def say(t):
    # now = datetime.now()
    # response_text = t
    # print("Siddhi :"+t)
    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-LibbyNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(t).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    # print(t)

# if __name__ == "__main__":
# #     main()
# initialize()
# # # say(sentiment(listen(" hello james  how are you")))
# response=listen("what is your name ?")
# res = listen("hello! "+response+" give me a sentence, to detect sentiment.")
# say("The sentiment is "+ sentiment(res))