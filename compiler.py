import data

title = data.title
topic = data.topic
banner_src = data.banner_src
logo_src = data.logo_src

def mdToHtml(text):
    stack = []
    htmlText = ""
    i = 0
    while i < len(text):
        try:
            if text[i] == "*" :
                if text[i + 1] == "*":
                    if text[i + 2] == "*":
                        if stack and stack[-1] == "***":
                            htmlText += "</i></b>"
                            stack.pop()
                        else:
                            htmlText += "<b><i>"
                            stack.append("***")
                        i += 2
                    else:
                        if stack and stack[-1] == "**":
                            htmlText += "</b>"
                            stack.pop()
                        else:
                            htmlText += "<b>"
                            stack.append("**")
                        i += 1
                else:
                    if stack and stack[-1] == "*":
                        htmlText += "</i>"
                        stack.pop()
                    else:
                        htmlText += "<i>"
                        stack.append("*")
            else:
                htmlText += text[i]
        except:
            htmlText += text[i]
        i += 1
    return htmlText

header = f'<!DOCTYPE html>\n<html lang="en">\n<head><meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>{title}</title>\n<link rel="icon" type="favicon.png" href="favicon.png">\n<link rel="stylesheet" href="style.css" />\n</head>\n<body bgcolor="white"><!-- <div class="background"></div> -->\n<div class="banner">\n<img src="{banner_src}" alt="" class="banner-img">\n</div\n<button id="scrollToTopBtn" title="Go to top">Top</button>\n<script src="script.js"></script>\n<div class="center">\n<div class="profile">\n<img class="logo" src="{logo_src}" alt="creator">\n<strong><b class="bald-text">{topic}</b></strong>\n</div>\n<hr class="solid-border">\n<br>'
body = f''
end = '\n</div>\n</body>\n</html>'

blog = open("blog.md", "r")
out = open("out.html", "w")

text = blog.read()

blogText = mdToHtml(text=text)

out.write(header)
out.write(body)
out.write(f"<p>{blogText}</p>")
out.write(end)

blog.close()
out.close()