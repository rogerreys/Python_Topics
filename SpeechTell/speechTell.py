#you will need the following library 
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize
from ibm_watson import LanguageTranslatorV3

# URL Speech to tell
url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/7fdd5b2b-bb8e-4dd8-a404-cb9afd607789"
# API key
iam_apikey_s2t = "fneVk2U79cVdKEz4hRrpgCCrdm3AEHmDY9OsQ_eCMwrC"
# Language Translator
url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/0903f757-dccc-405d-8791-f43de42d1d63'
apikey_lt='UTfaDxhlUAjeitKkZ12GmpNoVtSC6goXk6n2FaNO_NSg'
version_lt='2018-05-01'

# create a Speech To Text Adapter object 
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)

# path audio
filename='./PolynomialRegressionandPipelines.mp3'
recognized_text=""
with open(filename, "rb") as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    json_normalize(response.result['results'],"alternatives")
    for res in response.result['results'][0]["alternatives"]:
        print(res["transcript"])
    
    recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
# print("\nSpeech:", recognized_text, "\n")




# Translation
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

# he method Returns the language code
# print("languageList: ", json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))
# print(language_translator.list_identifiable_languages().get_result())
translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
# print("\nDictionary: ", translation_response, "\n")

# translation to Spanish
translation = translation_response.get_result()
spanish_translation = translation["translations"][0]["translation"]
print("\ntranlationEn-Es: ", spanish_translation, "\n")

# translation to English
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
english_translation = translation_new["translations"][0]["translation"]
print("\ntranlationEs-En: ", english_translation, "\n")
