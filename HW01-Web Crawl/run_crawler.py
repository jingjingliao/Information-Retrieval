import time
from collections import deque
from create_files import *
from spider import *


PROJECT_NAME = "Wikipedia_Project"
HOMEPAGE = 'https://en.wikipedia.org/wiki/Stephen_Robertson_(computer_scientist)'
queue = deque()
bytes_size_lists = []
crawled = []
NUM_OF_PAGES = 1000
MAX_DEPTH = 5
crawled_max_depth = 1


# Main function run the crawler
def run_crawler(seedUrl, numPages):
    create_project_dir(PROJECT_NAME)
    queue.append([seedUrl, 1])

    while queue and len(crawled) < numPages:
        url, depth = queue.popleft()
        if depth == MAX_DEPTH:
            crawled_max_depth = MAX_DEPTH
            break
        else:
            crawl_page(HOMEPAGE, url, depth, crawled,
                       queue, PROJECT_NAME, bytes_size_lists)

            time.sleep(1)
        crawled_max_depth = depth
    create_crawled_files()
    create_statics_files(crawled_max_depth)


def create_crawled_files():
    path = PROJECT_NAME + "/URLsCrawled.txt"
    for link in crawled:
        append_to_file(path, link)


def create_statics_files(crawled_max_depth):
    max_bytes = "Maximum size: {} bytes".format(str(max(bytes_size_lists)))
    min_bytes = "Minimum size: {} bytes".format(str(min(bytes_size_lists)))
    average_bytes = str(sum(bytes_size_lists) // len(bytes_size_lists))
    averate_bytes_string = "Average size: {} bytes".format(average_bytes)
    depth_reach = "Mazimum depth reach: " + str(crawled_max_depth)

    path = PROJECT_NAME + "/stats.txt"
    for data in [max_bytes, min_bytes, averate_bytes_string, depth_reach]:
        append_to_file(path, data)


run_crawler(HOMEPAGE, NUM_OF_PAGES)
