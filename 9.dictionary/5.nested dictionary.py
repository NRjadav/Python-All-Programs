
quiz = {
    1 : {
        'que' : 'who is prime minister of india ?',
        'ans' : 'narendra modi',
    },
    2 : {
        'que' : 'most popular programing language',
        'ans' : 'python',


    }

}

size=len(quiz)

for k in range(1,size+1):
    print("que = ",quiz[k]['que'])
    ans = input("Enter your ans:")
    if quiz[k]['ans']==ans:
        print("right answer")
    else:
        print("false answer")    

