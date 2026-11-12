import os
import glob
import json
from lxml import html

INSTR_DIR = r"d:\CODE\Aptis\data\instructions"
PROCESSED_INSTR = r"d:\CODE\Aptis\data\all_instructions.json"

guides = []
for fpath in glob.glob(os.path.join(INSTR_DIR, "*.html")):
    fname = os.path.basename(fpath)
    if fname == "index.html":
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    tree = html.fromstring(content)
    
    # Title
    h1 = tree.xpath('//h1//text()')
    title = h1[0].strip() if h1 else fname.replace('instructions_', '').replace('.html', '').replace('-', ' ').title()
    
    # Article body content
    article = tree.xpath('//article | //main | //div[contains(@class, "prose")]')
    if article:
        body_html = html.tostring(article[0], encoding='utf-8').decode('utf-8')
    else:
        body_html = content
        
    slug = fname.replace('instructions_', '').replace('.html', '')
    guides.append({
        "slug": slug,
        "title": title,
        "content_html": body_html
    })

with open(PROCESSED_INSTR, "w", encoding="utf-8") as f:
    json.dump(guides, f, ensure_ascii=False, indent=2)

print(f"Processed {len(guides)} instruction guides!")
for g in guides:
    print(f"  - {g['title']}")

