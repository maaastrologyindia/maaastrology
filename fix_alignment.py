import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized" in content:
        alignment_fix = """
<style>
/* Properly center align promotional dark banner containers with constrained width */
div[style*="background: rgb"], div[style*="background:linear-gradient"], div[style*="background: #"], section.bg-black, div.bg-black {
    display: block !important;
    width: 92% !important;
    max-width: 1200px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
</style>
</head>
"""
        # Replace old alignment fix if present, or append
        if "width: 92% !important;" not in content:
            if "Center align promotional dark banner containers" in content:
                # Remove old style block and insert new one
                import re
                content = re.sub(r'<style>/\* Center align promotional dark banner containers.*?</style>', '', content, flags=re.DOTALL)
            content = content.replace("</head>", alignment_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Updated alignment fix into:", path)
