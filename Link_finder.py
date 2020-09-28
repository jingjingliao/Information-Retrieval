from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    # Using Regular Expression to ignore the following links
    # Main_Page url, or url with a colon
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href' and self.is_valid(value):
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def is_valid(self, url):
        if url.startswith("https://en.wikipedia.org/wiki") or url.startswith("http://en.wikipedia.org/wiki"):
            if "Main_Page" not in url and ":" not in url[30:]:
                return True
        return False

    def page_links(self):
        return self.links

    def error(self, message):
        pass
