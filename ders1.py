print("ATM MİZE HOŞGELDİNİZ")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Bankamızdan '4' tuşu ile çıkabilirsiniz.

""")

bakiye  = 400 

while True:
    islem = input("Bir işlem Seçiniz:")

    if (islem == "4"):
        print("Bizi Tercih Etiiğniz İçin Teşekkür Eder,İyi Günler Dileriz")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} tldir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz Tutarı Giriniz:"))
        bakiye += miktar
        print("Yatırım İşlemi  Başarılı")
    elif (islem == "3"):
        miktar = int(input("Çekilecek Tutarı Giriniz:"))
        if (miktar <= bakiye ):
            bakiye -= miktar
            print("Para Çekme İşlemi Başarılı")
        else:
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} tldir".format(bakiye))
    else:
        print("Lütfen geçerli bir işlem giriniz.")