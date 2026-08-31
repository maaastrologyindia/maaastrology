import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("Perfect width match for white info box", "Cleaned")

    css = """
<style>
/* Absolute exact width match to black banner */
section#approach {
    max-width: 800px !important;
    width: 100% !important;
    margin: 40px auto !important;
    padding: 0 20px !important;
    box-sizing: border-box !important;
}

section#approach > div, 
section#approach .reviews, 
section#approach article, 
section#approach .review-card,
section#approach div[style*="background"] {
    max-width: 800px !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}
</style>
</head>
"""

    if "Absolute exact width match to black banner" not in content:
        content = content.replace("</head>", css)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated absolute width match in:", path)
