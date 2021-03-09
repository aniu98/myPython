from pynput import keyboard
import time
exitFlag=False
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    global exitFlag
    print('{0} released {1}'.format(key,exitFlag))
    if key == keyboard.Key.esc:
        exitFlag = Trueqd
        # print("change the flag %s"%exitFlag)
        return False


# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
print("sss")
while True:
    if exitFlag:
        print('aaaa')
        break
    print(exitFlag)
    time.sleep(1)

print("eeee")
