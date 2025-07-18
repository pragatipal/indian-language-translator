from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Languages you want to translate into
target_languages = {
    "Hindi": "hi",
    "Marathi": "mr",
    "Bengali": "bn",
    "Odia": "or",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn"
}

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    sentence = data.get("sentence", "")
    translations = {}

    for lang_name, lang_code in target_languages.items():
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(sentence)
            translations[lang_name] = translated
        except Exception as e:
            translations[lang_name] = f"Error: {str(e)}"

    return jsonify(translations)

if __name__ == '__main__':
    app.run(debug=True)
