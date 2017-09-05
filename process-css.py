#^[a-zA-z\.\#]
with open('main.css', errors="backslashreplace") as fp:
    for line in fp:
        print(line)
