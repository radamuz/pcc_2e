import sys

def make_sandwich(*toppings):
    
    sandwich_toppings = []

    if type(toppings[0]) == list:
        print("toppings es una lista\n")
        toppings = toppings[0]
        
    print("  Tus ingredientes: ")

    for topping in toppings:
        print(f"\t- {topping}")
        sandwich_toppings.append(topping)

    print("")

make_sandwich(sys.argv[1:])
make_sandwich('salsa', 'arroz')
