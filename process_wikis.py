import os
import glob
import shutil
import re
from datetime import datetime

clippings_dir = r"d:\2ndBrain\Clippings"
wiki_dir = r"d:\2ndBrain\wiki"
raw_dir = r"d:\2ndBrain\raw"
index_file = os.path.join(wiki_dir, "مۇندەرىجە.md")
log_file = os.path.join(wiki_dir, "log.md")

files = glob.glob(os.path.join(clippings_dir, "*ئۇيغۇر تورى ئارخىپلىرى*.md"))

if not files:
    print("No files found.")
    exit()

added_links = []

# Keywords to auto-link to build relationships
keywords = [
    "قۇتادغۇ بىلىگ", "مەھمۇد قەشقەرى", "ئەلىشىر نەۋائى",
    "قاراخانىيلار", "تەكلىماكان", "مەدەنىيەت", "سەئىدىيە",
    "ئۇيغۇر", "قەشقەر", "خوتەن", "تارىخ", "تۈرك", "ئىلى"
]

def auto_link(text):
    for kw in keywords:
        text = text.replace(kw, f"[[{kw}]]")
    # Clean up potential double brackets
    text = text.replace('[[[[', '[[').replace(']]]]', ']]')
    return text

for file_path in files:
    filename = os.path.basename(file_path)
    title = filename.replace(" – ئۇيغۇر تورى ئارخىپلىرى", "").replace(".md", "")
    
    # Keep Uyghur characters
    wiki_title_clean = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '-')
    if not wiki_title_clean:
        wiki_title_clean = f"ماقالە-{datetime.now().timestamp()}"
        
    wiki_filename = f"بىرىكمە-{wiki_title_clean}.md"
    wiki_path = os.path.join(wiki_dir, wiki_filename)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Remove existing frontmatter
    content = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)
    
    # Auto link
    content = auto_link(content)
    
    yaml_header = f"""---
title: "{title}"
tags: [ئۇيغۇر-تورى-ئارخىپلىرى, تارىخ, مەدەنىيەت]
last_updated: {datetime.now().strftime('%Y-%m-%d')}
source: raw/{filename}
---

# {title}

"""
    
    with open(wiki_path, "w", encoding="utf-8") as f:
        f.write(yaml_header + content)
        
    raw_path = os.path.join(raw_dir, filename)
    shutil.move(file_path, raw_path)
    
    added_links.append(f"- [[{wiki_filename.replace('.md', '')}]]: {title}")

# Update index
with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

new_section = "## ئۇيغۇر تورى ئارخىپلىرى كۇللىياتى\n" + "\n".join(added_links) + "\n\n"
index_content = index_content.replace("## بازار يۈزلىنىشى ۋە تارىخ (Market Trends & History)", new_section + "## بازار يۈزلىنىشى ۋە تارىخ (Market Trends & History)")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_content)
    
# Update log
with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"\n## [{datetime.now().strftime('%Y-%m-%d')}] ingest | Batch Processing: Automatically generated {len(files)} wiki pages from 'ئۇيغۇر تورى ئارخىپلىرى' clippings, built keyword links, updated index, and moved originals to raw folder.\n")

print(f"Processed {len(files)} files successfully.")
