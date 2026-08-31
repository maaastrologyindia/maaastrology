import glob
import re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        # Let's find the exact div/section containing the banner and inject margin: 0 auto directly into its style tag
        # Or wrap it in a clean center-aligned div tag programmatically
        
        # Replace the outer container or add an explicit centering wrapper around the banner block
        content = content.replace(
            '<div style="background:', 
            '<div style="display: flex; justify-content: center; width: 100%; margin: 20px 0;"><div style="width: 90%; max-width: 1200px; margin: 0 auto; background:'
        )
        
        # Close the extra wrapper div right after the banner closes
        # Let's find where the banner block ends (right before "A More Thoughtful Way to Shop")
        content = content.replace(
            '</div>\n    <div class="', 
            '</div></div>\n    <div class="'
        )
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Direct HTML structure updated in:", path)
