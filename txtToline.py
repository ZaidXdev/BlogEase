file = open("blog.html", "r")
text = file.read()
file.close()

raw = ""

last = ""

for i in text:
    if i == "\n":
        raw += "\\n"
    else:
        if last != " " and i != " ":
            raw += i
        last = i
        
header = ""
body = ""
footer = ""

print(raw)