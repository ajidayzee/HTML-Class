friends = []
new_friend = None
print()
while new_friend != "end" :
    new_friend = input("Type a friend's name: ") 
    if new_friend != "end":
        friends.append(new_friend)

print()
print("\nYour friend's are: ")   
for friend in friends:
    #print(*friend, sep='') This code does the same thing as the one below 
    print(friend)    