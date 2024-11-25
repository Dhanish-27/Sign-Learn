from googletrans import Translator

name="பூனை"
lang="en"



translator=Translator()
translation = translator.translate(name, dest=lang)
translated= translation.text
print(translated)