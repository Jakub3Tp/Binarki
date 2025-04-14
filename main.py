#Zamiana na Binarne
#Wczytaj liczby dziecietne.txt i zapisz je na liczby binarne w pliku binarne.txt
"""
with open("dziesietne.txt", 'r') as file:
    lines = file.read()
    lines = lines.split("\n")

    binarNumber = []

for number in lines:
    result = ""
    number_int = int(number)
    while number > 0:
        result += str(number_int % 2)
        number_int //= 2
    result = result[::-1]
    binarNumber.append(result)

ALternatywna metoda:
    for number in file:
        binarNumber.append(bin(number))
"""

# Schemat Hornera
with open("binarne2.txt", 'r') as file:
    lines = file.read()
    lines = lines.split('\n')

#alter methoda
for number in lines:
    print(int(number, base=2))

'''
for number in lines:
    result = int(number[0])
    for n in range(1, len(number)):
        result = result * 2 + int(number[n])
    print(result)
'''

#with open("binarne.txt", 'w') as file:
#    file.write("\n".join(binarNumber))