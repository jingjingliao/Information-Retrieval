import time
from collections import deque
from create_files import *
from spider import *


PROJECT_NAME = "Wikipedia_Project"
HOMEPAGE = 'https://en.wikipedia.org/wiki/Stephen_Robertson_(computer_scientist)'
queue = deque()
crawled = set()
NUM_OF_PAGES = 1000
MAX_DEPTH = 5


# Main function run the crawler
def run_crawler(seedUrl, numPages):
    create_project_dir(PROJECT_NAME)
    queue.append([seedUrl, 1])
    count = 1
    while queue and count <= numPages:
        url, depth = queue.popleft()
        if depth == MAX_DEPTH:
            break
        else:
            crawl_page(HOMEPAGE, url, depth, crawled, queue, PROJECT_NAME)
            count += 1
            time.sleep(1)


run_crawler(HOMEPAGE, NUM_OF_PAGES)
