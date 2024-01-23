while True :
    text = input()
    if text == "#":
        break
    else:
        ans = 0
        ans += text.count("a")
        ans += text.count("i")
        ans += text.count("e")
        ans += text.count("o")
        ans += text.count("u")

        ans += text.count("A")
        ans += text.count("E")
        ans += text.count("I")
        ans += text.count("O")
        ans += text.count("U")
        print(ans)