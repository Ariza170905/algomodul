def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / power(base, -exponent)
base_number = float(input("Masukkan angka : "))
power_number = int(input("Masukkan pangkat : "))
hasil = power(base_number, power_number)
print(f"Hasil {base_number} pangkat {power_number} adalah: {hasil}")
