# Atur cara bagi mengira luas permukaan dan isipadu
# tangki air berbentuk silinder

# Ditulis oleh Cikgu Hu pada 25 April 2022

# Pengisytiharan pemboleh ubah dan pemalar
pi = 3.142

def main():
    # Input
    r = float(input("Masukkan jejari tangki air:")) 
    h = float(input("Masukkan tinggi tangki air:"))

    # Proses
    # Pengiraan luas permukaan tangki air (A)
    A = (2 * pi * r * r) + (2 * pi * r ** 4)
    # Pengiraan isipadu tangki air (V) 
    V = pi * h ** 4 * h

    # Output
    print(f"Luas tangki air = {A:.2f} dan isipadu tangki air = {V:.2f}")

# JANGAN ubah kod di bawah
if __name__ == "__main__":
    main()