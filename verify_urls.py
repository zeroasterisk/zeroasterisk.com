#!/usr/bin/env python3
"""
URL Verification Script for zeroasterisk.com
Tests all critical URLs to ensure legacy URL compatibility
"""

import requests
import sys
from urllib.parse import urljoin
from pathlib import Path
import json
import time

def test_url(base_url, path, description):
    """Test a single URL and return result"""
    url = urljoin(base_url, path)
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        if response.status_code == 200:
            print(f"✅ {description}: {url}")
            return True
        else:
            print(f"❌ {description}: {url} (Status: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ {description}: {url} (Error: {e})")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python verify_urls.py <base_url>")
        print("Example: python verify_urls.py https://zeroasterisk.com")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    print(f"🧪 Testing URLs for: {base_url}")
    print("=" * 60)
    
    failed = 0
    total = 0
    
    # Core navigation pages
    core_pages = [
        ("", "Homepage"),
        ("/posts/", "Tech Posts"),
        ("/personal/", "Personal Posts"), 
        ("/about/", "About Page"),
        ("/tags/", "Tags Index"),
        ("/search/", "Search Page"),
    ]
    
    print("📄 Testing Core Pages:")
    for path, desc in core_pages:
        total += 1
        if not test_url(base_url, path, desc):
            failed += 1
    
    # Sample legacy URLs (random selection from our migration)
    legacy_urls = [
        ("/2017/07/playing-with-elixir-is-just-fun/", "Elixir Post (2017)"),
        ("/2014/09/meteor-092rc1-with-cordova/", "Meteor Post (2014)"),
        ("/2006/04/pandora-radio-except-for-some-npr/", "Old Pandora Post (2006)"),
        ("/2008/12/obamas-27-year-old-speech-writter/", "Obama Post (2008)"),
        ("/2013/08/meteor-phonegapcordova-roundup-fall-2013/", "Meteor/Cordova Post (2013)"),
        ("/personal/2007/06/we-are-having-a-baby/", "Personal: Baby News (2007)"),
        ("/personal/2009/01/poppys-first-birthday/", "Personal: Birthday (2009)"),
        ("/personal/2005/07/kyoto-day-1/", "Personal: Japan Trip (2005)"),
    ]
    
    print("\\n🔗 Testing Legacy URLs:")
    for path, desc in legacy_urls:
        total += 1
        if not test_url(base_url, path, desc):
            failed += 1
    
    # Cross-posts from Google
    crosspost_urls = [
        ("/2026/08/agent-plugins-package-your-skills-tools-and-more/", "Google Developers Cross-post"),
        ("/2026/09/5-things-every-ai-engineer-should-know-about-agent-sandboxes/", "Google Cloud Cross-post"),
    ]
    
    print("\\n📰 Testing Cross-posts:")
    for path, desc in crosspost_urls:
        total += 1
        if not test_url(base_url, path, desc):
            failed += 1
    
    # Tag pages (sample)
    tag_urls = [
        ("/tags/elixir/", "Elixir Tag"),
        ("/tags/meteor/", "Meteor Tag"),
        ("/tags/ai/", "AI Tag"),
        ("/tags/2017/", "2017 Year Tag"),
        ("/tags/development/", "Development Tag"),
        ("/tags/personal/", "Personal Tag"),
    ]
    
    print("\\n🏷️ Testing Tag Pages:")
    for path, desc in tag_urls:
        total += 1
        if not test_url(base_url, path, desc):
            failed += 1
    
    # RSS and sitemap
    meta_urls = [
        ("/sitemap.xml", "Sitemap"),
        ("/index.xml", "RSS Feed"),
        ("/posts/index.xml", "Posts RSS"),
        ("/personal/index.xml", "Personal RSS"),
    ]
    
    print("\\n📡 Testing Meta URLs:")
    for path, desc in meta_urls:
        total += 1
        if not test_url(base_url, path, desc):
            failed += 1
    
    # Summary
    print("\\n" + "=" * 60)
    print(f"🎯 VERIFICATION RESULTS")
    print(f"Total URLs tested: {total}")
    print(f"Successful: {total - failed}")
    print(f"Failed: {failed}")
    
    if failed == 0:
        print("\\n✅ ALL TESTS PASSED! Site is ready for production.")
        return 0
    else:
        print(f"\\n❌ {failed} tests failed. Please check the URLs above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())