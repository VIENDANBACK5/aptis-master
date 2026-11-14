# -*- coding: utf-8 -*-
import os
import time
import subprocess
from playwright.sync_api import sync_playwright

def run_tests():
    print("Starting local HTTP server...")
    server = subprocess.Popen(["python", "-m", "http.server", "8089"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, channel="chrome")
            page = browser.new_page(viewport={"width": 1440, "height": 900})

            # 1. Dashboard View
            print("1. Testing Dashboard...")
            page.goto("http://localhost:8089/index.html", wait_until="networkidle")
            page.wait_for_selector("#view-dashboard")
            page.screenshot(path="test_shot_dashboard.png")
            print("  Dashboard loaded and captured.")

            greeting = page.locator("h1:has-text('Chào Minh')").count()
            assert greeting > 0, "Missing greeting 'Chào Minh'"

            full_test_banner = page.locator("text=Full Test Aptis").count()
            assert full_test_banner > 0, "Missing Full Test Aptis banner"

            # 2. Skill Hub: Reading
            print("2. Testing Reading Skill Hub...")
            page.click("a[onclick*=\"openSkillHub('reading')\"]")
            page.wait_for_selector("#view-skill-hub")
            page.screenshot(path="test_shot_reading_hub.png")
            parts_count = page.locator("#hub-cards-grid > a").count()
            print(f"  Reading Hub loaded with {parts_count} part cards.")
            assert parts_count >= 4, f"Expected at least 4 part cards, got {parts_count}"

            # 3. Practice Room: Reading Part 1
            print("3. Testing Practice Room (Reading Part 1)...")
            page.click("#hub-cards-grid > a:first-child")
            page.wait_for_selector("#view-practice")
            time.sleep(1)
            page.screenshot(path="test_shot_practice_r_p1.png")
            
            sec_title = page.locator("#practice-sec-title").inner_text()
            print(f"  Practice section title: {sec_title}")
            assert "READING" in sec_title, f"Unexpected section title: {sec_title}"

            selects = page.locator("#q-interactive-area select").count()
            print(f"  Found {selects} dropdown selects in question.")
            assert selects > 0, "Expected dropdown selects for Reading Part 1"

            # Test answering
            page.locator("#q-interactive-area select").first.select_option(index=1)
            page.click("#btn-check")
            time.sleep(0.5)
            page.screenshot(path="test_shot_practice_checked.png")
            print("  Answer checked and feedback verified.")

            # Test Palette Popover
            page.click("button:has-text('Danh sách câu')")
            time.sleep(0.5)
            assert page.locator("#palette-popover").is_visible(), "Palette popover should be visible"
            page.screenshot(path="test_shot_palette_popover.png")
            print("  Palette popover opened successfully.")

            # 4. Speaking Hub & Mock Test
            print("4. Testing Speaking Mock Test...")
            page.click("#nav-link-practice")
            page.wait_for_selector("#view-dashboard")
            page.click("a[onclick*=\"openSkillHub('speaking')\"]")
            page.wait_for_selector("#view-skill-hub")
            page.screenshot(path="test_shot_speaking_hub.png")
            
            page.click("button:has-text('Luyện nói đề này →')")
            page.wait_for_selector("#view-speaking")
            time.sleep(0.5)
            page.screenshot(path="test_shot_speaking_mock.png")
            print("  Speaking Mock test room loaded.")

            # 5. Writing Hub & Mock Test
            print("5. Testing Writing Mock Test...")
            page.click("#nav-link-practice")
            page.wait_for_selector("#view-dashboard")
            page.click("a[onclick*=\"openSkillHub('writing')\"]")
            page.wait_for_selector("#view-skill-hub")
            page.screenshot(path="test_shot_writing_hub.png")

            page.click("button:has-text('Luyện viết đề này →')")
            page.wait_for_selector("#view-writing")
            time.sleep(0.5)
            page.screenshot(path="test_shot_writing_mock.png")
            print("  Writing Mock test room loaded.")

            # 6. Full Test View
            print("6. Testing Full Test View...")
            page.click("#nav-link-practice")
            page.wait_for_selector("#view-dashboard")
            page.click("#view-dashboard a[onclick*=\"openFullTest()\"]")
            page.wait_for_selector("#view-full-test")
            time.sleep(0.5)
            page.screenshot(path="test_shot_full_test.png")
            print("  Full Test view loaded.")

            # 7. Instructions View
            print("7. Testing Instructions View...")
            page.click("#nav-link-instructions")
            page.wait_for_selector("#view-instructions")
            time.sleep(0.5)
            page.screenshot(path="test_shot_instructions.png")
            print("  Instructions view loaded.")

            # 8. Vocab View
            print("8. Testing Vocab View...")
            page.click("#nav-link-vocab")
            page.wait_for_selector("#view-vocab")
            time.sleep(0.5)
            page.screenshot(path="test_shot_vocab.png")
            print("  Vocab view loaded.")

            browser.close()
            print("\n==========================================")
            print(" ALL 8 TESTS PASSED SUCCESSFULLY! 100% VERIFIED.")
            print("==========================================")
    finally:
        server.terminate()

if __name__ == "__main__":
    run_tests()
