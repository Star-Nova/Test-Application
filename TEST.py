

class Test:
    def __init__(self):
        self.sorular = [
            {"soru": "En popüler yazılım dili hangisidir?\n-C++\n-Python\n-Java\n-Javascript ", "cevap": "Python" or "PYTHON" or "python"},
            {"soru": "Python'un sürekli döngü yapısı nedir?\n-While\n-For\n-İf", "cevap": "While" or "WHİLE" or "while"},
            {"soru": "Python'da veri türleri nelerdir?(Cevabı küçük harflerle yazınız!)", "cevap": "integer"},
            {"soru": "Python'da hangi anahtar kelime try-except bloklarını tanımlamak için kullanılır?", "cevap": "try" or "TRY" or "Try"},   
            {"soru": "Python'da bir fonksiyonu tanımlamak için hangi anahtar kelime kullanılır?\n-For\n-Def\n-İf", "cevap": "Def" or "DEF" or "def"},
            {"soru": "Python'da liste elemanlarına nasıl erişilir?", "cevap": "indeksleme" or "İndeksleme" or "İNDEKSLEME"},
            {"soru": "Python'da bir stringteki elemeanların hepsini büyük yazmak için ne kullanırız?\n-Upper\n-Lower\n-For", "cevap": "Upper" or "UPPER" or "upper"},
            {"soru": "Python'da bir metni ekrana yazdırmak için hangi fonksiyon kullanılır?", "cevap": "print" or "PRİNT" or "Print"},
            {"soru": "Python'da bir liste elemanını silmek için hangi fonksiyon kullanılır?\n-Append\n-Remove", "cevap": "remove" or"REMOVE" or "Remove"},
            {"soru": "Python'da bir string'i parçalamak için kullanılan metot hangisidir?\n-Split\n-Remove\n-Print", "cevap": "split" or "SPLİT" or "Split"}
        ]
        self.puan = 0

    def testi_calistir(self):
        for soru_numarasi, soru in enumerate(self.sorular, 1):
            print(f"Soru {soru_numarasi}: {soru['soru']}")
            cevap = input("Cevabınızı girin: ")

            if cevap.lower() == soru['cevap'].lower():
                print("Doğru!")
                self.puan += 10
            else:
                print("Yanlış!")

        print(f"\nTesti tamamladınız! Toplam puanınız: {self.puan}/100")


if __name__ == "__main__":
    test = Test()
    test.testi_calistir()

    
