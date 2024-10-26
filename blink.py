import machine,time




# Noty:
    #button1 --> C
    #button2 --> D
    #button3 --> E
    #button4 --> F



klavesa1 = machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)
klavesa2 = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_DOWN)
klavesa3 = machine.Pin(3,machine.Pin.IN,machine.Pin.PULL_DOWN)
klavesa4 = machine.Pin(4,machine.Pin.IN,machine.Pin.PULL_DOWN)

buzzer  = machine.PWM(machine.Pin(5))

notaC = 261
notaD = 294
notaE = 329
notaF = 349
skladba = []
pisen = []

def play_tone(frequency):
    buzzer.freq(frequency)
    buzzer.duty_u16(5000)  
    time.sleep(0.3)
    buzzer.duty_u16(0)

def tisk():
    for i in range(100):
        print(" ")
    
    print("button1 --> C")
    print("button2 --> D")
    print("button3 --> E")
    print("button4 --> F")
    print(" ")
    print("Vaše skladba:")
    print(skladba)

tisk()

while True:    
    
    if (klavesa1.value() == 1) and (klavesa2.value() == 1):
        time.sleep(1)
        for nota in range(len(pisen)):
            play_tone(pisen[nota])
        tisk()
   
    if (klavesa3.value() == 1) and (klavesa4.value() == 1):
        time.sleep(1)
        pisen = []
        skladba = []
        tisk()
    
    if klavesa1.value() == 1:
        play_tone(notaC)
        pisen.append(notaC)
        skladba.append("C")
        tisk()
    
    if klavesa2.value() == 1:
        play_tone(notaD)
        pisen.append(notaD)
        skladba.append("D")
        tisk()
    
    if klavesa3.value() == 1:
        play_tone(notaE)
        pisen.append(notaE)
        skladba.append("E")
        tisk()
        

    if klavesa4.value() == 1:
        play_tone(notaF)
        pisen.append(notaF)
        skladba.append("F")
        tisk()
