import glob
for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Every bracelet is presented" in content:
        # Replace the dark section inline style or class to force white text
        new_content = content.replace(
            'style="background:', 
            'style="color: #ffffff !important; background:'
        )
        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Fixed banner text in:", path)
