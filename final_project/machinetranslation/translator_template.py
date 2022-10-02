import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


# authenticator = IAMAuthenticator('2I9aADFnLjSQ7FmkURW8l7AgB3LUpTSgaxro4tMECZka')
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4897ecb6-d658-45f8-8b39-a9b9ab10af70')
language_translator.set_service_url(url)

translation = language_translator.translate(
    text='Hello, how are you today? I am Dr. Amul Shinde.',
    model_id='en-de').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))
