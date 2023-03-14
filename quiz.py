print ('Seja muito bem vindo ao Quiz da Staff!')
pergunta = input("Vamos começar? (S/N)")

if pergunta != "S":
    quit()

score = 0

print("1..2..3..Já!")
print("Quais locais são zonas safes? \n (A) Praça Central \n (B) Departamento de Polícia \n (C) Mecanica \n (D) Zonas Vermelhas \n")
resp1 = input("Resposta: ")

if resp1 == "C":
    print("Acertou! *-* ")
    score = score + 1
else:
    print("Errou!:C ")

print("Qual armamento é permitido no sul? \n (A) Submetralhadoras \n (B) Pistolas \n (C) Fuzis \n (D) Shotgun \n")
resp1 = input("Resposta: ")

if resp1 == "B":
    print("Acertou! *-* ")
    score = score + 1
else:
    print("Errou!:C ")

print("Qual armamento é permitido no norte? \n (A) Submetralhadoras \n (B) Pistolas \n (C) Fuzis \n (D) Shotgun \n")
resp1 = input("Resposta: ")

if resp1 == "C":
    print("Acertou! *-* ")
    score = score + 1
else:
    print("Errou!:C ")

print("Qual quebra de RP é aplicado o banimento da cidade? \n (A) RDM \n (B) VDM \n (C) Power Gaming \n (D) Dark RP \n")
resp1 = input("Resposta: ")

if resp1 == "D":
    print("Acertou! *-* ")
    score = score + 1
else:
    print("Errou!:C ")

print("Quantos dias consistem o RP de Gravidez? \n (A) 5 \n (B) 7 \n (C) 9 \n (D) 10 \n")
resp1 = input("Resposta: ")

if resp1 == "C":
    print("Acertou! *-* ")
    score = score + 1
else:
    print("Errou!:C ")

print(f"Quiz terminou! Voce acertou: {score}/5")