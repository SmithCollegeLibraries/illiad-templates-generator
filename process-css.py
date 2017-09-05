import re

# Process CSS file
with open('main.css', errors="backslashreplace") as fp:
    for line in fp:
        print(re.sub('(^[a-zA-z\.\#])', r'#illiad-content \1', line))
