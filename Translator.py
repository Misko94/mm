from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('test1.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileExistsError as e:
    print('check your path silly!')
