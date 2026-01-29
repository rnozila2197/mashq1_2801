# 11
matn = "index.html"
print(matn.endswith("html"))

# 12
def boshlanadimi(fayl_nomi):
    harflar = list(fayl_nomi)
    return harflar[:6] == list("python")

print(boshlanadimi("python.py"))

# 13
matn = "12345"
print(matn.isdigit())

# 14
matn = "salom"
print(matn.isalpha())

# 15
matn_harf = "user123"
print(matn_harf.isalnum())

# 16
matn = " "
print(matn.isspace())

# 17
matn = "SALOM"
print(matn.isupper())

# 18
matn = "salom"
print(matn.islower())

# 19
matn = "Python"
print(matn.center(30, "-"))

# 20
matn = "Python"
print(matn.ljust(25, "-"))
