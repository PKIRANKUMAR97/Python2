# Create a list of colors.
# Write a script that checks if "green" is in the list;
# if it is, replace it with "emerald".
#     If not, change the first and last elements to "black".

colors=['red','greens','blue']
if "green" in colors:
    index=colors.index("green")
    colors[index]="emerald"
else :
    colors[0]="black"
    colors[-1]="black"
print(colors)


