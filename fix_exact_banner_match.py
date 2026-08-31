import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    exact_css = """
<style>
/* Exact match for white info section to upper black banner dimensions */
section#approach {
    max-width: 800px !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
    box-sizing: border-box !important;
}

section#approach .reviews, section#approach article {
    max-width: 100% !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}

footer {
    position: relative !important;
    margin-top: 80px !important;
    z-index: 10 !important;
}
</style>
</head>
"""

    # Clean previous injection markers
    content = content.replace("Precise fix for white info section width and footer spacing", "Cleaned")
    
    if "Exact match for white info section to upper black banner dimensions" not in content:
        content = content.replace("</head>", exact_css)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Applied exact banner width match CSS in:", path)
