import pyautogui
import keyboard

def capturar_posicao():
    while True:
        if keyboard.is_pressed('enter'):
            x, y = pyautogui.position()
            print(f'Posição X: {x}, Y: {y}')




            keyboard.wait('enter')

capturar_posicao()




