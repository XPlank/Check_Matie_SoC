# Write your code here
def cal_score(listt : list) :
    global dic
    if len(listt) >1 :
        if tuple(listt[:-1]) not in dic :
            dic[tuple(listt[:-1])]=cal_score(listt[:-1])
        
        if tuple(listt[1:]) not in dic :
            dic[tuple(listt[1:])]=cal_score(listt[1:])

        if listt[0]- dic[tuple(listt[1:])]> listt[-1]-dic[tuple(listt[:-1])] :
            return listt[0]-dic[tuple(listt[1:])]
        else :
            return listt[-1]-dic[tuple(listt[:-1])]

    return listt[0]

n=int(input())
listt=list(map(int, input().split()))

dic={}
score=cal_score(listt)

if score >0 :
    print("Player 1 wins")
elif score <0 :
    print("Player 2 wins")
else :
    print("Its a draw")