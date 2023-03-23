# 1236, BFS | O(N) and O(N)
from collections import deque
from typing import List
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

def crawl(startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
    base = startUrl.split('/')[2]
    output = []
    visited = {startUrl}
    queue = deque([startUrl])

    while queue:
        url = queue.popleft()
        urls = htmlParser.getUrls(url)
        output.append(url)
        for u in urls:
            if u not in visited and u.split('/')[2] == base:
                visited.add(u)
                queue.append(u)

    return output