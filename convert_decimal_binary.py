def decimal_to_binary(n: int) -> str:
    """Mengonversi bilangan desimal ke biner secara manual."""
    if n == 0:
        return "0"
    
    hasil = ""
    angka = abs(n)
    while angka > 0:
        sisa = angka % 2
        hasil = str(sisa) + hasil
        angka //= 2
        
    return f"-{hasil}" if n < 0 else hasil


def binary_to_decimal(b: str) -> int:
    """Mengonversi bilangan biner ke desimal secara manual."""
    b = b.strip()
    is_negatif = b.startswith("-")
    if is_negatif:
        b = b[1:]
        
    total = 0
    panjang = len(b)
    for i, char in enumerate(b):
        if char not in ("0", "1"):
            raise ValueError(f"Digit '{char}' bukan bilangan biner valid!")
        pangkat = panjang - 1 - i
        total += int(char) * (2 ** pangkat)
        
    return -total if is_negatif else total


decimal = 30

biner_builtin = bin(decimal)[2:]
biner_manual = decimal_to_binary(decimal)

print("=" * 45)
print("1. KONVERSI DESIMAL KE BINER")
print("=" * 45)
print(f"Nilai Desimal     : {decimal}")
print(f"Biner (Built-in)  : {biner_builtin}")
print(f"Biner (Manual)    : {biner_manual}")
print()


biner = biner_builtin

desimal_builtin = int(biner, 2)
desimal_manual = binary_to_decimal(biner)

print("=" * 45)
print("2. KONVERSI BINER KE DESIMAL")
print("=" * 45)
print(f"Nilai Biner       : {biner}")
print(f"Desimal (Built-in): {desimal_builtin}")
print(f"Desimal (Manual)  : {desimal_manual}")
print("=" * 45)

"""
Penjelasan Langkah Perhitungan (Trace / Langkah Manual):
---------------------------------------------------------
1. Desimal 30 ke Biner:
   30 / 2 = 15, sisa 0  (LSB - bit paling kanan)
   15 / 2 =  7, sisa 1
    7 / 2 =  3, sisa 1
    3 / 2 =  1, sisa 1
    1 / 2 =  0, sisa 1  (MSB - bit paling kiri)
   Dibaca dari bawah ke atas -> 11110

2. Biner 11110 ke Desimal:
   (1 * 2^4) + (1 * 2^3) + (1 * 2^2) + (1 * 2^1) + (0 * 2^0)
   = 16 + 8 + 4 + 2 + 0
   = 30
"""
