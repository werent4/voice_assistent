from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import subprocess
from voice_bibl import speech_recog



url = 'https://www.google.com/'
driver = webdriver.Chrome(executable_path= 'C:\\Users\\User\\Desktop\\projects\\asistent\\chromedriver.exe')




def weather(url_w):
    driver.get(url= url_w)
    time.sleep(10)
def another(url_an):
    driver.get(url= url_an)
    try:
        driver.find_element(by= By.ID, value= 'L2AGLb').click()
    except Exception as e:
        print(e)
        pass
    time.sleep(10)
def main(url,command):
    #
    try:
        driver.get(url= url)
        try:
            driver.find_element(by= By.ID, value= 'L2AGLb').click() #accept cookie
            if command== 'погода':
                weather(url_w= url+'search?q=погода&rlz=1C1CHZN_ruUA978UA978&oq=gjuj&aqs=chrome.1.69i57j0i1i10i512l7j0i10i512j0i1i10i512.2170j0j4&sourceid=chrome&ie=UTF-8')
            elif command== 'Другое':
                another(url_an= 'https://www.google.ru/search?q='+ asistent.recognizer())
        except Exception as e:
            print(e)
            pass

        #if command== 'погода':
        #    weather(url_w= url+'search?q=погода&rlz=1C1CHZN_ruUA978UA978&oq=gjuj&aqs=chrome.1.69i57j0i1i10i512l7j0i10i512j0i1i10i512.2170j0j4&sourceid=chrome&ie=UTF-8')
        #elif command== 'Другое':
        #    another(url_an= 'https://www.google.ru/search?q='+ asistent.recognizer())
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()

asistent = speech_recog()
asistent.recognizer()

if asistent.recognizer() == 'погода':
    print(asistent.recognizer())
    main(url=url, command= 'погода')
elif asistent.recognizer() == 'Открой Telegram':
    subprocess.call('C:\\Users\\User\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')
else:
    print(asistent.recognizer())
    main(url=url, command= 'Другое')
