# fetchrss-api: Python Client Library for FetchRSS API

## Installation

From [Python Package Index](https://pypi.python.org/pypi/fetchrss-api):

```bash
pip install fetchrss-api
```

Directly from the Git repository on GitHub:

```bash
pip install git+https://github.com/Impacto-jor/fetchrss-api.git
```

or

```bash
git clone https://github.com/Impacto-jor/fetchrss-api.git
cd fetchrss-api
python setup.py install
```

Tested on Python 3.7.0 (you may run using 3.6 by installing the `dataclasses`
package).


## Usage

Learn by example:


```python
from fetchrss import FetchRSS

# Instantiate the object
api = FetchRSS(access_token="<super secret>")

# Create a new feed using URL only
feed = api.feed_create(url="https://some-url/")
print(f"Feed created: {feed}")

# Create a new feed using all parameters
feed = api.feed_create(
    url="https://some-url/",
    news_selector="<news selector>",
    title_selector="<title selector>",
    content_selector="<content selector>",
    pic_selector="[optional picture selector]",
    date_selector="[optional date selector]",
    author_selector="[optional author selector]",
    link_selector="[optional link selector]",
    pic_src_param="[optional picture source parameter]",
    date_format_param="[optional date format parameter]",
)
print(f"Feed created: {feed}")

# List all available feeds
for feed in api.feeds():
    print(feed)

# Get RSS entries for a specific feed
for entry in api.rss(feed):
    print(entry)
```
