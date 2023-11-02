#Question_2

#creating dictionary to storing values
letter_values = {
    "A":1 ,"B":3 ,"C":3 ,"D":2 ,"E":1 ,"F":4 ,"G":2 ,"H":4 ,"I":1 ,"J":8 ,"K":5 ,"L":1 ,"M":3 ,"N":1 ,"O":1 ,
    "P":3 ,"Q":10 ,"R":1 ,"S":1 ,"T":1 ,"U":1 ,"V":4 ,"W":4 ,"X":8 ,"Y":4 ,"Z":10
}

#Funtion to calculate score
def calculate_word_score(word):
    word = word.upper()
    score = sum(letter_values.get(i,0) for i in word)
    return score
    
#get the inputs 
player_1 = input()
player_2 = input()

#calculate_scores 
player_1_score = calculate_word_score(player_1)
player_2_score = calculate_word_score(player_2)

#detremine the winner

if player_1_score > player_2_score:
    print("Player 1 wins!")
elif player_2_score > player_1_score:
    print("Player 2 wins!")
else:
    print("Tie!")