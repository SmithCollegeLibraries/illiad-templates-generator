import re

source = "ILLiad_8.7.0.0_DefaultWebPages/css/main.css"
destination = "rendered-illiad-templates/css/main.css"

# Process CSS file
with open(source, errors="backslashreplace") as fp:
    with open(destination, 'w') as out_fp:
        for line in fp:
            modified_line = re.sub('(^[a-zA-z\.\#])', r'#illiad-content \1', line)
            out_fp.write(modified_line)
out_fp.close()
