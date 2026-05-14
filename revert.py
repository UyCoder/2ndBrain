import os
import glob
import shutil

wiki_dir = r"d:\2ndBrain\wiki"
raw_dir = r"d:\2ndBrain\raw"
clippings_dir = r"d:\2ndBrain\Clippings"
index_file = os.path.join(wiki_dir, "مۇندەرىجە.md")

# 1. Move files back from raw to Clippings
raw_files = glob.glob(os.path.join(raw_dir, "*ئۇيغۇر تورى ئارخىپلىرى*.md"))
moved_count = 0
for file_path in raw_files:
    filename = os.path.basename(file_path)
    clippings_path = os.path.join(clippings_dir, filename)
    shutil.move(file_path, clippings_path)
    moved_count += 1

# 2. Delete the generated wiki files
deleted_count = 0
wiki_files = glob.glob(os.path.join(wiki_dir, "بىرىكمە-*.md"))
for file_path in wiki_files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read(500)
        if "ئۇيغۇر-تورى-ئارخىپلىرى" in content and "last_updated:" in content:
            os.remove(file_path)
            deleted_count += 1
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# 3. Clean up the index
try:
    with open(index_file, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    start_str = "## ئۇيغۇر تورى ئارخىپلىرى كۇللىياتى"
    end_str = "## بازار يۈزلىنىشى ۋە تارىخ (Market Trends & History)"
    
    if start_str in index_content and end_str in index_content:
        start_idx = index_content.find(start_str)
        end_idx = index_content.find(end_str)
        
        # Remove everything between start_str (inclusive) and end_str (exclusive)
        new_index = index_content[:start_idx] + end_str + index_content[end_idx+len(end_str):]
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(new_index)
        print("Cleaned up index.")
except Exception as e:
    print(f"Error cleaning index: {e}")

print(f"Reverted {moved_count} files to Clippings.")
print(f"Deleted {deleted_count} generated wiki pages.")
