# Make your strings more nerdy:
# Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1
#
# e.g. "Fundamentals" --> "Fund4m3nt41s"
#
def nerdify(txt):
    new_txt = ''
    for char in txt:
        if char.lower() == 'a':
            new_txt += '4'
        elif char.lower() == 'e':
            new_txt += '3'
        elif char == 'l':
            new_txt += '1'
        else:
            new_txt += char
    print(new_txt)
    return new_txt

nerdify("Fundamentals") # => "Fund4m3nt41s"
nerdify("Seven") # => "S3v3n"
nerdify("Los Angeles") # => "Los 4ng313s"
nerdify("Seoijselawuue") # => "S3oijs314wuu3"
