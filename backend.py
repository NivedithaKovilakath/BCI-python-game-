import random
def to_list(n):
    res = []
    while n>0:
        res.append(n%10)
        n/=10

#correct colour wrong or right place
def digitsMatched(anum,gnum):
    m=0
    for i in gnum:
            if anum.count(i)>0:
                m=m+1
    return m
#correct place correct colour
def find_fully_correct(answer, guess):
    res= 0
    for x, y in  zip(guess, answer):
        if x == y:
            res+=1
    return res 
#create adminno/answer
def create_code():
    characters = '123123123123123'
    length = 3 
    l = list(random.sample(characters,length))
    return l
answer = create_code()
print(answer)
tryy=5
while tryy>0:
        guess = input("Enter  guess")
        match=digitsMatched(answer,guess)
        print("Correct colour  " ,match)
        count = find_fully_correct(answer,guess)
        if count==3:
            print("Game Won!!!")
            print("You took ", str(5-tryy),"tries...")
            break
        print("Correct colour correct position " ,count)
        tryy-=1
