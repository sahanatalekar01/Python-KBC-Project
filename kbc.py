questions = [
["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", 4],

["Who created Python?", "Dennis Ritchie", "Guido van Rossum",
 "James Gosling", "Bjarne Stroustrup", 2],

["What does HTML stand for?", "Hyper Text Markup Language",
 "Hyper Tech Modern Language", "Home Tool Markup Language",
 "Hyper Transfer Markup Language", 1],

["Which company developed Python?", "Microsoft", "Apple", "Python Software Foundation", "Google", 3],

["What does CPU stand for?", "Central Processing Unit",
 "Computer Processing Unit", "Central Program Unit",
 "Computer Program Unit", 1]

]

levels = [1000, 2000, 3000, 5000, 10000]

money = 0

print("=" * 50)
print("🎮 WELCOME TO KBC QUIZ GAME 🎮")
print("=" * 50)

for i in range(len(questions)):
q = questions[i]

print(f"\n🏆 Question for Rs.{levels[i]}")
print(q[0])

print(f"1. {q[1]}")
print(f"2. {q[2]}")
print(f"3. {q[3]}")
print(f"4. {q[4]}")

try:
    answer = int(input("\nEnter your answer (1-4): "))
except ValueError:
    print("❌ Invalid Input!")
    break

if answer == q[5]:
    money = levels[i]
    print(f"✅ Correct! You won Rs.{money}")
else:
    print("❌ Wrong Answer!")
    print(f"✅ Correct option was: {q[5]}")
    break

print("\n" + "=" * 50)
print(f"🏆 Total Prize Money Won: Rs.{money}")
print("🙏 Thank You For Playing KBC!")
print("=" * 50)