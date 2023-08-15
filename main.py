import tkinter as tk
from tkinter import filedialog
from translate import Translator

def translate_text(input_text, from_lang, to_lang):
    translator = Translator(to_lang=to_lang, from_lang=from_lang)
    translated_text = translator.translate(input_text)
    return translated_text

def translate_and_save(input_file, output_file, from_lang, to_lang):
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()

    translated_text = translate_text(input_text, from_lang, to_lang)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated_text)

def open_file_dialog():
    global odia_input_path
    odia_input_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    translate_and_save_button["state"] = tk.NORMAL

def translate_files():
    english_output_path = "english_output.txt"
    hindi_output_path = "hindi_output.txt"

    # Translate from Odia to English
    translate_and_save(odia_input_path, english_output_path, "or", "en")
    status_label.config(text="Translation from Odia to English complete.")

    # Translate from English to Hindi
    translate_and_save(english_output_path, hindi_output_path, "en", "hi")
    status_label.config(text="Translation from English to Hindi complete.")

# Create the main window
root = tk.Tk()
root.title("Language Translation")

# Create and place widgets
select_file_button = tk.Button(root, text="Select Input File", command=open_file_dialog)
select_file_button.pack(pady=20)

translate_and_save_button = tk.Button(root, text="Translate and Save", command=translate_files, state=tk.DISABLED)
translate_and_save_button.pack()

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

root.mainloop()
