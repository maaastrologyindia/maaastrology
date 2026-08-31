import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    css_fix = """
<style>
/* Precise fix for white info section width and footer spacing */
section#approach {
    max-width: 800px !important;
    width: 90% !important;
    margin: 40px auto 100px auto !important;
    padding-bottom: 60px !important;
    box-sizing: border-box !important;
}

section#approach .reviews, section#approach .features-grid, section#approach > div {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto !important;
}

footer {
    position: relative !important;
    margin-top: 120px !important;
    z-index: 50 !important;
}
</style>
</head>
"""

    content = content.replace("Permanent fix for footer overlap", "Cleaned")
    content = content.replace("Fix footer overlap and ensure proper bottom spacing", "Cleaned")
    
    if "Precise fix for white info section width and footer spacing" not in content:
        content = content.replace("</head>", css_fix)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated spacing and width fix in:", path)
