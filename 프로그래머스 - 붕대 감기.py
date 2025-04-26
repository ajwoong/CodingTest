bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]

currentHealth = health
continueSuccess = 0
death = 0

i = 0
for time in range(attacks[len(attacks)-1][0]+1):
    if(time != attacks[i][0]):
        continueSuccess += 1
        if(continueSuccess == bandage[0]):
            if(currentHealth < health):
                if(currentHealth + bandage[2] >= health):
                    currentHealth = health
                else:
                    currentHealth += bandage[2]
            continueSuccess = 0
        if(currentHealth < health):
            if(currentHealth + bandage[1] >= health):
                currentHealth = health
            else:
                currentHealth += bandage[1]
    else:
        if(currentHealth - attacks[i][1] <= 0):
            death = 1
        else:
            currentHealth -= attacks[i][1]
            continueSuccess = 0
            i += 1

if(death == 1):
    print(-1)
else:
    print(currentHealth)