# -----------------------------------------+
# Tiegan Cozzie                             |
# CSCI 127, Program 2                      |
# Last Updated: September 29, 2021             |
# Name: Tiegan Cozzie                            |
# -----------------------------------------|
# Poker Hand Evaluation                    |
# -----------------------------------------+

import random

# Helper Function
# Given a poker hand as a list, return a list of the ranks

# Parameter listNum determines whether you want the number, "0" or suit,  "1"
def get_all_ranks(hand,listNum):
    result = []
    for card in hand:
        result.append(card[0+listNum])
    return result

    
# Count is making sure all the numbers within the deck are from 10-14. if so, the count should be 5 which makes the first statement true
# The suits are checking with the card in position 0 to see if they are all the same. if so, the second statement is true
# If both statements are true the royal flush function will return True
def royal_flush(hand):
    count=0
    S=""
    numbers=get_all_ranks(hand,0)
    suits=get_all_ranks(hand,1)

    
    for x in range(len(numbers)):
        if (numbers[x]==10+x):
            count+=1
        else:
            count=count

            
    if (suits[0]==suits[1]) and (suits[0]==suits[2]) and (suits[0]==suits[3]) and (suits[0]==suits[4]):
        S=True
    else:
        S=False

        
    if (count==5) and (S==True):
        return True
    else:
        return False


# First "if" statement checks if the card to the left is exactly one less then the card before it, If all cards are one less then the card to the right, N will be true
# Second "if" statement makes sure all the suits are the same with the card in position 0. if so, S will be true
# If S and N are both true the function will return True
def straight_flush(hand):
    N=""
    S=""
    numbers=get_all_ranks(hand,0)
    suits=get_all_ranks(hand,1)
    if (0<numbers[4]-numbers[3]<2) and (0<numbers[3]-numbers[2]<2) and (0<numbers[2]-numbers[1]<2) and (0<numbers[1]-numbers[0]<2):
         N=True
    else:
        N=False
    if(suits[0]==suits[1]) and (suits[0]==suits[2]) and (suits[0]==suits[3]) and (suits[0]==suits[4]):
        S=True
    else:
        S=False
    if (N==True) and (S==True):
        return True
    else:
        return False


# First "if" statement checks if the card to the left is exactly one less then the card before it, if all cards are one less then the card to the right, the function will return true
def straight(hand):
    numbers=get_all_ranks(hand,0)
    if (0<numbers[4]-numbers[3]<2) and (0<numbers[3]-numbers[2]<2) and (0<numbers[2]-numbers[1]<2) and (0<numbers[1]-numbers[0]<2):
        return True
    else:
        return False


# With a 4 of a kind, cards can only be arranged in 2 ways
#first way is all 4 start with the first card and the second way is all 4 start with the seconf card
def four_of_a_kind(hand):
    count=0
    numbers=get_all_ranks(hand,0)
    #checks the first way and seeing if the cards match with card in position 0
    for x in range(len(numbers)):
        if (numbers[0]==numbers[x]):
            count+=1
        else:
            count=count
    if (count!=4):
        count=0
        # If the count doesn't equal 4, this next if statement will check for the four of a kind referencing the card in position 1
        for x in range(len(numbers)):
            if (numbers[1]==numbers[x]):
                count+=1
            else:
                count=count
    if (count==4):
        return True
    else:
        return False
        

# This identifies if any cards match and how many there are of each pair
# if count1 has 2 and count2 has 3, or vise versa, this will equate to a full house
def full_house(hand):
    numbers=get_all_ranks(hand,0)
    count1=0
    count2=0
    for x in range(len(numbers)):
        if (numbers[0]==numbers[x]):
            count1+=1
        else:
            count1=count1
        if (numbers[4]==numbers[x]):
            count2+=1
        else:
            count2=count2
    if (count1+count2==5):
        return True
    else:
        return False


# This function checks to see if all the suits are the same
# if so, the count should equal 5 and would return true
def flush(hand):
    suits=get_all_ranks(hand,1)
    count=0
    for x in range(len(suits)):
        if (suits[0]==suits[x]):
            count+=1
        else:
            count=count
    if (count==5):
        return True
    else:
        return False
    
# For a three of a kind, the pair can be in one of 3 positions. That is why there is threee counts. One for checking each position
# If one of the three counts equals 3, then the function would equate to true
def three_of_a_kind(hand):
    numbers=get_all_ranks(hand,0)
    count1=0
    count2=0
    count3=0
    for x in range(len(numbers)):
        if (numbers[0]==numbers[x]):
            count1+=1
        else:
            count1=count1
        if (numbers[1]==numbers[x]):
            count2+=1
        else:
            count2=count2
        if (numbers[4]==numbers[x]):
            count3+=1
        else:
            count3=count3
    if (count1==3) or (count2==3) or (count3==3):
        return True
    else:
        return False
        
# Two pair can end up in three different positions in a hand
def two_pair(hand):
    numbers=get_all_ranks(hand,0)
    twoPair=0
    # if the cards in position 0 and 1 turn out to be a pair, there are then only two other positions in which the other pair can be in
    if (numbers[0]==numbers[1]):
        twoPair+=1
        #checks to see if the last pair is within position 2 and 3, if not. it will then check for positions 3 and 4
        if (numbers[2]==numbers[3]):
            twoPair+=1
        elif (numbers[3]==numbers[4]):
            twoPair+=1
        else:
            twoPair=twoPair
    # if the first pair isnt within position 0 and 1, it would then check for position 1 and 2, if true, the other pair can only be in one spot
    elif (numbers[1]==numbers[2]):
        twoPair+=1
        #if position 1 and 2 is a pair, it will now check 3 and 4
        if(numbers[3]==numbers[4]):
            twoPair+=1
        else:
            twoPair=twoPair
    else:
        twoPair=twoPair
    # If two Pair equates to 2, then the function will return true
    if (twoPair==2):
        return True
    else:
        return False
        
# Goes through each card one by one and checks to see if it has a pair
def pair(hand):
    numbers=get_all_ranks(hand,0)
    pair=0
    if (numbers[0]==numbers[1]):
        pair+=1
    elif (numbers[1]==numbers[2]):
        pair+=1
    elif (numbers[2]==numbers[3]):
        pair+=1
    elif (numbers[3]==numbers[4]):
        pair+=1
    else:
        pair=pair
        
    #if pair equates to one, then the function will return true
    if(pair==1):
        return True
    else:
        return False

# Generates a list off all possible numbers in a deck and all possible suits in a deck
# This function then randomly pairs a number with a suit and appends that to your hand
# Once each card is appended, it will be removed from being picked again to avoid not real scenarios
def generate_hand():
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14
    userHand=[]
    allNum=[]
    allSuits=[]
    count=1
    for y in range(8):
        count+=1
        for x in range(4):
            allNum.append(count)
    for x in range(4):
        allNum.append(T)
        allNum.append(J)
        allNum.append(Q)
        allNum.append(K)
        allNum.append(A)
    for x in range(13):
        allSuits.append("spd")
        allSuits.append("hrt")
        allSuits.append("clb")
        allSuits.append("dmd")

    for x in range(5):
        num=random.choice(allNum)
        suit=random.choice(allSuits)
        allNum.remove(num)
        allSuits.remove(suit)
        userHand.append([num,suit])
    return userHand


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort() 
    print(poker_hand, " is ", end="")
    if royal_flush(poker_hand):
        print("a Royal Flush")
    elif straight_flush(poker_hand):
        print("a Straight Flush")
    elif four_of_a_kind(poker_hand):
        print("a Four of a Kind")
    elif full_house(poker_hand):
        print("a Full House")
    elif flush(poker_hand):
        print("a Flush")
    elif straight(poker_hand):
        print("a Straight")
    elif three_of_a_kind(poker_hand):
        print("Three of a Kind")
    elif two_pair(poker_hand):
        print("Two Pair")
    elif pair(poker_hand):
        print("a Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    
    user=input("Do you want to draw your own hand??\n type 'yes' or 'no': ")
    
    if (user=="yes"):
        hand=generate_hand()
        evaluate(hand)
    else:
        evaluate([[2, "spd"], [7, "clb"], [8, "dmd"], [A, "dmd"], [Q, "hrt"]])    # nothing
        evaluate([[T, "spd"], [A, "spd"], [Q, "spd"], [K, "spd"], [J, "spd"]])    # royal flush
        evaluate([[T, "clb"], [9, "clb"], [6, "clb"], [7, "clb"], [8, "clb"]])    # straight flush
        evaluate([[2, "dmd"], [7, "clb"], [2, "hrt"], [2, "clb"], [2, "spd"]])    # 4 of a kind
        evaluate([[8, "dmd"], [7, "clb"], [8, "hrt"], [8, "clb"], [7, "spd"]])    # full house
        evaluate([[2, "hrt"], [9, "hrt"], [3, "hrt"], [6, "hrt"], [T, "hrt"]])    # flush    
        evaluate([[K, "dmd"], [7, "clb"], [7, "hrt"], [8, "clb"], [7, "spd"]])    # 3 of a kind
        evaluate([[T, "clb"], [9, "clb"], [6, "clb"], [7, "clb"], [8, "spd"]])    # straight
        evaluate([[T, "spd"], [9, "clb"], [6, "dmd"], [9, "dmd"], [6, "hrt"]])    # 2 pair
        evaluate([[T, "spd"], [Q, "clb"], [6, "dmd"], [9, "dmd"], [Q, "hrt"]])    # 1 pair




# -----------------------------------------+

main()
