# write a python program that accepts a sentence and print 
# vowels,spaces and consonents

sentence = input("Enter the sentence: ")

v = []
s = []
c = []

for ch in sentence:
    if ch in "aeiouAEIOU":
        v.append(ch)
    elif ch == " ":
        s.append(ch)
    elif ch.isalpha(): 
        c.append(ch)

print("Vowels are:", v)
print("Number of vowels:", len(v))

print("Spaces are:", s)
print("Number of spaces:", len(s))

print("Consonants are:", c)
print("Number of consonants:", len(c))
