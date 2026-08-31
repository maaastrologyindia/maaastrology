import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        fix_code = """
<style>
/* Force main container and its children to center */
main#top, #top {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
}
main#top > * {
    margin-left: auto !important;
    margin-right: auto !important;
    max-width: 1200px !important;
    width: 90% !important;
}
</style>
</head>
"""
        if "Force main container and its children to center" not in content:
            content = content.replace("</head>", fix_code)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Fixed main container centering in:", path)
