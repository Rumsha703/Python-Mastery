from typing import List

#global fuction(parent funtion) to take input as discount percentage and return a fuction
def discount_calculator_percentage(discount_percenatge: float):

#global variable
    mall_name="Wallmart"

#local funtion(child function) which performs calculation and returns discounted amount using gloabl parameters 
    def dicounted_cost(items: list ):
        total_cost=sum(items)
        discount_cost= (total_cost*discount_percenatge)/100
        discounted_amount=total_cost - discount_cost
        print(f"Thankyou for shopping at {mall_name}")
        print(f"You have got a discount of {discount_percenatge}% on total amount of {total_cost} and you have to pay {discounted_amount} ")
        

        return discounted_amount
    #exiting from child fuction and calling child fuction in parent fuction
    return dicounted_cost



cart=[1,2,3,4,5]

#assigning varaiable to discounted_amount of child fuction and calling parent fuction
da=discount_calculator_percentage(20)
#calling child fucntion
dc=da(cart)
