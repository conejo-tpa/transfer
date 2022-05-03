import os
os.system("pip install samino==1.9.7")  # SAmino 1.9.7
import samino, threading

os.system("clear")
e = input("Email: ")
p = input("Contraseña: ")
url = input("URL VIP: ")  

os.system("clear")
client = samino.Client()
client.login(e, p)
coins = client.get_wallet_info().totalCoins
print(f"Tus monedas = {coins} \n")
c = int(input("Cuantas coins desea enviar? > "))
total = 0
path = client.get_from_link(url)
comId = path.comId
userId = path.objectId
client.join_community(comId)
local = samino.Local(comId)
fee = int(local.get_user_info(userId).influencerMonthlyFee)
if fee > c: print(f"VIP Subscription Coins is {fee}\nyou chose {c}")

for _ in range(int(c / fee)):
    threading.Thread(target=local.subscribe, args=(userId,)).start()
    coins -= 500
    print("500 Donadas")
    total += 500
    if coins < 500:
        break

print(f"Total coins Donadas {total}")