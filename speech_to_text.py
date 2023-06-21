import os
import pyttsx3
import speech_recognition as sr
import openai
import textwrap
openai.api_key = "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"
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Speed in wpm
engine.setProperty('volume', 1) # Volume (0-1)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # Volume (0-1)

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    
        return text
    except sr.UnknownValueError:
        return "Pardon me but I could not recognize your speech."
    except sr.RequestError as e:
        return "Pardon me but I am currently facing problem in detecting your language due to server error at our end. I apologize for this."

# history=[]
chat=""
def generate_response(question):
    global chat
    chat+=question+'\n'
    prompt = question+"\n"
    # history.append({'role':'user',"content":prompt})
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=chat,
        max_tokens=1000,
        temperature=0.7,
        # messages=history
    )
    
    reply = response.choices[0].text.strip()
    # history.append({'role':'assistant',"content":reply})
    
    return reply

os.system('cls')

print("""
         Welcome to the ChatBot - JARVIS . This ChatBot is like a physical manifestation of Chat GPT 
         powered by the formidable GPT -3 model. It can help you to write codes , emails and answer 
         questions in a conversational domain like any other Language Model. 
         Hope you have an enjoyable experience.\n""")

r="What can i do for you"
print (r)
engine.say(r)
engine.runAndWait()

while(True):
    text=recognize_speech()
    if text=="Pardon me but I could not recognize your speech.":
        continue
    elif text=="Pardon me but I am currently facing problem in detecting your language due to server error at our end. I apologize for this.":
        continue
    print("\033[4mResponse detected\033[0m: ", (str(text[0])).upper(),text[1:],sep="")
    user_question = text
    response= generate_response(user_question)
    print("\033[4mResponse generated\033[0m: ",end="")
    wrapped_text = textwrap.wrap(response)
    for line in wrapped_text:
        print(line,end="")
    print()
    ### text to speech..
    engine.say(response)
    engine.runAndWait()