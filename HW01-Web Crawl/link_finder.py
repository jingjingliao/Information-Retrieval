import re


# Get all links from html page
def get_all_links(contents):
    all_links = set()
    pattern = '<a href="([^"]*)"'
    result = re.findall(pattern, contents)
    for link in result:
        if not link.startswith("http") and link.startswith("/wiki"):
            link = "https://en.wikipedia.org" + link
        if is_valid_links(link) and "Main_Page" not in link and len(link.split(":")) == 2:
            all_links.add(link)

    return all_links


# Check if the link format is valid
def is_valid_links(link):
    pattern = "[http, https].*en.wikipedia.org/wiki/.*"
    if re.match(pattern, link):
        return True
    else:
        return False
