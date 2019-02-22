#!/usr/bin/python3

#Developer : Hamdy Abou El Anein

from easygui import *
import sys

dict = {"1": "./pictures/a.jpg","2": "./pictures/b.jpg","3": "./pictures/c.jpg",
        "4": "./pictures/d.jpg","5": "./pictures/e.jpg","6": "./pictures/f.jpg",
        "7": "./pictures/g.jpg","8": "./pictures/h.jpg","9": "./pictures/i.jpg",
        "10": "./pictures/j.jpg","11": "./pictures/k.jpg","12": "./pictures/l.jpg",
        "13": "./pictures/m.jpg","14": "./pictures/n.jpg","15": "./pictures/o.jpg",
        "16": "./pictures/p.jpg","17":"./pictures/q.jpg","18": "./pictures/r.jpg",
        "19": "./pictures/s.jpg","20": "./pictures/t.jpg","21": "./pictures/u.jpg",
        "22": "./pictures/v.jpg","23": "./pictures/w.jpg","24": "./pictures/x.jpg",
        "25": "./pictures/y.jpg","26": "./pictures/z.jpg","-57" : "", "137":"./pictures/e.jpg",
        "136": "./pictures/e.jpg", "128": "./pictures/a.jpg", "-64": "","150":"./pictures/o.jpg",
        "132":"./pictures/a.jpg","-51":""}

def entertext():
    text=enterbox(msg="Welcome to the Rosetta Stone Hieroglyphic translator \n\n\n Enter your name in the field below", image = "./pictures/rosetta_stone.jpg", title="Rosetta Stone Hieroglyph translation", default="Your name here")
    if text == None:
        sys.exit(0)
    else:
        text = text.lower()
        output = []
        for character in text:
            number = ord(character) - 96
            output.append(number)
            #print(output)

        for n, i in enumerate(output):
            if i == 1:
                output[n] = dict["1"]
            if i == 2:
                output[n] = dict["2"]
            if i == 3:
                output[n] = dict["3"]
            if i == 4:
                output[n] = dict["4"]
            if i == 5:
                output[n] = dict["5"]
            if i == 6:
                output[n] = dict["6"]
            if i == 7:
                output[n] = dict["7"]
            if i == 8:
                output[n] = dict["8"]
            if i == 9:
                output[n] = dict["9"]
            if i == 10:
                output[n] = dict["10"]
            if i == 11:
                output[n] = dict["11"]
            if i == 12:
                output[n] = dict["12"]
            if i == 13:
                output[n] = dict["13"]
            if i == 14:
                output[n] = dict["14"]
            if i == 15:
                output[n] = dict["15"]
            if i == 16:
                output[n] = dict["16"]
            if i == 17:
                output[n] = dict["17"]
            if i == 18:
                output[n] = dict["18"]
            if i == 19:
                output[n] = dict["19"]
            if i == 20:
                output[n] = dict["20"]
            if i == 21:
                output[n] = dict["21"]
            if i == 22:
                output[n] = dict["22"]
            if i == 23:
                output[n] = dict["23"]
            if i == 24:
                output[n] = dict["24"]
            if i == 25:
                output[n] = dict["25"]
            if i == 26:
                output[n] = dict["26"]
            if i == -57:
                output[n] = dict["-57"]
            if i == 137:
                output[n] = dict["137"]
            if i == 136:
                output[n] = dict["136"]
            if i == 128:
                output[n] = dict["128"]
            if i == -64:
                output[n] = dict["-64"]
            if i == 150:
                output[n] = dict["150"]
            if i == 132:
                output[n] = dict["132"]
            if i == -51:
                output[n] = dict["-51"]

        image = output
        msg = "This is your Hieroglyphic name"
        choices = ["Try another name"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Try another name":
            entertext()
        else:
            sys.exit(0)
entertext()