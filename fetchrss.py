from dataclasses import dataclass
from urllib.parse import urljoin

import feedparser
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


@dataclass
class Feed:
    """FetchRSS Feed instance"""

    id: int
    rss_url: str
    target_url: str = ""
    title: str = ""


@dataclass
class Entry:
    author: str
    authors: str
    guidislink: str
    id: str
    link: str
    links: str
    media_content: str
    published: str
    published_parsed: str
    summary: str
    summary_detail: str
    title: str
    title_detail: str


class FetchRSS:

    """Main FetchRSS.com API client class"""

    base_uri = "https://fetchrss.com/api/v1/"

    def __init__(self, access_token, timeout=3, retries=3):
        self.__access_token = access_token
        self._session = requests.session()
        self.timeout = timeout

        adapter = HTTPAdapter(
            max_retries=Retry(total=retries, read=retries, connect=retries)
        )
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

    def _get(self, *args, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
        return self._session.get(*args, **kwargs)

    def feeds(self):
        """List created feeds (generator)"""

        params = {"auth": self.__access_token}
        response = self._get(urljoin(self.base_uri, "feed/list"), params=params)
        response_data = response.json()
        if not response_data["success"]:
            raise RuntimeError("Error while getting feed list")

        for result in response_data["feeds"]:
            yield Feed(**result)

    def feed_create(
        self,
        url,
        news_selector=None,
        title_selector=None,
        content_selector=None,
        pic_selector=None,
        date_selector=None,
        author_selector=None,
        link_selector=None,
        pic_src_param=None,
        date_format_param=None,
    ):
        """Create a new feed"""

        # TODO: check if feed already exists
        params = {"auth": self.__access_token, "url": url}
        if news_selector:
            params.update(
                {
                    "news_selector": news_selector,
                    "title_selector": title_selector,
                    "content_selector": content_selector,
                    "pic_selector": pic_selector,
                    "date_selector": date_selector,
                    "author_selector": author_selector,
                    "link_selector": link_selector,
                    "pic_src_param": pic_src_param,
                    "date_format_param": date_format_param,
                }
            )

        response = self._get(urljoin(self.base_uri, "feed/create"), params=params)
        response_data = response.json()
        if not response_data["success"]:
            raise ValueError("Error while creating feed")
        return Feed(
            id=response_data["feed"]["id"],
            rss_url=response_data["feed"]["rss_url"],
            target_url=response_data["target_url"],
        )

    def feed_delete(self, feed):
        """Delete a specific `Feed` (by passing the object or its id)"""

        if isinstance(feed, Feed):
            feed_id = feed.id
        else:
            feed_id = feed

        params = {"auth": self.__access_token, "id": feed_id}
        response = self._get(urljoin(self.base_uri, "feed/delete"), params=params)
        response_data = response.json()
        if not response_data["success"]:
            raise ValueError("Error while creating feed")

    def rss(self, feed):
        """Fetch RSS items for a specific `Feed` object (generator)

        `feed` can be also a feed id or a RSS URL
        """

        feed_id, rss_url = None, None
        if isinstance(feed, Feed):
            feed_id, rss_url = feed.id, feed.rss_url
        elif not feed.startswith("http"):
            feed_id = feed
        else:
            rss_url = feed

        if not rss_url:
            for tmp_feed in self.feeds():
                if tmp_feed.id == feed_id:
                    rss_url = tmp_feed.rss_url
                    break
            if not rss_url:
                raise ValueError(f"Invalid feed id: {repr(feed)}")

        rss_feed = feedparser.parse(rss_url)
        for item in rss_feed["items"]:
            yield Entry(**item)
