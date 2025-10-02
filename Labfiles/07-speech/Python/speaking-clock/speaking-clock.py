import os

from dotenv import load_dotenv
from datetime import datetime
from traceback import format_exc


# Import namespaces
from azure.core.credentials import AzureKeyCredential
import azure.cognitiveservices.speech as speech_sdk

def main():

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    try:
        global speech_config

        # Get config settings
        load_dotenv()
        speech_key = os.getenv('KEY')
        speech_region = os.getenv('REGION')

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(speech_key, speech_region)
        print("Ready to use speech service in: ", speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception:
        print(format_exc())

def TranscribeCommand():
    command = ''

    # Configure speech recognition


    # Process speech input


    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)


    # Configure speech synthesis
    

    # Synthesize spoken output


    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()
