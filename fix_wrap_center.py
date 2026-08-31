import glob
import re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        # Find the dark banner block (div/section with background) and wrap it
        # Let's target the block containing "Energized & Charged" and ensure it's wrapped cleanly
        pattern = r'(<div[^>]*style="[^"]*background[^"]*"[^>]*>.*?Choose Your Bracelet.*?</div>\s*</div>)'
        
        # Simpler approach: Find the specific banner container div and replace it with a centered wrapper version
        # Let's find the banner div by its unique content text
        match = re.search(r'(<div[^>]*style="[^"]*background:[^"]*".*?Choose Your Bracelet.*?</div>\s*</div>)', content, re.DOTALL)
        if match:
            banner_html = match.group(1)
            centered_banner = f'<div style="width: 100%; display: flex; justify-content: center; align-items: center; margin: 2rem 0;">{banner_html}</div>'
            content = content.replace(banner_html, centered_banner)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully wrapped and centered banner in:", path)
