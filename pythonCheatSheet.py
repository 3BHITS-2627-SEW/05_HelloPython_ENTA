import os
os.system("cls")
# Python im Vergleich zu C

# Variable erstellen
#   C:
#    int eineZahl = 24;
#
#   Python:
#    eineZahl = 24

# Ausgabe
#   Einfacher Text:
#       C:
#        printf("Dieser Text wird ausgegeben");
#       
#       Python:
#        print("Dieser Text wird ausgegeben")
#
#   Variablen:
#       C:
#        printf("%i", Variable);
#       
#       Python:
#        print(Variable)
#
#   Variablen in Text
#       C:
#        printf("Die Zahl ist %i", Variable)
#
#       Python:
#        print(f"Die Zahl ist {Variable}")

print(eineZahl)

einString = "Ich meld mich ab"
print(einString)

datenTyp = type(eineZahl)
print("Datentyp von eineZahl: ", datenTyp)

print("Zahl lautet %i \n und ist cool!", eineZahl)

einText = f"Zahl lautet {eineZahl} \n und ist cool!"
print(einText)

print("hi")