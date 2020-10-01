import speech_recognition as sr

r = sr.Recognizer()
file = sr.AudioFile('speechrecognition/audio.wav')

with file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language='pt')

print(result)
