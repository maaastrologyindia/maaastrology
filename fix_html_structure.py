import glob, re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's inject a definitive styling block that forces the approach section and its inner cards 
    # to match the 800px max-width, center alignment, and rounded corners of the black banner.
    forced_fix = """
<style>
/* Exact structural match to upper black banner */
section#approach {
    max-width: 800px !important;
    width: 100% !important;
    margin: 40px auto !important;
    padding: 0 20px !important;
    box-sizing: border-box !important;
    display: block !important;
    float: none !important;
}

section#approach > div, section#approach .reviews, section#approach article {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto !important;
    box-sizing: border-box !important;
}

section#approach article, section#approach .review-card {
    border-radius: 16px !important;
    overflow: hidden !important;
}
</style>
</head>
"""

    content = content.replace("Force section#approach to match the exact max-width", "Cleaned")
    
    if "Exact structural match to upper black banner" not in content:
        content = content.replace("</head>", forced_fix)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated HTML structure and CSS match in:", path)
