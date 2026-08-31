import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    footer_fix = """
<style>
/* Fix footer overlap and ensure proper bottom spacing */
body {
    position: relative !important;
    min-height: 100vh !important;
    padding-bottom: 0 !important;
}
main#top, .main-container {
    padding-bottom: 80px !important;
}
footer {
    position: relative !important;
    width: 100% !important;
    clear: both !important;
    margin-top: 60px !important;
    z-index: 10 !important;
}
</style>
</head>
"""

    if "Fix footer overlap and ensure proper bottom spacing" not in content:
        content = content.replace("</head>", footer_fix)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Applied footer overlap fix in:", path)
    else:
        # Update existing block if needed
        pass
