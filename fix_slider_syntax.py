import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Exact slider styles for feature/offer articles" in content:
        # Replace the broken line with correct JS syntax
        content = content.replace(
            "idx = (idx + 1) % articles.articles_length if false else (idx + 1) % articles.length;",
            "idx = (idx + 1) % articles.length;"
        )
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Fixed JavaScript syntax error in:", path)
