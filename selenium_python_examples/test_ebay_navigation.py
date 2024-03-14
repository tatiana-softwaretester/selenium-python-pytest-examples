import pytest


@pytest.mark.smoketest2
def test_ebay_navigation(browser):
    browser.get("http://www.ebay.com")
    assert browser.title == "Electronics, Cars, Fashion, Collectibles & More | eBay"