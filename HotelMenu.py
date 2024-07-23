#Define The Menu Of Restaurant
menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee': 90,
    'Chole Bhature' : 120,
    'Daal Puri' : 100,
    'Poha' : 40,
    'Kachori' : 30
}

#Greet
print("Welcome To PYTHON Restaurant !")
print(" Pizza: Rs40\n Pasta: Rs50\n Burger: Rs60\n Salad: Rs70\n Coffee: Rs90 \n Chole Bhature: Rs120 \n Daal Puri: Rs100 \n Poha: Rs40 \n Kachori: Rs30")

total_order = 0
# 40 + 50 = 90

item_1 = input("Enter The Name Of The Item You Want To Order --> ")

#Using Membership Oprator To Check Item Avilabale Of Not

if item_1 in menu:
    total_order += menu[item_1] #0 + Salad Order than total is 70
    print(f"Your Item {item_1} Has Been Added To Your Oder ! ")

else:
    print(f"Order Item {item_1} Not Available Yet ! ")

another_order = input("Do You Want To Add Another Item ? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter The Name Of Second Item --> ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Item {item_2} Has Been Added To Order !")
    else:
        print(f"Order Item {item_2} Is Not Available !")
    
print(f"The Total Amount Of Items To Pay Is {total_order}")
