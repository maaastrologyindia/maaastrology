import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove old injected styles to prevent conflicts
    content = content.replace("Exact structural match to upper black banner", "Cleaned")
    content = content.replace("Force section#approach to match the exact max-width", "Cleaned")

    perfect_sync_css = """
<style>
/* Exact width and alignment synchronization with the upper black banner */
section#approach {
    max-width: 800px !important;
    width: 100% !important;
    margin: 40px auto !important;
    padding: 0 !important;
    box-sizing: border-box !important;
}

section#approach .reviews, section#approach .features-grid, section#approach > div {
    max-width: 800px !important;
    width: 100% !important;
    margin: 0 auto !important;
    padding: 0 !important;
    box-sizing: border-box !important;
}

section#approach article, section#approach .review-card {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto 20px auto !important;
    box-sizing: border-box !important;
}
</style>
</head>
"""

    if "Exact width and alignment synchronization" not in content:
        content = content.replace("</head>", perfect_sync_css)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated exact sync CSS in:", path)
