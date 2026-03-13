# Aliyun ASR Demo for Voice-to-Claude-Code
# This script demonstrates how to use Aliyun ASR (DashScope) for speech-to-text.

import os
import dashscope
from dashscope.audio.asr import Recognition

# Set your Aliyun DashScope API Key
# dashscope.api_key = 'YOUR_API_KEY'

def transcribe_audio(file_path):
    """
    Transcribes local audio file using Aliyun Paraformer model.
    """
    recognition = Recognition(model='paraformer-v1',
                              format='wav',
                              sample_rate=16000,
                              callback=None)
    
    result = recognition.call(file_path)
    
    if result.status_code == 200:
        # Extract transcribed text
        text = result.output['sentence'][0]['text']
        return text
    else:
        print(f"Error: {result.message}")
        return None

if __name__ == "__main__":
    # Example usage:
    # text = transcribe_audio('input.wav')
    # print(f"Transcribed Text: {text}")
    print("This is a demo script for Aliyun ASR integration.")
