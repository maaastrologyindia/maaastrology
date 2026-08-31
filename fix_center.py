import glob, re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        # Wrap or force absolute centering via a clean CSS block injected right before </head>
        absolute_center_fix = """
<style>
/* Absolute centering wrapper fix for the dark banner */
div:has(> div[style*="background"]), section:has(> div[style*="background"]), div:has(> h2:contains("Energized")) {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
}
div[style*="background: rgb"], div[style*="background:linear-gradient"], div[style*="background: #"] {
    margin-left: auto !important;
    margin-right: auto !important;
    float: none !important;
}
</style>
</head>
"""
        if "Absolute centering wrapper fix" not in content:
            content = content.replace("</head>", absolute_center_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Injected absolute centering fix into:", path)
