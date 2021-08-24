banner = '''
  _____ _______ _____  _      
 / ____|__   __|  __ \| |     
| |       | |  | |__) | |     
| |       | |  |  _  /| |     
| |____   | |  | | \ \| |____ 
 \_____|  |_|  |_|  \_\______|       
WhatsApp, Telegram and more bomber, v1.0
Разработчик: Orlov German
Сайт проекта: https://github.com/Gerbl444/ctrl.git
'''
import pyautogui 
import time 
import pyperclip

print(banner)
message = input("Что отправляем? ")
number = int(input("Сколько сообщений отправить? (0 - бесконечно)"))
pyperclip.copy(message)
count = 0


print("У Вас есть 10 секунд, чтобы перевестись на нужное окно!")
time.sleep(1)
print("9...")
time.sleep(1)
print("8...")
time.sleep(1)
print("7...")
time.sleep(1)
print("6...")
time.sleep(1)
print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("attack!")


if number == 0:
	while True:
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press('enter')
		count = count + 1
		print("Сообщений отправлено: " + str(count))
else:
	while number != 0:
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press('enter')
		number = number - 1	
		count = count + 1
		print("Сообщений отправлено: " + str(count))

