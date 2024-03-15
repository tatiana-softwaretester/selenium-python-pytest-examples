import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("item, url", [
    ("Skagen Women Watch", "Skagen+Women+Watch"),
    ("Volkswagen Amarok", "Volkswagen+Amarok"),
    ("Banana Republic Dress", "Banana+Republic+Dress"),
    ("Math books", "Math+books")
])
@pytest.mark.regressiontest
def test_ebay_search_multiple_items(browser, item, url):
    browser.get("https://www.ebay.com/")
    assert "Electronics, Cars, Fashion, Collectibles & More | eBay" == browser.title
    assert "https://www.ebay.com/" == browser.current_url
    browser.find_element(By.ID, "gh-ac").send_keys(item + Keys.ENTER)
    assert item in browser.title
    assert url in browser.current_url