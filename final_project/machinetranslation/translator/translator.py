"""Translator

Translate text from French to English and vice versa using IBM Watson.

"""

# import json
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

def englishToFrench(english_text=None):
    """
    Given English text, translate to French and return
    """

    if english_text is None or english_text == "":
        return None

    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr',
    ).get_result()

    french_text = french_text.get('translations', None)[0].get('translation', None)

    return french_text

def frenchToEnglish(french_text=None):
    """
    Given French text, translate to English and return
    """

    if french_text is None or french_text == "":
        return None

    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en',
    ).get_result()

    english_text = english_text.get('translations', None)[0].get('translation', None)
    
    return english_text 
