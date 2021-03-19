def checkLetters(word,sigma):
  for letter in word:
    if letter not in sigma:
      return False
  return True

fl_to_read = input()
f = open(fl_to_read,"rt")
content = f.readlines()
f.close()
sigma = []
states = [] 
trans = []

i = 0 
#removing the comments and trimming the input
while i < len(content):
    if content[i][0] == '#':
        content.remove(content[i])
    else:
        content[i] = content[i].replace(" ","").replace("\t",'').replace('\n','')
        i += 1


#going through content and getting the values
i = 0
while i < len(content):
    if content[i] == 'Sigma:':
        i += 1
        while content[i] != 'End':
            sigma.append(content[i])
            i += 1
        i += 1
    if content[i] == 'States:':
        i += 1
        while content[i] != 'End':
            states.append(content[i])
            i += 1
        i += 1
    if content[i] == 'Transitions:':
        i+=1
        while content[i] != 'End':
            trans.append(content[i].split(','))
            i += 1
        i += 1



#checking the initial and final states
#and removing S and F
initialState = []
finalStates = []

for i in range(0,len(states)):
    if "S" in states[i] or "F" in states[i]:
        helper = states[i].split(",")
        if "S" in states[i]:
            initialState.append(helper[0])
        if "F" in states[i]:
            finalStates.append(helper[0])
        states[i] = helper[0]
        


if len(initialState) != 1:
    print('Invalid number of initial states')
    exit()
if len(finalStates) == 0:
    print("No final state detected")
    exit()

if len(trans) != len(states)*len(sigma):
    print("Might be error if it's DFA. Every state should have another state specified on each input")

for element in trans:
    if element[0] not in states or element[2] not in states:
        print("One of the states doesn't exist in States")
        exit()
    if element[1] not in sigma:
        print("Input that was not in Sigma")
        exit()

print("Everything went alright")


#adding transitions into dictionary for easier use later on
transitions = {}
for element in trans:
    transitions[element[0] + '->' + element[1]] = element[2]

while(True):
    word = input()
    if len(word) == 0:
        if initialState[0] in finalStates:
            print("Cuvantul este acceptat")
        else:
            print("Cuvantul nu este acceptat")
        continue
    


    if checkLetters(word,sigma) == True:
        nextState = transitions[initialState[0] + "->" + word[0]]
        word = word[1:]

        while len(word) > 0:
            nextState = transitions[nextState+ "->" + word[0]]
            word = word[1:]

        if nextState in finalStates:
            print("Cuvantul este acceptat")
        else:
            print("Cuvantul nu este acceptat")
    else:
        print("Wrong word! Not at all in limbaj")






