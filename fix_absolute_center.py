import glob
import re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Energized & Charged" in content:
        bulletproof_fix = """
<style>
/* Bulletproof Centering Fix */
section, div {
    box-sizing: border-box;
}
body * {
    max-width: 100%;
}
div[style*="background:"]:not(:root), section[style*="background:"] {
    display: block !important;
    margin: 0 auto !important;
    float: none !important;
    position: relative !important;
    left: 0 !important;
    right: 0 !important;
    width: 92% !important;
    max-width: 1200px !important;
}
div:has(> div[style*="background:"]) {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
}
</style>
</head>
"""
        # Clean up old style tags cleanly
        content = re.sub(r'<style>/\*.*?Centering.*?\*/.*?</style>', '', content, flags=re.DOTALL)
        content = content.replace("</head>", bulletproof_fix)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Applied bulletproof centering to:", path)
