"""to-do:
    - incorporate house ownership tax benefits
    - use actual historical data to calculate S&P500 gains
    - turn this into class-based system
    - turn into GUI
    - allow edits of assumption numbers"""

import csv

#S&P500 historical data from www.macrotrends.net
history_data = csv.reader(open('sp-500-historical-annual-returns.csv'))

#make a dictionary of the S&P500 data
data = {}
for row in history_data:
    key = row[0]
    data[key] = row[1]
    
#get data from inputs
down_pay = int(input("What is the amount of the potential downpayment? \n> "))
price = int(input("What is the current sales price of the house?\n> "))
history = int(input("what is the last sales price of the house?\n> "))
year = int(input("What year was the house last sold?\n> "))
rent = int(input("What is your current rent?\n> "))
mortgage = int(input("What is your estimated mortgage?\n> "))
time = 2020 - year

#calculate gains if downpayment was invested in S&P500
def index_funds():
    index_gains = (int(down_pay) * (1 + 0.1)**time) - down_pay
    print(f"\nYour down payment would've gained ${round(index_gains, 2)} "
          "at 10% annual growth.")
    
#calculate gains of house equity
def equity():
    house_gains = (price - history) / time / history * 100
    print(f"\nThis house grew ${price - history} over {time} years"
          f" for an average of {round(house_gains, 2)}% annual growth.")

#calculate difference between rent and mortgage with 5% yearly increase in rent
def rent_vs_mortgage():
    global rent
    global mortgage
    global time
    rent_time = time
    total_rent = rent * 12
    while rent_time > 1:
        new_rent = rent * 1.05
        total_rent += (new_rent * 12)
        rent = new_rent
        rent_time -= 1
    total_mortgage = mortgage * 12 * time
    if total_rent > total_mortgage:
        savings = total_rent - total_mortgage
        print(f"\nYou'd save a total of ${round(savings, 2)} in monthly "
              f"payments over {time} years by buying this house.")
    else:
        savings = total_mortgage - total_rent
        print(f"\nYou'd save a total of ${round(savings, 2)} in monthly "
              f"payments over {time} years by renting.")

#calculate maintenance costs at an estimated 1% per year
def maintenance():
    repair = round(price * .01 * time)
    print(f"\nEstimated ${repair} in maintenance costs during this time.")

def worth():
    global rent
    repair = round(price * .01 * time)
    rent_time = time
    total_rent = rent * 12
    while rent_time > 1:
        new_rent = rent * 1.05
        total_rent += (new_rent * 12)
        rent = new_rent
        rent_time -= 1
    total_mortgage = mortgage * 12 * time
    index_gains = (int(down_pay) * (1 + 0.1)**time) - down_pay
    
    house_value = price - history - repair - total_mortgage
    index_value = index_gains - total_rent
    
    if house_value > index_value:
        print("\nThis house is a great deal!")
    elif house_value == index_value:
        print("\nMonetarily, no difference.")
    else:
        print("\nStick with index funds!")

    
equity()
maintenance()
index_funds()
rent_vs_mortgage()
worth()


print("\nAssumptions: \n\t- 5% yearly increase of rent (could be more! D:)"
      "\n\t- 10% annual S&P500 growth (negatively affected by Covid19!?)"
      "\n\t- 1% yearly maintenance costs (might not be relevant in a condo")