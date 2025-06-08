question = ["What is your name?" , "India's capital."]
answer = ["Pratham" , "Delhi"]
priceWon = 0

for i in range(len(question)):
    print(question[i])
    userAns = (input("Enter your answer:").title())
    if( userAns == answer[i]):
       print("correct answer")
       priceWon = priceWon + 10000 
    else:
        print("incorrect answer")
        priceWon
        break
print("You won the ₹",priceWon)