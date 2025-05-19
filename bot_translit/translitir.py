from deep_translator import GoogleTranslator

def translate_text(tex, yas):
    print(f'{tex} {yas}')
    trans = GoogleTranslator(source='auto', target=yas)
    resulr = trans.translate(tex)
    print(resulr)
    return resulr

