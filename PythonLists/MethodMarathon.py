# Write a function that takes a list and:
# Counts how many times the number 5 appears (.count()).
# Finds the index of the first string "Target" (.index()).
# Reverses the list in place (.reverse()).

def funMM(l):
    count_no_of_fives=l.count(5)
    print(f"count of total fives in list is {count_no_of_fives}")
    try:

        target_index=l.index("Target")
        print(f"first index  of target  is {target_index}")

    except ValueError:
        print("target is not in list")
    l.reverse()
    print(f"reverse list is {l}")

mylist = [1,2,3,4,5,5,6,5,6,5]
funMM(mylist)