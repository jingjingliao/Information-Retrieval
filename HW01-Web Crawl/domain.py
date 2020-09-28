from urllib.parse import urlparse


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    return urlparse(url).netloc


def get_path(url):
    return urlparse(url).path
