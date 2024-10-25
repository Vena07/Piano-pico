import machine,time

# Ovládání:
    # Pohybujte se pomocí tlačítek, číslo určuje jaký je tlačítko ( 1. === button1)
    # Zmáčknutí všech 4 tlačítek najedou ---> Zpět

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

notaC = (261, 0.1)
notaD = (294, 0.1)
notaE = (329, 0.1)
notaF = (349, 0.1)

def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(5000)  
    time.sleep(duration)
    buzzer.duty_u16(0)

def mezera():
    for i in range(10):
        print(" ")






mezera()

hra = True




while hra == True:
    print("Piano")
    print("Pro ovládání mačkejte tlačítka")
    print("1. Skladby")
    print("2. Free Play")
    print("3. Konec")
    vybrano = True
    
    
    while vybrano == True:
        if klavesa1.value() == 1:
            mezera()
            print("1. Hot Cross Buns")
            print("2. Mary Had a Little Lamb")
            print("3. Happy Tune")
            print("4. Simple Dance")
            
        
        
        
        if klavesa2.value() == 1:
            mezera()
            print("Zde si hraj jak chceš")
            while konec == True:
                if klavesa1.value() == 1:
                    play_tone(notaC[0],notaC[1])
    
                if klavesa2.value() == 1:
                    play_tone(notaD[0],notaD[1])
                    
                if klavesa3.value() == 1:
                    play_tone(notaE[0],notaE[1])
                    
                if klavesa4.value() == 1:
                    play_tone(notaF[0],notaF[1])

                if (klavesa1.value() == 1) and (klavesa2.value() == 1) and (klavesa3.value() == 1) and (klavesa4.value() == 1):
                    konec = False
            konec

        if klavesa3.value() == 1:
            hra = False
            mezera()
            print("KONEC")    