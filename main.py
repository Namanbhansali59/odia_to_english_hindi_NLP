from translate import Translator

def translate_odia_to_english(input_text):
    translator = Translator(to_lang="en", from_lang="or")
    translated_text = translator.translate(input_text)
    return translated_text

def translate_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()

    translated_text = translate_odia_to_english(input_text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated_text)

# Replace these paths with your actual file paths
input_file_path = "input.txt"
output_file_path = "output.txt"

translate_file(input_file_path, output_file_path)
print("Translation complete. Translated text saved to", output_file_path)
