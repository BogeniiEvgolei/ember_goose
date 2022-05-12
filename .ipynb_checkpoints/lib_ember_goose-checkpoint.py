import os
import requests


if os.path.isfile('lib_ember_goose.txt')==False: 
    
    r = requests.get('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1gh6i8kJPzvaPc9DuuaiDzN573zjRq7cB')
        
    with open('lib_ember_goose.txt', 'wb') as f:
        f.write(r.content)


with open ('lib_ember_goose.txt') as f:
    LIB_ember_goose = {}    
    for stroke in f:        
        stroke = stroke.replace(':', '').replace(',', ' ').split()
        LIB_ember_goose[stroke[0]] = [float(signal) for signal in stroke[1:]]