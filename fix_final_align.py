import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        # Force parent and banner into absolute center
        fix_code = """
<style>
/* Direct Centering Fix */
body {
    display: flex;
    flex-direction: column;
    align-items: center;
}
main, div.container, section {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
div[style*="background"] {
    margin: 0 auto !important;
    max-width: 1200px !important;
    width: 90% !important;
}
</style>
</head>
"""
        if "Direct Centering Fix" not in content:
            content = content.replace("</head>", fix_code)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Fixed alignment in:", path)
