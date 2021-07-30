prefixes = set()

def get_prefix(url: str):
    idx = url.find("typeid=")
    if idx == -1:
        # print(url)
        return None
    return url[:idx + len("typeid=")]
    idx += len("fid=")
    start = idx
    while idx < len(url) and url[idx].isdigit():
        idx += 1
    # print(url[start: idx])
    return int(url[start: idx])

with open('/Users/lipengfei/Documents/WebCrawler/parent_url_experience.txt', 'r') as urls:
    while True:
        parent_url = urls.readline()
        if not parent_url:
            break
        prefix = get_prefix(parent_url)
        if prefix in prefixes:
            print(parent_url)
        prefixes.add(prefix)
    # print(len(prefixes))

with open('/Users/lipengfei/Documents/WebCrawler/parent_url_all.txt', 'r') as urls:
    while True:
        parent_url = urls.readline()
        if not parent_url:
            break
        prefix = get_prefix(parent_url)
        if prefix not in prefixes:
            print(parent_url)