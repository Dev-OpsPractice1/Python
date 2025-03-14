print ("welcome to 'Hyderabad Biryani House' delivery")

quant = (str(input("please type your wished quantity mini or full or family : ")))

total = 0

if quant == "mini" :
    total += 150
if quant == "full" : 
    total += 250
if quant == "family" :
    total += 600
else:
    print("Invalid quantity! Please choose mini, full, or family.")
    exit()    

soft_drint = (str(input("if you want to add soft drink press ' y ' : ")))
if soft_drint == "y" :
    total += 20 

mayoo = (str(input("if you want to add mayoo press ' y ' : ")))
if mayoo == "y" :
    if quant == "family" :
        total += 60
    else :
        total += 30    

pudina_chetuny = (str(input("if you want to add pudina chetuny press ' y ' : ")))
if soft_drint == "y" :
    total += 25 
print(f"your total will be : {total}")