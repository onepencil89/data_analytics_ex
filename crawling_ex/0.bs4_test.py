html_doc = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ; and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)

# print(soup.title)
# # <title>The Dormouse's story</title>

# print(soup.title.name)
# # u'title'

# print(soup.select_one('title'))

# print(soup.title.name)
# print(soup.title.parent.name)  # head
# print(soup.p)
# print(soup.a)
# print(soup.p['class'])

# print(soup.select_one('p'))  ㅌ

# p태그 모두
e_eles = soup.select('p')

for p in e_eles:
    print(p)
    # print(p.get_text().strip())
    print('-'*30)