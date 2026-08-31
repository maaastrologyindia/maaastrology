import glob, re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find the style of the black banner section to replicate it exactly
    match = re.search(r'(<section[^>]*style="[^"]*background[^"]*"[^>]*>)', content)
    
    exact_match_css = """
<style>
/* Force section#approach to match the exact max-width and styling of the upper banner */
section#approach {
    max-width: 800px !important;
    width: 800px !important;
    max-width: min(800px, 92vw) !important;
    margin: 40px auto !important;
    padding: 0 !important;
    background: transparent !important;
    box-sizing: border-box !important;
}

section#approach .reviews, section#approach .features-grid, section#approach div {
    max-width: 100% !important;
    width: 100% !important;
    box-sizing: border-box !important;
}

section#approach article, section#approach .review {
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 auto 20px auto !important;
    border-radius: 16px !important;
    box-sizing: border-box !important;
}
</style>
</head>
"""

    content = content.replace("Exact match for white info section to upper black banner dimensions", "Cleaned")
    
    if "Force section#approach to match the exact max-width" not in content:
        content = content.replace("</head>", exact_match_css)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Applied exact black banner dimension match in:", path)
