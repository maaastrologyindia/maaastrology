import glob, re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Target the approach section or the container holding "A More Thoughtful Way to Shop"
    # and force it to have the exact inline wrapper style matching the black banner
    if 'A More Thoughtful Way to Shop' in content:
        # Replace the section tag with a styled wrapper version
        content = re.sub(
            r'<section([^>]*)id="approach"([^>]*)>',
            r'<section\1id="approach"\2 style="max-width: 800px !important; width: 90% !important; margin: 40px auto !important; padding: 0 20px !important; box-sizing: border-box !important;">',
            content
        )
        # Also fix inner wrapper/cards if any
        content = content.replace(
            '<div class="reviews"',
            '<div class="reviews" style="max-width: 100% !important; width: 100% !important; margin: 0 auto !important;"'
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Directly updated HTML structure in:", path)
