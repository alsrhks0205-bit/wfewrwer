from poke.Pokemon import Pokemon
import random

def process_attack(attacker,defender):
    print(f"{attacker.name} 의 공격")
    dmg = attacker.atk - defender.arm
    defender.hp -= dmg
    print(f"damage {dmg} : ")
    print(f"{defender.name}remain hp {defender.hp} : ")
    if defender.hp <= 0:
        print(f"game over, {attacker.name} win!!")
        return True

    return False

print("===POKEMON===")
p1 = Pokemon("피카쥬쥬", 100, 10, 3)
p2 = Pokemon("꼬북꼬북", 110, 8, 5)
p3 = Pokemon("파파이리", 90, 12, 1 )

n = input("선택한 포켓몬 번호 : ")
match n:
    case "1": user = Pokemon("피카쥬쥬", 100, 10, 3)
    case "2": user = Pokemon("꼬북꼬북", 110, 8, 5)
    case "3": user = Pokemon("파파이리", 90, 12, 1 )
    case _ : user = None

r = random.randint(1,3)
match r:
    case 1: com = Pokemon("피카쥬쥬", 100, 10, 3)
    case 2: com = Pokemon("꼬북꼬북", 110, 8, 5)
    case 3: com = Pokemon("파파이리", 90, 12, 1 )
    case _ : com = None

print(f"user : {user}")
print(f"com : {com}")

print(user == com)

print("user 의 공격")
dmg = user.atk - com.arm
com.hp -= dmg
if com.hp <= 0:
    print("game over")

print("com 의 공격")
dmg = com.atk - user.arm
user.hp -= dmg
if user.hp <= 0:
    print("game over")

while True:
    #user -> com
    is_finish = process_attack(user, com)
    if is_finish: break

    #com -> user
    is_finish = process_attack(com, user)
    if is_finish: break