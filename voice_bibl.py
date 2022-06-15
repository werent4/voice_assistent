import speech_recognition as sr

class speech_recog():
    """speech_recognition"""

    def __init__(self):
        self.mic = sr.Microphone()
        self.r = sr.Recognizer()

    def __version__(self):
        version = '1.0'
        return version


    def recognizer(self):

        with self.mic as audio_file:
            print('Скажи что то..')

            self.r.adjust_for_ambient_noise(audio_file)
            audio_input= self.r.listen(audio_file)


            print('Перевожу слова в текст')

            try:
                return self.r.recognize_google(audio_input, language= 'ru-RU')
                print('Выполняю')
                '''if self.audio_output =='погода':
                    print('I will check it for u')
                else:
                    print('repeat pls')'''
            except Exception as e:
                print('Error:' + str(e))

'''test = speech_recog()
test.recognizer()
if test.recognizer() =='погода':
    print('Ok')'''
