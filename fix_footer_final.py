import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    clean_footer_css = """
<style>
/* Permanent fix for footer overlap */
html, body {
    height: 100%;
    margin: 0;
    display: flex;
    flex-direction: column;
}
main#top, .main-container, body > div:not(footer):not(header) {
    flex: 1;
}
footer {
    position: relative !important;
    width: 100% !important;
    margin-top: 80px !important;
    flex-shrink: 0;
    z-index: 100 !important;
}
</style>
</head>
"""

    if "Permanent fix for footer overlap" not in content:
        content = content.replace("</head>", clean_footer_css)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Applied permanent footer layout fix in:", path)
