import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "A More Thoughtful Way to Shop" in content:
        # Replace the faint section header block with explicitly styled maroon text
        old_block = '<div class="sectionhead"><div><h2 style="color: #ffffff !important;">A More Thoughtful Way to Shop</h2>'
        new_block = '<div class="sectionhead"><div><h2 style="color: #5c1d24 !important;">A More Thoughtful Way to Shop</h2>'
        
        content = content.replace(old_block, new_block)
        
        # Also catch any generic sectionhead h2 variations
        content = content.replace(
            '<div class="sectionhead"><div><h2>A More Thoughtful Way to Shop</h2>',
            '<div class="sectionhead"><div><h2 style="color: #5c1d24 !important;">A More Thoughtful Way to Shop</h2>'
        )
        
        # Also fix the paragraph description text right below it
        content = content.replace(
            '<p>Clear information, simple pricing and a calm premium experience.</p>',
            '<p style="color: #5c1d24 !important; opacity: 0.9 !important;">Clear information, simple pricing and a calm premium experience.</p>'
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated HTML inline styles for section header in:", path)
