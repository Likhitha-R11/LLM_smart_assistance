from googletrans import Translator

def translate_text(text, target_language):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"
