""" Translator """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """ English to French Translator"""
    #write the code here
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    # french_text = json.dumps(translation, indent=2, ensure_ascii=False)
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ French TO English Translator """
    #write the code here
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    # english_text = json.dumps(translation, indent=2, ensure_ascii=False)
    english_text = translation['translations'][0]['translation']
    return english_text

# print("\n========== English to French ===============\n")
# TEXT = 'Hello, how are you today? I am Dr. Amul Shinde.'
# print(TEXT)
# print(english_to_french(TEXT))

# print("\n========== French to English ===============\n")
# TEXT = 'Bonjour, comment vous êtes aujourd\'hui? Je suis le Dr Amul Shinde.'
# print(TEXT)
# print(french_to_english(TEXT))
# print("\n========== ***************** ===============\n")
