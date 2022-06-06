from asyncio.base_futures import _FINISHED
import string, random, os, time
alphabets = list(string.ascii_letters)
target, current = input('Type in a word (no symbols): '), ""
for n in target:
    letters = alphabets.copy()
    l = ""
    while l != n:
        l = random.choice(letters)
        letters.remove(l)
        print(current + l)
        time.sleep(0.02)
    current += l
print("Finished!", "The word was:", target)
