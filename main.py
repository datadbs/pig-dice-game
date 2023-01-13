import random

# 처음 참가인원 조사
def participate():
    global players
    global dealer_score
    dealer_score = 0
    players = dict()
    while True:
        num = int(input("몇명? 겜할거니 최대 3명 가능합니다.?"))
        if num <= 3:
            for i in range(num):
                players[input(f"Player {i+1} : ")] = 0
            break
        else:
            print("다시 입력해 최대 3명 가능")
    return players

# 주사위 굴리기
def roll():
    number = random.randint(1,6)
    print(f"You get {number}")
    return number


# 멈춰서 다음턴으로 넘기기
def stop(name,score):
    global players,dealer_score
    players[name] += score
    print("-----------------------------")
    print(players)
    print("Dealer Score :",dealer_score)
    print("-----------------------------")

    if players[name] > 50:
        # 게임 승리
        end(name,players[name])

# 게임종료 함수    
def end(name,score):
    global players
    print("#########################")
    print(f"{score}점 달성")
    print(f"{name} !!  Win !!!")
    print("#########################")
    exit()


# 플레이어가 롤을 할지 스탑할지 고르는 함수
def choice(name,temp_score):
    print(f"{name} !! 너 차례임",end=" ")
    menu = input("r : roll, s : stop What do you want ? ")
    if menu == 'r':
        score = roll()
        if score == 1:
            return print("1나와서 턴 종료")
        else:
            temp_score += score
            return re_choice(name,temp_score)
    elif menu == 's':
        return stop(name,temp_score)
    else:
        print("다시 입력해")
        return choice()

# 롤 한번더할때 함수
def re_choice(name,temp_score):
    print(f"현재 쌓인 점수 : {temp_score}",end ="  ")
    menu = input("r : roll, s : stop What do you want ? ")
    if menu == 'r':
        score = roll()
        if score == 1:
            temp_score = 0
            return print("1나와서 턴 종료")
        else:
            temp_score += score
            return re_choice(name,temp_score)
    elif menu == 's':
        return stop(name,temp_score)
    else:
        print("다시 입력해")
        return re_choice()

# 딜러 멈추는 함수
def dealer_stop(temp_score):
    global dealer_score
    global players
    dealer_score += temp_score
    print("Dealer : I want to stop now")
    print()
    print("-----------------------------")
    print(players)
    print("Dealer Score :",dealer_score)
    print("-----------------------------")
    print()
    return True

# 딜러 알고리즘
def dealer_algorithm():
    global dealer_score
    global players
    temp_score = 0
    while True:

        number = random.randint(1,6)
        print(f"Dealer get {number}, Nice~~")
        temp_score += number
        if dealer_score+temp_score >= 50:
            return end("dealer",dealer_score+temp_score)

        if number == 1:
            print("Oh my God ㅜㅠㅜ")
            break
        else:
            # 쌓인점수가 10넘으면 스탑
           
            if temp_score > 10:
                if dealer_stop(temp_score):
                    break
            # 주사위가 6나오면 무조건 멈춤
            elif number == 6:
                if dealer_stop(temp_score):
                    break
            
           
# 플레이 함수
def play():
    member = participate()
    while True:
        for i in member:
            temp_score = 0
            print()
            choice(i,temp_score)
        print()
        dealer_algorithm()

# Main
if __name__ == "__main__":
    play()

