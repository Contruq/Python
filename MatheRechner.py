import random
# 4/3 * PI * R³
PI = 3.14
global fehler
fehler = 0
global richtig
richtig = 0

##VOLUMEN TASCHENRECHNER

def TRKugel():
    # 4/3 * PI * R³
    KugelR = input("Gib den Radius deiner Kugel an.")
    CalcR3 = float(KugelR) ** 3
    CalculateKgl = 4 * PI * CalcR3 / 3
    print(f"Das Volumen deiner Kugel ist {CalculateKgl}cm³\nBerechnet mit der Formel: V=4/3*π*r³")


def TRKegel():
    # 1/3 * PI * R² * H
    KegelR = input("Gib den Radius deines Kegels an.")
    KegelH = input("Gib die Höhe deines Kegels an.")
    CalcR2 = float(KegelR) ** 2
    CalculateKegl = 1 * PI * CalcR2 * float(KegelH) / 3
    print(f"Das Volumen deines Kegels ist {CalculateKegl}cm³\nBerechnet mit der Formel: V=1/3*G*H (G=π*r² ; H=höhe)")


def TRqPyramide():
    # 1/3 * G(a²)*H
    PyramideG1 = input("Gib die a Seite deiner Pyramide an.")
    PyramideG2 = input("Gib die b Seite deiner Pyramide an.")
    PyramideH = input("Gib die höhe deiner Quadratischen Pyramide an.")
    CalcG2 = float(PyramideG1) * float(PyramideG2)
    CalculateQPyramide = 1 * CalcG2 * float(PyramideH) / 3
    print(
        f"Das Volumen deiner Pyramide ist {CalculateQPyramide}cm³\nBerechnet mit der Formel: V=1/3*G*H (G=a*b ; H=höhe)")


def TRZylinder():
    # PI * R² * H
    ZylinderR = input("Gib den Radius deines Zylinders an")
    ZylinderH = input("Gib die Höhe deines Zylinders an")
    CalcZR = float(ZylinderR) ** 2
    CalculateZylinder = PI * CalcZR * float(ZylinderH)
    print(f"Das Volumen deines Zylinders ist {CalculateZylinder}cm³\nBerechnet mit der Formel: V=G*H (G=π*r² ; H=höhe)")


def TRWürfel():
    # G(a²) * H
    WürfelG = input("Gib die a Seite deines Würfels an")
    CalculateWürfel = float(WürfelG) ** 3
    print(f"Das Volumen deines Würfels ist {CalculateWürfel}cm³\nBerechnet mit der Formel: V=G*H (G=a*a ; H=a)")


def TRQuader():
    # G(a*b) * H
    QuaderG1 = input("Gib die a Seite deines Quaders an")
    QuaderG2 = input("Gib die b Seite deines Quaders an")
    QuaderH = input("Gib die Höhe deines Quaders an")
    CalcQG = float(QuaderG1) * float(QuaderG2)
    CalculateQuader = CalcQG * float(QuaderH)
    print(f"Das Volumen deines Quaders ist {CalculateQuader}cm³\nBerechnet mit der Formel: V=G*H (G=a*b ; H=höhe)")


def TRDreiecksPrisma():
    # G(a*kh:2) * H
    PrismaA = input("Gib die a Seite deines Dreieck-Prismas an")
    PrismaB = input("Gib die b Seite deines Dreieck-Prismas an")
    PrismaH = input("Gib die Höhe deines Prismas an")
    CalcPrismaG = float(PrismaA) * float(PrismaB) / 2
    CalculatePrisma = CalcPrismaG * float(PrismaH)
    print(f"Das Volumen deines Dreiecksprismas ist {CalculatePrisma}cm³\nBerechnet mit der Formel: V=G*H (G=a*b:2 ; H=höhe)")

def TRTrapezPrisma():
    # G(a*kh:2) * H
    TrapezA = input("Gib die 1.Parallere Seite z.B a, an")
    TrapezC = input("Gib die 2.Parallere Seite z.B c, an")
    TrapezH = input("Gib die Höhe des flachen Trapez an")
    PrismaH = input("Gib die Höhe des Prismas(Körper) an")
    CalculateTrapez1 = float(TrapezA) + float(TrapezC)
    CalculateTrapez2 = CalculateTrapez1 * float(TrapezH) / 2
    CalculateTPrisma = CalculateTrapez2 * float(PrismaH)
    print(f"Das Volumen deines Trapezprismas ist {CalculateTPrisma}cm³\nBerechnet mit der Formel: \nTrapez: A = (a+c) * h : 2\nPrisma: V=G*H (G= Trapez ; H=höhe)")

##FORMELN TASCHENRECHNER

def TRQuadrat():
    QuadratA = input("Gib die a Seite deines Quadrats an")
    CalculateQuadrat = float(QuadratA) ** 2
    print(f"Der Flächeninhalt deines Quadrats ist {CalculateQuadrat}cm²\nBerechnet mit der Formel: A = a*a")

def TRRechteck():
    RechteckA = input("Gib die a Seite deines Rechtecks an")
    RechteckB = input("Gib die b Seite deines Rechtecks an")
    CalculateRechteck = float(RechteckA) * float(RechteckB)
    print(f"Der Flächeninhalt deines Rechtecks ist {CalculateRechteck}cm²\nBerechnet mit der Formel: A = a*b")

def TRDreieck():
    DreieckG = input("Gib die g Seite deines Dreiecks an")
    DreieckH = input("Gib die höhe deines Dreieck an")
    CalculateDreieck = float(DreieckG) * float(DreieckH) / 2
    print(f"Der Flächeninhalt deines Dreiecks ist {CalculateDreieck}cm²\nBerechnet mit der Formel: A = g*h : 2")

def TRParallelogramm():
    ParallelogrammG = input("Gib die g Seite deines Parallelogramms an")
    ParallelogrammH = input("Gib die höhe deines Parallelogramms an")
    CalculateParallelogramm = float(ParallelogrammG) * float(ParallelogrammH)
    print(f"Der Flächeninhalt von deinen Parallelogramm ist {CalculateParallelogramm}cm²\nBerechnet mit der Formel: A = g*h : 2")

def TRTrapez():
    TrapezA = input("Gib die 1.Parallere Seite z.B a, an")
    TrapezC = input("Gib die 2.Parallere Seite z.B c, an")
    TrapezH = input("Gib die Höhe des Trapez an")
    CalculateTrapez1 = float(TrapezA) + float(TrapezC)
    CalculateTrapez = CalculateTrapez1 * float(TrapezH) / 2
    print(f"Der Flächeninhalt deines Trapez ist {CalculateTrapez}cm²\nBerechnet mit der Formel: A = (a+c) * h : 2")

def TRKreis():
    KreisR = input("Gib den Radius von deinen Kreis an")
    CalcKR2 = float(KreisR) ** 2
    CalculateKreis = CalcKR2 * PI
    print(f"Der Flächeninhalt von deinen Kreis ist {CalculateKreis}cm²\nBerechnet mit der Formel: A = π*r²")

##AufgabenSteller VOLUMEN

def ASKugel():
    # 4/3 * PI * R³
    KugelR = random.randint(1,100)
    CalcR3 = float(KugelR) ** 3
    CalculateKgl = 4 * PI * CalcR3 / 3
    Antwort = input(f"Gegeben ist eine Kugel mit dem Radius von {KugelR}cm\nBerechne den Volumen der Kugel, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateKgl:
        Chc = input(f"Richtig!\nDie Kugel hat einen Volumen von {CalculateKgl}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASKugel()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDie Kugel hat einen Volumen von {CalculateKgl}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASKugel()
        if Chc == "Nein":
            Check()


def ASKegel():
    # 1/3 * PI * R² * H
    KegelR = random.randint(1,100)
    KegelH = random.randint(1,100)
    CalcR2 = float(KegelR) ** 2
    CalculateKegl = 1 * PI * CalcR2 * float(KegelH) / 3
    Antwort = input(f"Gegeben ist ein Kegel mit dem Radius von {KegelR}cm und eine Höhe von {KegelH}cm\nBerechne den Volumen vom Kegel, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateKegl:
        Chc = input(f"Richtig!\nDer Kegel hat einen Volumen von {CalculateKegl}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASKegel()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDer Kegel hat einen Volumen von {CalculateKegl}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASKegel()
        if Chc == "Nein":
            Check()


def ASqPyramide():
    # 1/3 * G(a²)*H
    PyramideG1 = random.randint(1,100)
    PyramideG2 = random.randint(1,100)
    PyramideH = random.randint(1,200)
    CalcG2 = float(PyramideG1) * float(PyramideG2)
    CalculateQPyramide = 1 * CalcG2 * float(PyramideH) / 3
    Antwort = input(f"Gegeben ist eine Pyramide mit der Seite a {PyramideG2}cm, b {PyramideG2}cm und eine Höhe von {PyramideH}cm\nBerechne den Volumen der Pyramide, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateQPyramide:
        Chc = input(f"Richtig!\nDie Pyramide hat einen Volumen von {CalculateQPyramide}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASqPyramide()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDie Pyramide hat einen Volumen von {CalculateQPyramide}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASqPyramide()
        if Chc == "Nein":
            Check()


def ASZylinder():
    # PI * R² * H
    ZylinderR = random.randint(1,100)
    ZylinderH = random.randint(1,200)
    CalcZR = float(ZylinderR) ** 2
    CalculateZylinder = PI * CalcZR * float(ZylinderH)
    Antwort = input(f"Gegeben ist ein Zylinder mit dem Radius von {ZylinderR}cm und eine Höhe von {ZylinderH}cm\nBerechne den Volumen vom Zylinder, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateZylinder:
        Chc = input(f"Richtig!\nDer Zylinder hat einen Volumen von {CalculateZylinder}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASZylinder()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDer Zylinder hat einen Volumen von {CalculateZylinder}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASZylinder()
        if Chc == "Nein":
            Check()


def ASWürfel():
    # G(a²) * H
    WürfelG = random.randint(1,999)
    CalculateWürfel = float(WürfelG) ** 3
    Antwort = input(f"Gegeben ist ein Würfel mit der Seite a {WürfelG}cm\nBerechne den Volumen vom Würfel, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateWürfel:
        Chc = input(f"Richtig!\nDer Würfel hat einen Volumen von {CalculateWürfel}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASWürfel()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDer Würfel hat einen Volumen von {CalculateWürfel}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASWürfel()
        if Chc == "Nein":
            Check()


def ASQuader():
    # G(a*b) * H
    QuaderG1 = random.randint(1,999)
    QuaderG2 = random.randint(1,999)
    QuaderH = random.randint(1,999)
    CalcQG = float(QuaderG1) * float(QuaderG2)
    CalculateQuader = CalcQG * float(QuaderH)
    Antwort = input(f"Gegeben ist ein Quader mit der Seite a {QuaderG1}cm b, {QuaderG2}cm und eine Höhe von {QuaderH}cm\nBerechne den Volumen vom Quader, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateQuader:
        Chc = input(f"Richtig!\nDer Quader hat einen Volumen von {CalculateQuader}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASQuader()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDer Quader hat einen Volumen von {CalculateQuader}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASQuader()
        if Chc == "Nein":
            Check()


def ASDreiecksPrisma():
    # G(a*kh:2) * H
    PrismaA = random.randint(1,100)
    PrismaB = random.randint(1,100)
    PrismaH = random.randint(1,200)
    CalcPrismaG = float(PrismaA) * float(PrismaB) / 2
    CalculatePrisma = CalcPrismaG * float(PrismaH)
    Antwort = input(f"Gegeben ist ein Dreiecksprisma mit der Seite a {PrismaA}cm b, {PrismaB}cm und eine Höhe von {PrismaH}cm\nBerechne den Volumen vom Dreiecksprisma, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculatePrisma:
        Chc = input(f"Richtig!\nDas Dreiecksprisma hat einen Volumen von {CalculatePrisma}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASDreiecksPrisma()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDas Dreiecksprisma hat einen Volumen von {CalculatePrisma}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASDreiecksPrisma()
        if Chc == "Nein":
            Check()

def ASTrapezPrisma():
    # G(a*kh:2) * H
    TrapezA = random.randint(1,100)
    TrapezC = random.randint(1,100)
    TrapezH = random.randint(1,200)
    PrismaH = random.randint(1,500)
    CalculateTrapez1 = float(TrapezA) + float(TrapezC)
    CalculateTrapez2 = CalculateTrapez1 * float(TrapezH) / 2
    CalculateTPrisma = CalculateTrapez2 * float(PrismaH)
    Antwort = input(f"Gegeben ist ein Trapezprisma mit der Grundfläche: a {TrapezA}cm b, {TrapezC}cm und eine Höhe von {TrapezH}cm, Körperhöhe des Prismas beträgt {PrismaH}cm\nBerechne den Volumen vom Dreiecksprisma, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateTPrisma:
        Chc = input(f"Richtig!\nDer Trapezprisma hat einen Volumen von {CalculateTPrisma}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASTrapezPrisma()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDer Trapezprisma  hat einen Volumen von {CalculateTPrisma}cm³\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASTrapezPrisma()
        if Chc == "Nein":
            Check()

##Aufgabensteller FLÄCHENINHALT

def ASQuadrat():
    QuadratA = random.randint(1,9999)
    CalculateQuadrat = float(QuadratA) ** 2
    Antwort = input(f"Gegeben ist ein Quadrat mit der Seite a {CalculateQuadrat}cm\nBerechne den Flächeninhalt vom Quadrat, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateQuadrat:
        Chc = input(f"Richtig!\nDer Quadrat hat einen Flächeninhalt von {CalculateQuadrat}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASQuadrat()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDer Quadrat hat einen Flächeninhalt von {CalculateQuadrat}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASQuadrat()
        if Chc == "Nein":
            Check()

def ASRechteck():
    RechteckA = random.randint(1,999)
    RechteckB = random.randint(1,999)
    CalculateRechteck = float(RechteckA) * float(RechteckB)
    Antwort = input(f"Gegeben ist ein Rechteck mit der Seite a {RechteckA}cm und b {RechteckB}cm\nBerechne den Flächeninhalt vom Rechteck, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateRechteck:
        Chc = input(f"Richtig!\nDas Rechteck hat einen Flächeninhalt von {CalculateRechteck}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASRechteck()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDas Rechteck hat einen Flächeninhalt von {CalculateRechteck}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASRechteck()
        if Chc == "Nein":
            Check()

def ASDreieck():
    DreieckG = random.randint(1,100)
    DreieckH = random.randint(1,200)
    CalculateDreieck = float(DreieckG) * float(DreieckH) / 2
    Antwort = input(f"Gegeben ist ein Dreieck mit der Grundfläche von {DreieckG}cm und einer Höhe von {DreieckH}cm\nBerechne den Flächeninhalt vom Dreieck, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateDreieck:
        Chc = input(f"Richtig!\nDas Dreieck hat einen Flächeninhalt von {CalculateDreieck}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASDreieck()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDas Dreieck hat einen Flächeninhalt von {CalculateDreieck}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASDreieck()
        if Chc == "Nein":
            Check()

def ASParallelogramm():
    ParallelogrammG = random.randint(1,100)
    ParallelogrammH = random.randint(1,200)
    CalculateParallelogramm = float(ParallelogrammG) * float(ParallelogrammH)
    Antwort = input(f"Gegeben ist ein Parallelogramm mit der Grundfläche von {ParallelogrammG}cm und einer Höhe von {ParallelogrammH}cm\nBerechne den Parallelogramm vom Rechteck, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateParallelogramm:
        Chc = input(f"Richtig!\nDas Parallelogramm hat einen Flächeninhalt von {CalculateParallelogramm}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASParallelogramm()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDas Parallelogramm hat einen Flächeninhalt von {CalculateParallelogramm}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASParallelogramm()
        if Chc == "Nein":
            Check()

def ASTrapez():
    TrapezA = random.randint(1,100)
    TrapezC = random.randint(1,100)
    TrapezH = random.randint(1,200)
    CalculateTrapez1 = float(TrapezA) + float(TrapezC)
    CalculateTrapez = CalculateTrapez1 * float(TrapezH) / 2
    Antwort = input(f"Gegeben ist ein Trapez mit den Seiten a {TrapezA}cm, c {TrapezC}cm und einer Höhe von {TrapezH}\nBerechne den Flächeninhalt vom Trapez, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateTrapez:
        Chc = input(f"Richtig!\nDas Trapez hat einen Flächeninhalt von {CalculateTrapez}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASTrapez()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDas Trapez hat einen Flächeninhalt von {CalculateTrapez}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASTrapez()
        if Chc == "Nein":
            Check()

def ASKreis():
    KreisR = random.randint(1,1337)
    CalcKR2 = float(KreisR) ** 2
    CalculateKreis = CalcKR2 * PI
    Antwort = input(f"Gegeben ist ein Kreis mit einen Radius von {KreisR}cm\nBerechne den Flächeninhalt vom Kreis, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateKreis:
        Chc = input(f"Richtig!\nDas Trapez hat einen Flächeninhalt von {CalculateKreis}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASKreis()
        if Chc == "Nein":
            Check()
    else:
        Chc = input(f"Falsch!\nDas Trapez hat einen Flächeninhalt von {CalculateKreis}cm²\nWiederholung Ja / Nein?")
        if Chc == "Ja":
            ASKreis()
        if Chc == "Nein":
            Check()

##AufgabenSteller VOLUMEN

def ASLKugel():
    # 4/3 * PI * R³
    global fehler
    global richtig
    KugelR = random.randint(1,100)
    CalcR3 = float(KugelR) ** 3
    CalculateKgl = 4 * PI * CalcR3 / 3
    Antwort = input(f"Gegeben ist eine Kugel mit dem Radius von {KugelR}cm\nBerechne den Volumen der Kugel, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateKgl:
        print(f"Richtig!\nDie Kugel hat einen Volumen von {CalculateKgl}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDie Kugel hat einen Volumen von {CalculateKgl}cm³")
        fehler += 1
        return


def ASLKegel():
    # 1/3 * PI * R² * H
    global fehler
    global richtig
    KegelR = random.randint(1,100)
    KegelH = random.randint(1,100)
    CalcR2 = float(KegelR) ** 2
    CalculateKegl = 1 * PI * CalcR2 * float(KegelH) / 3
    Antwort = input(f"Gegeben ist ein Kegel mit dem Radius von {KegelR}cm und eine Höhe von {KegelH}cm\nBerechne den Volumen vom Kegel, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateKegl:
        print(f"Richtig!\nDer Kegel hat einen Volumen von {CalculateKegl}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Kegel hat einen Volumen von {CalculateKegl}cm³")
        fehler += 1
        return
def ASLqPyramide():
    # 1/3 * G(a²)*H
    global fehler
    global richtig
    PyramideG1 = random.randint(1,100)
    PyramideG2 = random.randint(1,100)
    PyramideH = random.randint(1,200)
    CalcG2 = float(PyramideG1) * float(PyramideG2)
    CalculateQPyramide = 1 * CalcG2 * float(PyramideH) / 3
    Antwort = input(f"Gegeben ist eine Pyramide mit der Seite a {PyramideG2}cm, b {PyramideG2}cm und eine Höhe von {PyramideH}cm\nBerechne den Volumen der Pyramide, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateQPyramide:
        print(f"Richtig!\nDie Pyramide hat einen Volumen von {CalculateQPyramide}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDie Pyramide hat einen Volumen von {CalculateQPyramide}cm³")
        fehler += 1
        return


def ASLZylinder():
    # PI * R² * H
    global fehler
    global richtig
    ZylinderR = random.randint(1,100)
    ZylinderH = random.randint(1,200)
    CalcZR = float(ZylinderR) ** 2
    CalculateZylinder = PI * CalcZR * float(ZylinderH)
    Antwort = input(f"Gegeben ist ein Zylinder mit dem Radius von {ZylinderR}cm und eine Höhe von {ZylinderH}cm\nBerechne den Volumen vom Zylinder, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateZylinder:
        print(f"Richtig!\nDer Zylinder hat einen Volumen von {CalculateZylinder}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Zylinder hat einen Volumen von {CalculateZylinder}cm³")
        fehler += 1
        return


def ASLWürfel():
    # G(a²) * H
    global fehler
    global richtig
    WürfelG = random.randint(1,999)
    CalculateWürfel = float(WürfelG) ** 3
    Antwort = input(f"Gegeben ist ein Würfel mit der Seite a {WürfelG}cm\nBerechne den Volumen vom Würfel, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateWürfel:
        print(f"Richtig!\nDer Würfel hat einen Volumen von {CalculateWürfel}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Würfel hat einen Volumen von {CalculateWürfel}cm³")
        fehler += 1
        return

def ASLQuader():
    # G(a*b) * H
    global fehler
    global richtig
    QuaderG1 = random.randint(1,999)
    QuaderG2 = random.randint(1,999)
    QuaderH = random.randint(1,999)
    CalcQG = float(QuaderG1) * float(QuaderG2)
    CalculateQuader = CalcQG * float(QuaderH)
    Antwort = input(f"Gegeben ist ein Quader mit der Seite a {QuaderG1}cm b, {QuaderG2}cm und eine Höhe von {QuaderH}cm\nBerechne den Volumen vom Quader, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateQuader:
        print(f"Richtig!\nDer Quader hat einen Volumen von {CalculateQuader}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Quader hat einen Volumen von {CalculateQuader}cm³")
        fehler += 1
        return


def ASLDreiecksPrisma():
    # G(a*kh:2) * H
    global fehler
    global richtig
    PrismaA = random.randint(1,100)
    PrismaB = random.randint(1,100)
    PrismaH = random.randint(1,200)
    CalcPrismaG = float(PrismaA) * float(PrismaB) / 2
    CalculatePrisma = CalcPrismaG * float(PrismaH)
    Antwort = input(f"Gegeben ist ein Dreiecksprisma mit der Seite a {PrismaA}cm b, {PrismaB}cm und eine Höhe von {PrismaH}cm\nBerechne den Volumen vom Dreiecksprisma, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculatePrisma:
        print(f"Richtig!\nDas Dreiecksprisma hat einen Volumen von {CalculatePrisma}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDas Dreiecksprisma hat einen Volumen von {CalculatePrisma}cm³")
        fehler += 1
        return

def ASLTrapezPrisma():
    # G(a*kh:2) * H
    global fehler
    global richtig
    TrapezA = random.randint(1,100)
    TrapezC = random.randint(1,100)
    TrapezH = random.randint(1,200)
    PrismaH = random.randint(1,500)
    CalculateTrapez1 = float(TrapezA) + float(TrapezC)
    CalculateTrapez2 = CalculateTrapez1 * float(TrapezH) / 2
    CalculateTPrisma = CalculateTrapez2 * float(PrismaH)
    Antwort = input(f"Gegeben ist ein Trapezprisma mit der Grundfläche: a {TrapezA}cm b, {TrapezC}cm und eine Höhe von {TrapezH}cm, Körperhöhe des Prismas beträgt {PrismaH}cm\nBerechne den Volumen vom Dreiecksprisma, zur überprüfung gib deine Antwort(Komma müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateTPrisma:
        print(f"Richtig!\nDas Trapezprisma hat einen Volumen von {CalculateTPrisma}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDas Trapezprisma hat einen Volumen von {CalculateTPrisma}cm³")
        fehler += 1
        return

##Aufgabensteller FLÄCHENINHALT

def ASLQuadrat():
    global fehler
    global richtig
    QuadratA = random.randint(1,9999)
    CalculateQuadrat = float(QuadratA) ** 2
    Antwort = input(f"Gegeben ist ein Quadrat mit der Seite a {QuadratA}cm\nBerechne den Flächeninhalt vom Quadrat, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateQuadrat:
        print(f"Richtig!\nDer Quadrat hat einen Volumen von {CalculateQuadrat}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Quadrat hat einen Volumen von {CalculateQuadrat}cm³")
        fehler += 1
        return

def ASLRechteck():
    global fehler
    global richtig
    RechteckA = random.randint(1,999)
    RechteckB = random.randint(1,999)
    CalculateRechteck = float(RechteckA) * float(RechteckB)
    Antwort = input(f"Gegeben ist ein Rechteck mit der Seite a {RechteckA}cm und b {RechteckB}cm\nBerechne den Flächeninhalt vom Rechteck, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateRechteck:
        print(f"Richtig!\nDas Rechteck hat einen Volumen von {CalculateRechteck}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDas Rechteck hat einen Volumen von {CalculateRechteck}cm³")
        fehler += 1
        return

def ASLDreieck():
    global fehler
    global richtig
    DreieckG = random.randint(1,100)
    DreieckH = random.randint(1,200)
    CalculateDreieck = float(DreieckG) * float(DreieckH) / 2
    Antwort = input(f"Gegeben ist ein Dreieck mit der Grundfläche von {DreieckG}cm und einer Höhe von {DreieckH}cm\nBerechne den Flächeninhalt vom Dreieck, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateDreieck:
        print(f"Richtig!\nDas Dreieck hat einen Volumen von {CalculateDreieck}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDas Dreieck hat einen Volumen von {CalculateDreieck}cm³")
        fehler += 1
        return

def ASLParallelogramm():
    global fehler
    global richtig
    ParallelogrammG = random.randint(1,100)
    ParallelogrammH = random.randint(1,200)
    CalculateParallelogramm = float(ParallelogrammG) * float(ParallelogrammH)
    Antwort = input(f"Gegeben ist ein Parallelogramm mit der Grundfläche von {ParallelogrammG}cm und einer Höhe von {ParallelogrammH}cm\nBerechne den Parallelogramm vom Rechteck, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateParallelogramm:
        print(f"Richtig!\nDer Parallelogramm hat einen Volumen von {CalculateParallelogramm}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Parallelogramm hat einen Volumen von {CalculateParallelogramm}cm³")
        fehler += 1
        return

def ASLTrapez():
    global fehler
    global richtig
    TrapezA = random.randint(1,100)
    TrapezC = random.randint(1,100)
    TrapezH = random.randint(1,200)
    CalculateTrapez1 = float(TrapezA) + float(TrapezC)
    CalculateTrapez = CalculateTrapez1 * float(TrapezH) / 2
    Antwort = input(f"Gegeben ist ein Trapez mit den Seiten a {TrapezA}cm, c {TrapezC}cm und einer Höhe von {TrapezH}\nBerechne den Flächeninhalt vom Trapez, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateTrapez:
        print(f"Richtig!\nDer Trapez hat einen Volumen von {CalculateTrapez}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Trapez hat einen Volumen von {CalculateTrapez}cm³")
        fehler += 1
        return

def ASLKreis():
    global fehler
    global richtig
    KreisR = random.randint(1,1337)
    CalcKR2 = float(KreisR) ** 2
    CalculateKreis = CalcKR2 * PI
    Antwort = input(f"Gegeben ist ein Kreis mit einen Radius von {KreisR}cm\nBerechne den Flächeninhalt vom Kreis, zur überprüfung gib deine Antwort(Kommatar müssen ein Punkt sein z.B 1307,752 müssen 1307.752 sein)!")
    if float(Antwort) == CalculateKreis:
        print(f"Richtig!\nDer Kreis hat einen Volumen von {CalculateKreis}cm³")
        richtig += 1
        return
    else:
        print(f"Falsch!\nDer Kreis hat einen Volumen von {CalculateKreis}cm³")
        fehler += 1
        return

##Funktionalität

def PunkteCheck():
    global fehler
    global richtig
    if fehler == 0:
        print(f"Großartig! Du hast alle 14. Aufgaben richtig bearbeitet")
    elif fehler == 1:
        print(f"Sehr gut! Du hast leider eine Aufgabe von 14 falsch bearbeitet.")
    elif fehler == 14:
        print(f"Uff... Du hast bei jeder Aufgabe einen Fehler gemacht! Lern weiter und mach Herr M. stolz")
    elif fehler == 2:
        print(f"Toll! du hast die hälfte der Aufgaben richtig bearbeitet, mach dir nichts drauß und lern weiter!")
    else:
        print(f"Du hast von 14 Aufgaben, {fehler} fehler gemacht!")



def AufgabenSteller():
    Antwort = input("Bestimmte Formeln(Formeln) oder Allgemein Alles(Alles)?\nEingabe als Formel / Alles")
    if Antwort == "Formeln" or Antwort == "formeln":
        AntwortF = input("Anwendung & Rechnung mit Volumen oder Flächeninhalt?")
        if AntwortF == "Volumen" or Antwort == "volumen":
            AntwortV = input("Welcher Geometrischer Körper?\n|Würfel|Quader|Zylinder|Dreiecksprisma|Trapezprisma|Pyramide|Kegel|Kugel|")
            if AntwortV == "Würfel" or AntwortV == "würfel":
                ASWürfel()
            elif AntwortV == "Quader" or AntwortV == "quader":
                ASQuader()
            elif AntwortV == "Zylinder" or AntwortV == "zylinder":
                ASZylinder()
            elif AntwortV == "Dreiecksprisma" or AntwortV == "dreiecksprisma":
                ASDreiecksPrisma()
            elif AntwortV == "Trapezprisma" or AntwortV == "trapezprisma":
                ASTrapezPrisma()
            elif AntwortV == "Pyramide" or AntwortV == "pyramide":
                ASqPyramide()
            elif AntwortV == "Kegel" or AntwortV == "kegel":
                ASKegel()
            elif AntwortV == "Kugel" or AntwortV == "kugel":
                ASKugel()

        elif AntwortF == "Flächeninhalt" or Antwort == "Flächeninhalt":
                AntwortF = input("|Quadrat|Rechteck|Dreieck|Parallelogramm|Trapez|Kreis|")
                if AntwortF == "Quadrat" or AntwortF == "quadrat":
                    ASQuadrat()
                if AntwortF == "Rechteck" or AntwortF == "rechteck":
                    ASRechteck()
                if AntwortF == "Dreieck" or AntwortF == "dreieck":
                    ASDreieck()
                if AntwortF == "Parallelogramm" or AntwortF == "paralellogramm":
                    ASParallelogramm()
                if AntwortF == "Trapez" or AntwortF == "trapez":
                    ASTrapez()
                if AntwortF == "Kreis" or AntwortF == "kreis":
                    ASKreis()
    elif Antwort == "Alles" or Antwort == "alles":
        global fehler
        global richtig
        ASLQuadrat() #Flächeninhalt
        ASLQuader() #Volumen
        ASLRechteck() #Flächeninhalt
        ASLWürfel() #Volumen
        ASLKreis() #Flächeninhalt
        ASLKegel() #Volumen
        ASLZylinder() #Volumen
        ASLDreieck() #Flächeninhalt
        ASLDreiecksPrisma() #Volumen
        ASLqPyramide() #Volumen
        ASLParallelogramm() #Flächeninhalt
        ASLTrapez() #Flächeninhalt
        ASLTrapezPrisma() #Volumen
        ASLKugel() #Volumen
        print("Du bist jetzt mit den Aufgabenfertig")
        PunkteCheck()

def Taschenrechner():
    Antwort = input("Flächeninhalt oder Volumen?")
    if Antwort == "Flächeninhalt" or Antwort == "flächeninhalt":
        AntwortF = input("|Quadrat|Rechteck|Dreieck|Parallelogramm|Trapez|Kreis|")
        if AntwortF == "Quadrat" or AntwortF == "quadrat":
            TRQuadrat()
        if AntwortF == "Rechteck" or AntwortF == "rechteck":
            TRRechteck()
        if AntwortF == "Dreieck" or AntwortF == "dreieck":
            TRDreieck()
        if AntwortF == "Parallelogramm" or AntwortF == "paralellogramm":
            TRParallelogramm()
        if AntwortF == "Trapez" or AntwortF == "trapez":
            TRTrapez()
        if AntwortF == "Kreis" or AntwortF == "kreis":
            TRKreis()
    elif Antwort == "Volumen" or Antwort == "volumen":
        AntwortV = input("|Würfel|Quader|Zylinder|Dreiecksprisma|Trapezprisma|Pyramide|Kegel|Kugel|")
        if AntwortV == "Würfel" or AntwortV == "würfel":
            TRWürfel()
        elif AntwortV == "Quader" or AntwortV == "quader":
            TRQuader()
        elif AntwortV == "Zylinder" or AntwortV == "zylinder":
            TRZylinder()
        elif AntwortV == "Dreiecksprisma" or AntwortV == "dreiecksprisma":
            TRDreiecksPrisma()
        elif AntwortV == "Trapezprisma" or AntwortV == "trapezprisma":
            TRTrapezPrisma()
        elif AntwortV == "Pyramide" or AntwortV == "pyramide":
            TRqPyramide()
        elif AntwortV == "Kegel" or AntwortV == "kegel":
            TRKegel()
        elif AntwortV == "Kugel" or AntwortV == "kugel":
            TRKugel()

def Check():
    Antwort = input("Willst du den Taschenrechner verwenden oder Formeln lernen?\nAls Eingabe bitte Taschenrechner / Formeln")
    if Antwort == "Taschenrechner" or Antwort == "taschenrechner":
        Taschenrechner()
    elif Antwort == "Formeln" or Antwort == "formeln":
        AufgabenSteller()

Check()
