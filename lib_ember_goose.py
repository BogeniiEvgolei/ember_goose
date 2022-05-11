with open ('lib_ember_goose.txt') as f:
    LIB_ember_goose = {}    
    for stroke in f:        
        stroke = stroke.replace(':', '').replace(',', ' ').split()
        LIB_ember_goose[stroke[0]] = [float(signal) for signal in stroke[1:]]