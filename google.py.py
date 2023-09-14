from googlesearch import search
import random

# پرسش از کاربر
search_query = input("Enter your search query: ")

# جستجو در گوگل
search_results = list(search(search_query, num_results=10, lang="en"))

# انتخاب تصادفی یک لینک از نتایج جستجو
random_link = random.choice(search_results)

# چاپ لینک مقاله
print(random_link)