import urllib.request
from link_finder import *
from domain import *
from create_files import *


# Logic to crawl one page
def crawl_page(base_url, page_url, depth, crawled, queue, PROJECT_NAME):
    if page_url not in crawled:
        crawled.add(page_url)
        contents = str((urllib.request.urlopen(page_url)).read())
        create_crawled_files(crawled, contents, PROJECT_NAME)
        parser = LinkFinder(base_url, page_url)
        parser.feed(contents)
        put_links_in_queue(parser.links, queue, depth, base_url, crawled)


def create_crawled_files(crawled, contents, PROJECT_NAME):
    length = len(crawled)
    path = PROJECT_NAME + "/" + str(length) + ".txt"
    write_file(path, contents)


def put_links_in_queue(links, queue, depth, base_url, crawled):
    for link in links:
        if is_valid_link(link, base_url) and link not in queue and link not in crawled:
            queue.append([link, depth + 1])


def is_valid_link(link, base_url):
    base_sub_domain_name = get_sub_domain_name(base_url)
    path = get_path(link)
    if (link.startswith("https") or link.startswith("http")) and (get_sub_domain_name(link) == base_sub_domain_name) and ("Main_Page" not in path and ":" not in path):
        return True
    return False
