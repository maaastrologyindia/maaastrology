import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "A More Thoughtful Way to Shop" in content:
        color_fix = """
<style>
/* Match light section headings to footer maroon color */
section:not([style*="background:"]) h2, .sectionhead h2, div.sectionhead h2 {
    color: #5c1d24 !important;
}
</style>
</head>
"""
        if "Match light section headings to footer maroon color" not in content:
            content = content.replace("</head>", color_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Updated heading color in:", path)
