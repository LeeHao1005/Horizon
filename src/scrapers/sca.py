"""国密局 (State Cryptography Administration) scraper for Horizon.

Monitors the official SCA website (www.sca.gov.cn) for announcements,
standards, and policy updates related to commercial cryptography
(SM2/SM3/SM4/SM9, post-quantum research directions, etc.).
"""

import hashlib
import re
import logging
from datetime import datetime, timezone
from typing import Optional
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, ScaConfig

logger = logging.getLogger(__name__)

_BASE_URL = "https://www.sca.gov.cn"
_ANNOUNCEMENTS_URL = f"{_BASE_URL}/sca/xwdt/tzgg.shtml"
_NEWS_URL = f"{_BASE_URL}/sca/xwdt/"


class ScaScraper(BaseScraper):
    """Scraper for China's State Cryptography Administration announcements."""

    def __init__(self, config: ScaConfig, http_client: httpx.AsyncClient):
        super().__init__({}, http_client)
        self.sca_config = config

    async def fetch(self, since: datetime) -> list[ContentItem]:
        """Fetch SCA announcements since the given time.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched items
        """
        items = []
        items.extend(await self._fetch_page(self.sca_config.announcements_url or _ANNOUNCEMENTS_URL, since))

        # Sort by published date descending
        items.sort(key=lambda x: x.published_at, reverse=True)
        return items

    async def _fetch_page(
        self, url: str, since: datetime
    ) -> list[ContentItem]:
        """Fetch a single SCA page and extract article links."""
        items = []

        try:
            response = await self.client.get(url, follow_redirects=True, timeout=15.0)
            response.raise_for_status()
            html = response.text

            # Parse <li> blocks containing <a> title + <span> date
            li_pattern = re.compile(
                r"<li[^>]*>\s*"
                r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>\s*'
                r"<span[^>]*>\s*(\d{4}-\d{2}-\d{2})\s*</span>",
                re.DOTALL,
            )

            for match in li_pattern.finditer(html):
                href = match.group(1).strip()
                title = re.sub(r"<[^>]+>", "", match.group(2)).strip()
                date_str = match.group(3).strip()

                try:
                    pub_date = datetime.strptime(date_str, "%Y-%m-%d").replace(
                        tzinfo=timezone.utc
                    )
                except ValueError:
                    continue

                if pub_date < since:
                    continue

                # Build full URL
                if href.startswith("http"):
                    full_url = href
                else:
                    full_url = f"{_BASE_URL}{href}"

                # Generate an ID from the URL
                url_hash = hashlib.sha256(full_url.encode("utf-8")).hexdigest()[:16]

                # Try to fetch the article content
                content = await self._fetch_article_content(full_url)

                item = ContentItem(
                    id=self._generate_id("sca", "announcement", url_hash),
                    source_type=SourceType.SCA,
                    title=title,
                    url=full_url,
                    content=content,
                    author="国家密码管理局",
                    published_at=pub_date,
                    metadata={"category": "pqc"},
                )
                items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching SCA page %s: %s", url, e)
        except Exception as e:
            logger.warning("Error parsing SCA page %s: %s", url, e)

        return items

    async def _fetch_article_content(
        self, url: str
    ) -> Optional[str]:
        """Fetch and extract plain text from an SCA article page."""
        try:
            response = await self.client.get(url, follow_redirects=True, timeout=15.0)
            response.raise_for_status()
            html = response.text

            # Remove script/style blocks
            cleaned = re.sub(
                r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.DOTALL
            )
            cleaned = re.sub(r"<[^>]+>", " ", cleaned)
            cleaned = re.sub(r"&[a-z]+;", " ", cleaned)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()

            # Only keep if we got meaningful text
            if len(cleaned) > 100:
                return cleaned[:2000]  # Limit length

            return None

        except Exception as e:
            logger.debug("Could not fetch SCA article %s: %s", url, e)
            return None
