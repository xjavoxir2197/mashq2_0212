# 1 - misol
get_len = lambda s: len(s)
print(get_len("salom"))

# 2 - misol
check_num = lambda x: "musbat" if x > 0 else ("manfiy" if x < 0 else "nol")
print(check_num(5))
print(check_num(-3))
print(check_num(0))

# 3 - misol
area = lambda b, h: 0.5 * b * h
print(area(10, 6))

# 4 - misol
check = lambda x: "10 dan katta" if x > 10 else "10 dan katta emas"
print(check(15))
print(check(7))

# 5 - misol
check_a = lambda name: "bor" if "a" in name.lower() else "yo‘q"
print(check_a("Javoxir"))
print(check_a("Temur"))
