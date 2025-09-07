import random

def autoroller(numberOfAttacks, ACToBeat, attackModifier, damageModifier, damageDice, dicePerAttack):
    outcomes = []
    totalDamage = 0
    crits = 0
    hits = 0
    misses = 0

    for _ in range(numberOfAttacks):
        attackRoll = random.randint(1,20) + attackModifier
        if((attackRoll - attackModifier) == 20):
            damage = damageModifier + sum(random.randint(1,damageDice) for _ in range(2 * dicePerAttack))
            outcomes.append(f"Crit Attack!: {attackRoll}. Damage: {damage}")
            totalDamage += damage
            crits += 1
        elif(attackRoll >= ACToBeat):
            damage = damageModifier + sum(random.randint(1,damageDice) for _ in range(dicePerAttack))
            outcomes.append(f"Attack: {attackRoll}. Damage: {damage}")
            totalDamage += damage
            hits += 1
        else:
            outcomes.append(f"Attack: {attackRoll}. Damage: Miss")
            misses += 1
    
    finalString = outputFormatter(outcomes)
    return (finalString, totalDamage, crits, hits, misses)



def outputFormatter(outcomes):
    finalString = ""
    
    for roll in outcomes:
        splitRoll = roll.split(". ")
        attackRoll = splitRoll[0]
        damage = splitRoll[1]
        finalString += "{0} {1} ".format(attackRoll, damage)
    
    return finalString