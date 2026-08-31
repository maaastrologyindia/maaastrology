import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized" in content:
        alignment_fix = """
<style>
/* Center align promotional dark banner containers */
div[style*="background: rgb"], div[style*="background:linear-gradient"], div[style*="background: #"], section.bg-black, div.bg-black {
    margin-left: auto !important;
    margin-right: auto !important;
}
</style>
</head>
"""
        if "Center align promotional dark banner containers" not in content:
            content = content.replace("</head>", alignment_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Injected alignment fix into:", path)
