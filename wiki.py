import wikipedia

subject = input('Enter keyword: ')
wiki = wikipedia.page(subject)

text = wiki.content
print(text)