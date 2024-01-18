
import pyautogui
from time import sleep

pyautogui.click(404,862,duration=2)
sleep(2)
pyautogui.hotkey('command', 'n')
sleep(1)
pyautogui.write("https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PF/Emitir/")
pyautogui.press('enter')
sleep(1)

with open('cpfs.txt', 'r') as file:
    for line in file:
        cpf = line
        pyautogui.click(326,693, duration=2)
        pyautogui.write(cpf)
        pyautogui.click(326,693, duration=2)
        pyautogui.click(314,740, duration=2)
        pyautogui.click(327,682, duration=2)