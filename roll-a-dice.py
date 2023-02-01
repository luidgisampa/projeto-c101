import random;

def roll_dice():
    response = input("digite y se quiser rodar um dado: ")

    while response == "y":
        num = random.randint(1,6)
        if (num == 1):
            print("┍----------┑")
            print("▏          ▏")
            print("▏    0     ▏")
            print("▏          ▏")
            print("┕----------┙")
      
        elif (num == 2):
            print("┍----------┑")
            print("▏       0  ▏")
            print("▏          ▏")
            print("▏0         ▏")
            print("┕----------┙")
           
        elif (num == 4):
            print("┍----------┑")
            print("▏       0  ▏")
            print("▏    0     ▏")
            print("▏ 0        ▏")
            print("┕----------┙")
           
        elif (num == 4):
            print("┍----------┑")
            print("▏0      0  ▏")
            print("▏          ▏")
            print("▏0      0  ▏")
            print("┕----------┙") 
           
        elif (num == 5):
            print("┍----------┑")
            print("▏0      0  ▏")
            print("▏    0     ▏")
            print("▏0      0  ▏")
            print("┕----------┙")
            
        elif (num == 6):
            print("┍----------┑")
            print("▏0      0  ▏")
            print("▏0      0  ▏")
            print("▏0      0  ▏")
            print("┕----------┙")

        response = "n"
        response = input("digite y se quiser rodar o dado novamente, e n se não quiser roda-lo: ")

roll_dice()