# Crawlee Python: Modern Web Scraping & Browser Automation

[Crawlee Python](https://github.com/apify/crawlee-python) is a powerful, open-source library for web scraping, crawling, and browser automation. Built by Apify, it provides a unified, asyncio-based interface for extracting data from the web—supporting both HTTP and headless browser workflows (Playwright, BeautifulSoup, Parsel, and more).

## 🚀 Key Features
- **Unified API** for HTTP and browser-based crawling (switch between Playwright, BeautifulSoup, Parsel, etc.)
- **Asyncio-native**: High performance, modern Python, type hints throughout
- **Automatic proxy rotation** and session management
- **Persistent queues** and robust error handling
- **Pluggable storage**: Save tabular data, files, and more
- **Production-ready**: Retry logic, stealth mode, scaling, and cloud deployment (Apify platform)
- **Rich example gallery** and CLI for fast project setup

## 🧑‍💻 Use Cases
- Data extraction for AI, LLMs, RAG, and GPT workflows
- Scraping HTML, PDFs, images, and more
- Automating browser tasks (form filling, screenshotting, navigation)
- Building robust, scalable crawlers for research or production

## 📦 Installation
```bash
python -m pip install 'crawlee[all]'
playwright install
```
Or use the CLI for quick templates:
```bash
pipx run 'crawlee[cli]' create my-crawler
```

## 📚 Official Resources
- [GitHub Repository](https://github.com/apify/crawlee-python)
- [Official Documentation & Guides](https://crawlee.dev/python/)
- [PyPI Package](https://pypi.org/project/crawlee/)
- [Example Gallery](https://crawlee.dev/python/docs/examples)
- [API Reference](https://crawlee.dev/python/api)
- [Apify SDK for Python (Actors)](https://docs.apify.com/sdk/python/)
- [Discord Community](https://discord.gg/jyEM2PRvMU)

## 🆚 Crawlee vs. Scrapy
- **Asyncio-native** (Crawlee) vs. Twisted (Scrapy)
- **Unified API** for HTTP & browser crawling (Crawlee)
- **Modern Python, type hints, and easy integration**
- **State persistence** and robust storage options

## 📝 Example: BeautifulSoupCrawler
```python
import asyncio
from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext

async def main() -> None:
    crawler = BeautifulSoupCrawler(max_requests_per_crawl=10)

    @crawler.router.default_handler
    async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
        context.log.info(f'Processing {context.request.url} ...')
        data = {
            'url': context.request.url,
            'title': context.soup.title.string if context.soup.title else None,
        }
        await context.push_data(data)
        await context.enqueue_links()

    await crawler.run(['https://crawlee.dev'])

if __name__ == '__main__':
    asyncio.run(main())
```

## 🔗 See Also
- [PlaywrightCrawler Example](https://crawlee.dev/python/docs/examples/playwright-crawler)
- [Adaptive Crawling](https://crawlee.dev/python/docs/examples/adaptive-playwright-crawler)
- [All Examples](https://crawlee.dev/python/docs/examples)

---

Crawlee is forever free and open source. For advanced cloud deployment, see the [Apify platform](https://apify.com/).

*Contributed to Digital Palace July 2025*.
