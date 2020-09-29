import urllib.request
from link_finder import *
from create_files import *
import sys


# Logic to crawl one page
def crawl_page(base_url, page_url, depth, crawled, queue, PROJECT_NAME, bytes_size_lists):
    if page_url not in crawled:
        crawled.append(page_url)
        total_bytes = urllib.request.urlopen(page_url).read()
        bytes_size = sys.getsizeof(total_bytes)
        bytes_size_lists.append(bytes_size)
        contents = str(total_bytes)
        create_crawled_files(crawled, contents, PROJECT_NAME)
        all_links = get_all_links(contents)
        put_links_in_queue(all_links, queue, depth, base_url, crawled)


def create_crawled_files(crawled, contents, PROJECT_NAME):
    length = len(crawled)
    path = PROJECT_NAME + "/" + str(length) + ".txt"
    write_file(path, contents)


def put_links_in_queue(links, queue, depth, base_url, crawled):
    for link in links:
        if link not in queue and link not in crawled:
            queue.append([link, depth + 1])
