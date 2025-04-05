import wikipedia
from pyexpat import features

page_title = input("Enter page title: ")
while page_title:
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
    except wikipedia.PageError:
        print(f'Page id "{page_title}" does not match any pages. Try another id!')
    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print("(BeautifulSoup warning)")
        print(e.options)
    else:
        print(wikipedia.summary(page))
        print(page.url)
    page_title = input("\nEnter page title: ")

print("Thank you.")
