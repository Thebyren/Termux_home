import subprocess
from os import system
hola =input("escribe lo que quieras: ")
variable = "echo "+str(hola)+" | "+" termux-tts-speak"
def  speak():
    print(variable)
    subprocess.call(variable,shell=True)
speak()
