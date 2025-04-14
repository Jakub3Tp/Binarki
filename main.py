#Zamiana na Binarne
#Wczytaj liczby dziecietne.txt i zapisz je na liczby binarne w pliku binarne.txt

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

with open("binarne.txt", 'w') as file:
    file.write("\n".join(number))