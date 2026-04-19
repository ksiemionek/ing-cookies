from playwright.sync_api import Page, expect

def test_cookies(page: Page):
    page.goto("https://www.ing.pl")
    
    page.get_by_role("button", name="Dostosuj").click()
    page.get_by_role("switch", name="Cookies analityczne").click()
    accept_btn = page.get_by_role("button", name="Zaakceptuj zaznaczone")
    accept_btn.click()

    expect(accept_btn).to_be_hidden()
    
    cookies = page.context.cookies()
    cookie_names = [c['name'] for c in cookies]
    
    assert 'cookiePolicyGDPR' in cookie_names, "cookiePolicyGDPR not found"
    assert 'cookiePolicyGDPR__details' in cookie_names, "cookiePolicyGDPR__details not found"

    cookie_gdpr = next((c for c in cookies if c['name'] == 'cookiePolicyGDPR'), None)

    assert cookie_gdpr is not None, "cookiePolicyGDPR not found"
    assert cookie_gdpr['value'] == '3', "cookiePolicyGDPR value is not 3"
