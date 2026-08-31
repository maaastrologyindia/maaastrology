import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Every bracelet is presented" in content:
        # Target the entire dark banner block and ensure all text inside it is white
        # Let us inject a powerful style right above </head> that targets the specific container
        universal_fix = """
<style>
/* Force absolute white for all text inside dark promotional banner */
div[style*="background:"], section[style*="background:"], div.bg-black, section.bg-black {
    color: #ffffff !important;
}
div[style*="background:"] *, section[style*="background:"] * {
    color: #ffffff !important;
}
</style>
</head>
"""
        if "Force absolute white" not in content:
            content = content.replace("</head>", universal_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully injected absolute white text fix into:", path)
