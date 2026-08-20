def calculate_love_score(name1, name2,):
    total_true = 0
    total_love = 0
    for character in (name1+name2).upper():
        if character in word1:
            total_true += 1
    print(total_true)

    for character in (name1+name2).upper():
        if character in word2:
            total_love += 1
    print(total_true)
    love_score = str(total_true)+str(total_love)
    print(f"love score = {love_score}")

word1 = "TRUE"
word2 = "LOVE"
calculate_love_score(name1="Kanye West", name2="Kim Kardashian")