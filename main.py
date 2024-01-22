from gtts import gTTS #pip install gTTS

def text_to_speech(text, language, output_file):
    tts = gTTS(text=text, lang=language) #converting the given text to speech with the given language
    tts.save(output_file) #save the audio file

text_to_speech('hello', 'en', 'output_en.mp3')
text_to_speech('salut', 'fr', 'output_fr.mp3')
text_to_speech('hola', 'es', 'output_es.mp3')