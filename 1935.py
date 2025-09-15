def canBeTypedWords(text: str, brokenLetters: str) -> int:
    words = text.split(" ")
    brokens = set(brokenLetters)
    cnt = 0
    for w in words:
        for c in w:
            if c in brokens:
                cnt += 1
                break
    return len(words)-cnt

print(canBeTypedWords("hello world","ad"))
print(canBeTypedWords("leet code","lt"))
print(canBeTypedWords("leet code","e"))
