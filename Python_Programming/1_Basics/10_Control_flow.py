#Bill example with control flow statements

bill_total = 210

discount1 = 10
discount2 = 20

if bill_total > 200:
    print('Bill greater than 200, you get a discount of 20%')
    bill_total = bill_total - (bill_total * discount2 / 100)
elif bill_total > 100:
    print('Bill greater than 100, you get a discount of 10%')
    bill_total = bill_total - (bill_total * discount1 / 100)
else:
    print('Bill less than 100, no discount applied')
    
print('Your total bill is $', bill_total)


#Light example with control flow statements

#Light is currently off
current = False #True means light is on, False means light is off

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')



