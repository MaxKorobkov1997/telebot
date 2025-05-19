from deep_translator import GoogleTranslator

trans = GoogleTranslator(source = 'auto', target = 'en')
resulr = trans.translate('дом')
print(resulr)