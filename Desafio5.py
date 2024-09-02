def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Digite uma palavra: ")
print("Palavra invertida:", inverter_string(string))
