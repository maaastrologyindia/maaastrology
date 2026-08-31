import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "A More Thoughtful Way to Shop" in content:
        # Inject style to ensure section headings and descriptions on light background are dark and legible
        contrast_fix = """
<style>
/* Ensure high contrast for light sections */
section:not([style*="background:"]), div:not([style*="background:"]) h1, 
section:not([style*="background:"]), div:not([style*="background:"]) h2, 
section:not([style*="background:"]), div:not([style*="background:"]) h3 {
    color: #1a1a1a !important;
}
p.text-muted, .text-gray-600, .text-gray-500, div > p {
    color: #4a4a4a !important;
}
</style>
</head>
"""
        if "Ensure high contrast for light sections" not in content:
            content = content.replace("</head>", contrast_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Injected contrast fix into:", path)
