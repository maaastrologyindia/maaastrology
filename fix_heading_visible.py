import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "A More Thoughtful Way to Shop" in content:
        fix = """
<style>
/* Force high contrast dark maroon color for section headings */
.sectionhead h2, .sectionhead p, section#approach h2, section#approach p {
    color: #5c1d24 !important;
    opacity: 1 !important;
    visibility: visible !important;
}
</style>
</head>
"""
        if "Force high contrast dark maroon color" not in content:
            content = content.replace("</head>", fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Updated heading color and opacity in:", path)
