import data

title = data.title
topic = data.topic
banner_src = data.banner_src

header = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>{title}</title>\n<link rel="icon" type="favicon.png" href="favicon.png">\n<link rel="stylesheet" href="style.css" />\n</head>\n'
body = f'<body bgcolor="white">\n<div class="banner">\n<img src="{banner_src}" alt="" class="banner-img">\n</div>\n<div class="center">\n<b class="bald-text">{topic}</b>\n<hr class="solid-border">\n<br>\n'
end = '\n</div>\n</body>\n</html>'

blog = open("blog.md", "r")
out = open("out.html", "w")

text = blog.read()
blogText = ""

stack = []

i = 0
while i < len(text):
    try:
        if text[i] == "*" :
            if text[i + 1] == "*":
                if text[i + 2] == "*":
                    if stack and stack[-1] == "***":
                        blogText += "</i></b>"
                        stack.pop()
                    else:
                        blogText += "<b><i>"
                        stack.append("***")
                    i += 2
                else:
                    if stack and stack[-1] == "**":
                        blogText += "</b>"
                        stack.pop()
                    else:
                        blogText += "<b>"
                        stack.append("**")
                    i += 1
            else:
                if stack and stack[-1] == "*":
                    blogText += "</i>"
                    stack.pop()
                else:
                    blogText += "<i>"
                    stack.append("*")
        else:
            blogText += text[i]
    except:
        blogText += text[i]
    i += 1

out.write(header)
out.write(body)
out.write(f"<p>{blogText}</p>")
out.write(end)

blog.close()
out.close()