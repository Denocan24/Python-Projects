#Program hala bitmedi. Üzerinde çalışıcam en yakın zamanda... Umarım bunu başarılı bir şekilde tamamlarım.
import random

def NumberGuessGame():
        
    while True:
            
            TargetNumber = random.randint(1, 50)
            print("1 ile 50 arasında tuttuğum rastgele bir sayıyı bulabilir misin?")

            while True:

                try:
                    
                    Guess = int(input("Tuttuğum Sayıyı Tahmin Et: "))

                    if Guess < TargetNumber:

                        print("Daha büyük bir sayı tahmin etmiştim...")
                    
                    elif Guess > TargetNumber:
                        print("Daha küçük bir sayı tahmin etmiştim...")
                    
                    else:

                        print(f"Tebrikler! {TargetNumber} sayısını bilmeyi başardın.")
                    
                except ValueError:

                    print("Lütfen geçerli bir sayı gir!")

                RepeatGame = input("Tekrar oynamak ister misin? (E/H): ").strip().lower()
                if RepeatGame != 'e':
                    print("Oyun bitti! Görüşürüz.")
                    break

NumberGuessGame()