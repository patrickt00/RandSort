import random
import time

while True:
    od=0
    do=0
    przedzial=0
    while(od==0):
        try:
            od = int(input("Podaj OD jakiej liczby ma być generowanie: ")) #Provide the first number of the interval
        except:
            print('Podano nieprawidłową wartość, wprowadź liczbę: ') #Input incorrect, provide the number

    while(do==0):
        try:
            do = int(input("Podaj DO jakiej liczby ma być generowanie: ")) #Provide the last number of the interval
        except:
            print('Podano nieprawidłową wartość, wprowadź liczbę: ') #Input incorrect, provide the number
    while(przedzial==0):
        try:
            przedzial = int(input("Podaj ILE liczb ma być wygenerowane: ")) #Provide how many numbers to generate
        except:
            print('Podano nieprawidłową wartość, wprowadź liczbę: ') #Input incorrect, provide the number
    start_time = time.time()
    rand_nums = [random.randint(od, do) for n in range(przedzial)]
    print('Lista liczb wygenerowanych przez program: ', rand_nums) #The list of generated numbers
    print('Liczby posortowane przez program:', sorted(rand_nums)) #The list of sorted generated numbers (ascending)
    print("Czas potrzebny programowi na wykonanie operacji: {:.2f}s".format(time.time() - start_time)) #Time the program needed to print and sort the numbers

    while True:
        k = str(input("Czy chcesz zamknąć program? Wpisz 'y' aby zakończyć lub 'n' aby kontynuować: "))  # Requires input, so you can close the program (it does not close itself)
        if k in ('y', 'n'):
            break
        print("Wpisz 'y' aby zakończyć lub 'n' aby kontynuować: ")
    if k == 'n':
        continue #Program is being executed from the beginning
    else:
        print("Do widzenia!")
        break #Program is being closed