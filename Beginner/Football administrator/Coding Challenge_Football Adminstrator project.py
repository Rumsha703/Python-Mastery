status=input("What is the match status? ")

if status=="Suspended".lower():
    print("Match was suspended")

elif status =="Played".lower():
    home_team=int(input("How many goals home team created? "))
    away_team=int(input("How many goals away team created? "))
    if home_team > away_team:
        print("home team won")
    elif home_team==away_team:
        print("draw")
    else:
        print("Away team won")
else:
    print("Invalid response")
