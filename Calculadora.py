while(True):
    try:
        print("Insira sua quantitade de vitórias em rankeadas: ")
        WinRate = int(input())
        break
    except:
        print("Insira somente numeros!")

print("")

while(True):
    try:
        print("Insira sua quantitade de derrotas em rankeadas: ")
        DefeatRate = int(input())
        break
    except:
        print("Insira somente numeros!")

WinRateTotal = WinRate - DefeatRate

if WinRateTotal <= 10:
    HeroRank = "Ferro"
elif WinRateTotal >= 11 and WinRateTotal <= 20:
    HeroRank = "Bronze"
elif WinRateTotal >= 21 and WinRateTotal <= 50:
    HeroRank = "Prata"
elif WinRateTotal >= 51 and WinRateTotal <= 80:
    HeroRank = "Ouro"
elif WinRateTotal >= 81 and WinRateTotal <= 90:
    HeroRank = "Diamante"
elif WinRateTotal >= 91 and WinRateTotal >= 100:
    HeroRank = "Lendário"
elif WinRateTotal >= 101:
    HeroRank = "Imortal"
    
print(f"O Héroi tem saldo de {WinRateTotal} está no rank de {HeroRank}!")