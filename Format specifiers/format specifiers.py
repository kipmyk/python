# format specifiers -- {:<flags>} format a value based on what
# flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 3141.59265
price2 = -987.65
price3 = 12.34

# 1. Decimal Places
print("Add decimal formats")
print(f"Price 1 is: ksh.{price1:.2f}")
print(f"Price 2 is: ksh.{price2:.2f}")
print(f"Price 3 is: ksh.{price3:.2f}")

# 2. Allocate space
print("# Allocate space with fixed width")
print(f"Price 1 is: ksh.{price1:10}")
print(f"Price 2 is: ksh.{price2:10}")
print(f"Price 3 is: ksh.{price3:10}")

# 3. Zero-padding
print("# Zero-padding")
print(f"Price 1 is: ksh.{price1:010.2f}")
print(f"Price 2 is: ksh.{price2:010.2f}")
print(f"Price 3 is: ksh.{price3:010.2f}")

# 4. Left-align
print("# Left-align")
print(f"Price 1 is: ksh.{price1:<10.2f}")
print(f"Price 2 is: ksh.{price2:<10.2f}")
print(f"Price 3 is: ksh.{price3:<10.2f}")

# 5. Right-align
print("# Right-align")
print(f"Price 1 is: ksh.{price1:>10.2f}")
print(f"Price 2 is: ksh.{price2:>10.2f}")
print(f"Price 3 is: ksh.{price3:>10.2f}")

# 6. Center-align
print("# Center-align")
print(f"Price 1 is: ksh.{price1:^10.2f}")
print(f"Price 2 is: ksh.{price2:^10.2f}")
print(f"Price 3 is: ksh.{price3:^10.2f}")

# 7. Show + for positive numbers
print("# Show plus sign for positive values")
print(f"Price 1 is: ksh.{price1:+.2f}")
print(f"Price 2 is: ksh.{price2:+.2f}")
print(f"Price 3 is: ksh.{price3:+.2f}")

# 8. Add space before positive numbers
print("# Space before positive values")
print(f"Price 1 is: ksh.{price1: .2f}")
print(f"Price 2 is: ksh.{price2: .2f}")
print(f"Price 3 is: ksh.{price3: .2f}")

# 9. Place sign on the far left (useful in tables)
print("# Sign to leftmost position")
print(f"Price 1 is: ksh.{price1:=+10.2f}")
print(f"Price 2 is: ksh.{price2:=+10.2f}")
print(f"Price 3 is: ksh.{price3:=+10.2f}")

# 10. Use comma separator
print("# Use comma as thousand separator")
print(f"Price 1 is: ksh.{price1:,.2f}")
print(f"Price 2 is: ksh.{price2:,.2f}")
print(f"Price 3 is: ksh.{price3:,.2f}")

