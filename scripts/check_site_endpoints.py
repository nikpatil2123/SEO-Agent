#!/usr/bin/env python3
"""Optional read-only check for robots.txt and sitemap endpoints.

Requires: pip install requests
Usage: python scripts/check_site_endpoints.py https://example.com
Only run against a site you are authorized to assess. This makes two GET requests.
"""
import sys
from urllib.parse import urljoin, urlparse

try:
    import requests
except ImportError:
    raise SystemExit("Install dependency first: pip install requests")

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/check_site_endpoints.py https://example.com")
    base = sys.argv[1].rstrip("/") + "/"
    parsed = urlparse(base)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise SystemExit("Provide a valid http(s) website URL.")
    session = requests.Session()
    session.headers["User-Agent"] = "AgentSEO-Audit/1.0 (+authorized read-only assessment)"
    for path in ("robots.txt", "sitemap.xml"):
        url = urljoin(base, path)
        try:
            response = session.get(url, timeout=15, allow_redirects=True)
            print(f"\n{url}")
            print(f"Status: {response.status_code}")
            print(f"Final URL: {response.url}")
            print(f"Content-Type: {response.headers.get('Content-Type', 'unknown')}")
            print(f"Bytes: {len(response.content)}")
            if path == "robots.txt" and response.ok:
                print("Preview:")
                print(response.text[:1500])
        except requests.RequestException as exc:
            print(f"\n{url}\nERROR: {exc}")

if __name__ == "__main__":
    main()
