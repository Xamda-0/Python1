import csv
import os

def Customer_Diwaan():
    # Magaca faylka
    filename = 'CustomerInformation.csv'

    # Hubi haddii faylka uu horey u jiro
    file_exists = os.path.isfile(filename)

    # Ku fur faylka habka "append mode" oo ku dar header haddii aanu jirin
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Haddii faylku aanu jirin, qor header-ka si loo kala hago
        if not file_exists:
            writer.writerow([
                "Username".ljust(15),
                "Full Name".ljust(25),
                "Age".ljust(10),
                "Sex".ljust(10),
                "Status".ljust(10),
                "Nooca Xanuunka".ljust(20),
                "Nooca Daawada".ljust(20)
            ])

        # Gelinta xogta isticmaalaha
        while True:
            print('Please write his/her information:')
            username = input("Username: ").strip().ljust(15)
            full_name = input("Full Name: ").strip().ljust(25)
            age = input("Age: ").strip().ljust(10)
            sex = input("Sex: ").strip().ljust(10)
            status = input("Status: ").strip().ljust(10)
            nooca_xanuun = input("Nooca xanuunka: ").strip().ljust(20)
            nooc_daawo = input("Nooca daawada: ").strip().ljust(20)

            # Ku qor xogta faylka
            writer.writerow([username, full_name, age, sex, status, nooca_xanuun, nooc_daawo])
            print('Data has been saved successfully!.')

            jawaab = input("Ma rabtaa inaad xog kale geliso? (Haa/Haa ma ahan): ").lower()
            if jawaab != 'haa':
                print("Faylka waa la xiray. Mahadsanid!")
                break

# Customer_Diwaan()