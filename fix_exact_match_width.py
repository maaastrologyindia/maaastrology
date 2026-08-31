import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("Exact width and alignment synchronization", "Cleaned")

    exact_css = """
<style>
/* Perfect width match for white info box to upper black banner */
section#approach {
    max-width: 800px !important;
    width: 100% !important;
    margin: 40px auto !important;
    padding: 0 20px !important;
    box-sizing: border-box !important;
}

section#approach .reviews, 
section#approach .features-grid, 
section#approach > div, 
section#approach article, 
section#approach .review-card {
    max-width: 800px !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}
</style>
</head>
"""

    if "Perfect width match for white info box" not in content:
        content = content.replace("</head>", exact_css)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated exact width match in:", path)
