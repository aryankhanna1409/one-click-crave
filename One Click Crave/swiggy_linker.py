import urllib.parse

def make_links(restaurant, item):
    query = f"{restaurant} {item} site:swiggy.com"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    return f"<a href='{url}' target='_blank'>Find {item} on Swiggy</a>"
