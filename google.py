from googlesearch import search
import random


search_query = input("Enter your search query: ")
search_results = list(search(search_query, num_results=10, lang="en"))


random_link = random.choice(search_results)


print(random_link)
