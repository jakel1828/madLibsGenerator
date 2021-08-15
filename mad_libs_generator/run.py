adj1 = input('Enter an adjective: ')
adj2 = input('Enter an adjective: ')
noun1 = input('Enter a noun: ')
noun2 = input('Enter a noun: ')
pnoun1 = input('Enter a plural noun: ')
game1 = input('Enter a game: ')
pnoun2 = input('Enter a plural noun: ')
verbing1 = input('Enter a verb ending in "ing": ')
verbing2 = input('Enter a verb ending in "ing": ')
pnoun3 = input('Enter a plural noun: ')
verbing3 = input('Enter a verb ending in "ing": ')
noun3 = input('Enter a noun: ')
plant1 = input('Enter a plant: ')
bodypart1 = input('Enter a part of the body: ')
place1 = input('Enter a place: ')
verbing4 = input('Enter a verb ending in "ing": ')
adj3 = input('Enter an adjective: ')

while True:
       try:
              number1 = int(input('Enter a whole number: '))
       except ValueError:
              print("That was not a whole number. Please try again.")
              continue
       else:
              break
pnoun4 = input('Enter a plural noun: ')
print('You have entered all the prompts. Now for the mad lib!')
print('A vacation is when you take a trip to some ' + adj1 + ' place with your ' + adj2 + ' family. Usually you go to'
' some place that is near a/an ' + noun1 + ' or up on a/an ' + noun2 + '. A good vacation place is one where'
' you can ride ' + pnoun1 + ' or play ' + game1 + ' or go hunting for ' + pnoun2 + '. I like to spend my time '
+ verbing1 + ' or ' + verbing2 + '. When parents go on a vacation, they spend their time eating three ' + pnoun3
+ ' a day, and fathers play golf, and mothers sit around ' + verbing3 + '. Last summer, my little brother fell in' \
' a/an ' + noun3 + ' and got poison ' + plant1 + ' all over his ' + bodypart1 + '. My family is going to (the)'
+ place1 + ', and I will practice ' + verbing4 + '. Parents need vacations more than kids because parents are'
' always very ' + adj3 + ' and because they have to work ' + str(number1) + ' hours every day all year making enough '
+ pnoun4 + ' to pay for the vacation.')
