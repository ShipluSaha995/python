secret_number=9
count=0
limit=3
times=1
print("You have only 3 chance.\n")
while count<limit:
    guess=int(input(f"Enter Your guess number {times}: "))
    count+=1
    times+=1
    if(guess==secret_number):
        print("\nYou Won!\n")
        break
else:
    print("Sorry, Your limit is over\n")