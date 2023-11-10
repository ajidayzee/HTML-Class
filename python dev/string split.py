colors = "red green blue yellow"
print()

color_parts  = colors.split()
print()

print(colors)
print(color_parts)
print()
name = "Mondayz   "
clean_name = name.strip()
print(f"-----{name}-----")
print(f"-----{clean_name}-----")
print()
for color in color_parts:
    print(color)

print()    
second = color_parts[1]
print(second)

print()
color_parts = colors.split("e")
print(color_parts)