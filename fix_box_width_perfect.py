import glob

# First let's clean up repository via git reset if needed, or just overwrite the bad style cleanly
for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove previous injected CSS blocks to avoid conflicts
    if "<style>" in content:
        # Let's target and replace our custom injected styles cleanly
        content = content.replace("Match white section width and container style", "Cleaned_Old")
        content = content.replace("Match white box width and sizing", "Cleaned_Old")

    perfect_css = """
<style>
/* Match the feature box section container width precisely to the black banner container width */
section#approach {
    max-width: 820px !important;
    width: 100% !important;
    margin: 0 auto !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
    box-sizing: border-box !important;
}
section#approach .reviews {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto !important;
}
section#approach article {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}
</style>
</head>
"""

    if "Match the feature box section container width" not in content:
        content = content.replace("</head>", perfect_css)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Applied precise container width fix in:", path)
