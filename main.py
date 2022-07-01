import random
import time

od=0
do=0
przedzial=0
while(od==0):
    try:
        od = int(input("Podaj OD jakiej liczby ma być generowanie: ")) #Provide the first number of the interval
    except:
        print('Podana nieprawidlowa wartosc, wprowadz liczbe: ') #Input incorrect, provide the number

while(do==0):
    try:
        do = int(input("Podaj DO jakiej liczby ma być generowanie: ")) #Provide the last number of the interval
    except:
        print('Podana nieprawidlowa wartosc, wprowadz liczbe: ') #Input incorrect, provide the number
while(przedzial==0):
    try:
        przedzial = int(input("Podaj ILE liczb ma być wygenerowane: ")) #Provide how many numbers to generate
    except:
        print('Podana nieprawidlowa wartosc, wprowadz liczbe: ') #Input incorrect, provide the number
start_time = time.time()
rand_nums = [random.randint(od, do) for n in range(przedzial)]
print('Lista liczb wygenerowanych przez program: ', rand_nums) #The list of generated numbers
print('Liczby posortowane przez program:', sorted(rand_nums)) #The list of sorted generated numbers (ascending)
print("Czas potrzebny programowi na wykonanie operacji: {:.2f}s".format(time.time() - start_time)) #Time the program needed to print and sort the numbers
k = input("Można zamknąć program.") #Requires input, so you can close the program (it does not close itself)
