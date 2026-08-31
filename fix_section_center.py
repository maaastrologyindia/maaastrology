import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        fix_style = """
<style>
/* Force absolute center alignment on the Energized banner section */
section#why, section:has(h2), div:has(> h2:contains("Energized")) {
    margin-left: auto !important;
    margin-right: auto !important;
    display: block !important;
    width: 90% !important;
    max-width: 1200px !important;
    float: none !important;
}
</style>
</head>
"""
        if "Force absolute center alignment" not in content:
            content = content.replace("</head>", fix_style)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Applied section center fix to:", path)
