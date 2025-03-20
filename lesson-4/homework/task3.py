txt = "abcabcdabcdeabcdefabcdefg"
result = []
done = set("aeiou")

i = 0
while i < len(txt):
    result.append(txt[i])

    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        if txt[i] in done:
            pass
        else:
            result.append("_")
            done.add(txt[i])

    i += 1

print("".join(result))
