import speech_recognition
import wikipedia

wikipedia.set_lang("es")

def consulta(query):
	result = wikipedia.summary(query, sentences=2)
	return result
