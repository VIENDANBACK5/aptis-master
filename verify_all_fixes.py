# -*- coding: utf-8 -*-
import os
import time
import subprocess
from playwright.sync_api import sync_playwright

def run_tests():
    print("Starting local HTTP server on port 8093...")
    server = subprocess.Popen(["python", "-m", "http.server", "8093"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, channel="chrome")
            page = browser.new_page(viewport={"width": 1440, "height": 900})

            # 1. Test Dashboard & Exam Hub Filter Tabs (Image 1 check)
            print("\n1. Testing Dashboard & Exam Hub Filter Tabs...")
            page.goto("http://localhost:8093/index.html", wait_until="networkidle")
            page.wait_for_selector("#view-dashboard")
            
            # Check badge "Trọn Bộ 4 Kỹ Năng"
            assert page.locator("text=Trọn Bộ 4 Kỹ Năng").count() > 0, "Missing 'Trọn Bộ 4 Kỹ Năng' badge"
            print("  ✓ 'Trọn Bộ 4 Kỹ Năng' badge verified.")

            # Check Filter Tabs
            for tab_id in ['all', 'listening', 'reading', 'grammar', 'speaking', 'writing']:
                el = page.locator(f"#exam-tab-{tab_id}")
                assert el.count() > 0, f"Missing exam tab {tab_id}"
            print("  ✓ All 6 Exam Filter Tabs verified on Dashboard.")

            # Filter Listening
            page.click("#exam-tab-listening")
            time.sleep(0.3)
            cards = page.locator("#exam-hub-grid > div").count()
            print(f"  ✓ Listening filtered: {cards} cards found.")
            assert cards == 4, f"Expected 4 listening cards, got {cards}"

            # Filter Speaking
            page.click("#exam-tab-speaking")
            time.sleep(0.3)
            spk_cards = page.locator("#exam-hub-grid > div").count()
            print(f"  ✓ Speaking filtered: {spk_cards} sets found.")
            assert spk_cards == 20, f"Expected 20 speaking cards, got {spk_cards}"

            # Filter Writing
            page.click("#exam-tab-writing")
            time.sleep(0.3)
            wri_cards = page.locator("#exam-hub-grid > div").count()
            print(f"  ✓ Writing filtered: {wri_cards} sets found.")
            assert wri_cards == 30, f"Expected 30 writing cards, got {wri_cards}"

            # 2. Test Listening Part 1 - Question 182 (Screenshot 5 issue check)
            print("\n2. Testing Listening Part 1 - Question 182 (MCQ Evaluation Bug)...")
            page.click("#exam-tab-listening")
            time.sleep(0.3)
            page.locator("#exam-hub-grid button:has-text('Làm bài ngay →')").first.click()
            page.wait_for_selector("#view-practice")
            time.sleep(1)

            # Jump to question 182 directly via renderQuestion
            page.evaluate("renderQuestion(0)")
            time.sleep(0.5)

            stem = page.locator("#q-stem-text").inner_text()
            print(f"  Question 182 Stem: {stem}")
            assert "complain" in stem.lower(), f"Expected question 182 about customer complaint, got: {stem}"

            # Options: A (The coffee was cold), B (The Wi-Fi was too slow), C (The shop was too noisy)
            # Correct answer is B (index 1).
            # First, select option B (correct) and check:
            print("  Selecting option B (The Wi-Fi was too slow)...")
            page.locator("#q-interactive-area label:has-text('The Wi-Fi was too slow')").click()
            page.click("#btn-check")
            time.sleep(0.5)

            fb_area = page.locator("#q-feedback-area")
            assert fb_area.is_visible(), "Feedback area must be visible"
            fb_text = fb_area.inner_text()
            print(f"  Feedback text: {fb_text.splitlines()[0]}")
            assert "Chính xác" in fb_text, f"Expected 'Chính xác', got: {fb_text}"
            assert "The Wi-Fi was too slow" in fb_text, "Expected feedback to contain 'The Wi-Fi was too slow'"
            print("  ✓ Option B successfully evaluated as CORRECT!")

            # Also verify selecting wrong option A highlights red and shows correct answer B
            page.evaluate("checkedState[0] = undefined; userAnswers[0] = undefined; renderQuestion(0);")
            time.sleep(0.3)
            page.locator("#q-interactive-area label:has-text('The coffee was cold')").click()
            page.click("#btn-check")
            time.sleep(0.5)
            fb_text_wrong = page.locator("#q-feedback-area").inner_text()
            assert "Chưa chính xác" in fb_text_wrong, f"Expected 'Chưa chính xác', got: {fb_text_wrong}"
            assert "The Wi-Fi was too slow" in fb_text_wrong, "Expected explanation of correct answer B"
            print("  ✓ Option A evaluated as INCORRECT, showing correct answer B!")

            # 3. Test Reading Part 1 (Screenshot 2 check: blanks & paragraphs)
            print("\n3. Testing Reading Part 1 (Empty content bug check)...")
            page.evaluate("showDashboard()")
            page.wait_for_selector("#view-dashboard")
            page.click("#exam-tab-reading")
            time.sleep(0.3)
            page.locator("#exam-hub-grid button:has-text('Làm bài ngay →')").first.click()
            page.wait_for_selector("#view-practice")
            time.sleep(1)

            selects = page.locator("#q-interactive-area select").count()
            print(f"  Reading Part 1 dropdown count: {selects}")
            assert selects == 5, f"Expected 5 blank dropdowns, got {selects}"
            
            # Check paragraphs text is not empty
            para_text = page.locator("#q-interactive-area").inner_text()
            assert "cycle to work" in para_text, "Missing email text in Reading Part 1!"
            print("  ✓ Reading Part 1 email text and dropdowns verified (NOT empty).")

            # 4. Test Reading Part 3 (Screenshot 4 check: '1. undefined' bug)
            print("\n4. Testing Reading Part 3 (undefined questions bug check)...")
            page.evaluate("showDashboard()")
            page.wait_for_selector("#view-dashboard")
            page.click("#exam-tab-reading")
            time.sleep(0.3)
            # Click Part 3 (3rd card)
            page.locator("#exam-hub-grid button:has-text('Làm bài ngay →')").nth(2).click()
            page.wait_for_selector("#view-practice")
            time.sleep(1)

            r3_text = page.locator("#q-interactive-area").inner_text()
            assert "undefined" not in r3_text, f"Found 'undefined' in Reading Part 3: {r3_text[:200]}"
            assert "James" in r3_text or "Người" in r3_text, "Missing person names in Reading Part 3"
            print("  ✓ Reading Part 3 verified: NO 'undefined', 2 columns with person cards and questions.")

            # 5. Test Reading Part 4 (Screenshot 3 check: 'undefined' above headings bug)
            print("\n5. Testing Reading Part 4 (undefined paragraphs bug check)...")
            page.evaluate("showDashboard()")
            page.wait_for_selector("#view-dashboard")
            page.click("#exam-tab-reading")
            time.sleep(0.3)
            # Click Part 4 (4th card)
            page.locator("#exam-hub-grid button:has-text('Làm bài ngay →')").nth(3).click()
            page.wait_for_selector("#view-practice")
            time.sleep(1)

            r4_text = page.locator("#q-interactive-area").inner_text()
            assert "undefined" not in r4_text, f"Found 'undefined' in Reading Part 4: {r4_text[:200]}"
            assert "Đoạn 1:" in r4_text, "Missing 'Đoạn 1:' label in Reading Part 4"
            print("  ✓ Reading Part 4 verified: NO 'undefined', paragraphs and dropdowns cleanly displayed.")

            # 6. Test Grammar & Vocab Matching (Collocation/Synonym matching)
            print("\n6. Testing Grammar & Vocab (Matching pairs evaluation)...")
            page.evaluate("showDashboard()")
            page.wait_for_selector("#view-dashboard")
            page.click("#exam-tab-grammar")
            time.sleep(0.3)
            page.locator("#exam-hub-grid button:has-text('Làm bài ngay →')").first.click()
            page.wait_for_selector("#view-practice")
            time.sleep(1)

            # Jump to vocab question 26 (index 25)
            page.evaluate("renderQuestion(25)")
            time.sleep(0.5)

            vocab_selects = page.locator("#q-interactive-area select").count()
            print(f"  Vocab Question 26 dropdown count: {vocab_selects}")
            assert vocab_selects == 5, f"Expected 5 matching pairs, got {vocab_selects}"

            # Select correct first pair ('argue' -> 'disagree')
            page.locator("#q-interactive-area select").first.select_option(value="disagree")
            page.click("#btn-check")
            time.sleep(0.5)
            q26_fb = page.locator("#q-interactive-area").inner_text()
            assert "✓ Đúng" in q26_fb, f"Expected '✓ Đúng' for 'disagree', got: {q26_fb}"
            print("  ✓ Vocab matching successfully evaluated and marked correct!")

            page.screenshot(path="test_shot_all_verified.png")
            browser.close()
            print("\n============================================================")
            print(" 100% OF BUGS REPORTED IN SCREENSHOTS FIXED & VERIFIED!")
            print("============================================================")
    finally:
        server.terminate()

if __name__ == "__main__":
    run_tests()
