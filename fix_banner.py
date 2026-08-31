import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized" in content:
        # Directly target and force white color on headings containing Energized
        content = content.replace("<h2>✨", '<h2 style="color: #ffffff !important;"><span style="color: #ffd700 !important;">✨</span>')
        content = content.replace("<h3>✨", '<h3 style="color: #ffffff !important;"><span style="color: #ffd700 !important;">✨</span>')
        # Fallback for any h2/h3 near the dark banner
        content = content.replace("<h2>", '<h2 style="color: #ffffff !important;">')
        content = content.replace("<h3>", '<h3 style="color: #ffffff !important;">')
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Forced inline white color on headings in:", path)
