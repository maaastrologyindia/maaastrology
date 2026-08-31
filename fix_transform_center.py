import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        transform_fix = """
<style>
/* Foolproof Transform Centering Trick */
div[style*="background:"]:not(:root), section[style*="background:"] {
    position: relative !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    width: 92% !important;
    max-width: 1200px !important;
}
</style>
</head>
"""
        # Clean up old style tags if any, and inject transform fix
        import re
        content = re.sub(r'<style>/\*.*?(Centering|Alignment).*?\*/.*?</style>', '', content, flags=re.DOTALL)
        if "Foolproof Transform Centering Trick" not in content:
            content = content.replace("</head>", transform_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Injected transform centering fix into:", path)
