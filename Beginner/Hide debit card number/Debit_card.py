debit_card=input("Enter a 16 digit card number with space after four digits: ").replace(" ","")



counter=0
card_number=""
for x in debit_card:
    counter+=1
    if counter <=12:
        card_number+="*"
    else:
        card_number+=x
print(card_number)