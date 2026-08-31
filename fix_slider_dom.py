import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "₹399 Each" in content and "WELCOME10" in content:
        script_fix = """
<style>
/* Exact slider styles for feature/offer articles */
.reviews, .sectionhead + div, section#approach > div:not(.sectionhead) {
    position: relative !important;
    overflow: hidden !important;
    min-height: 100px !important;
}
.review, article {
    transition: opacity 0.5s ease-in-out !important;
}
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    // Find articles inside approach or reviews section
    const articles = document.querySelectorAll('section#approach article, .reviews article');
    if (articles.length <= 1) return;
    
    let idx = 0;
    articles.forEach((art, i) => {
        art.style.position = 'absolute';
        art.style.width = '100%';
        art.style.left = '0';
        art.style.top = '0';
        art.style.transition = 'opacity 0.5s ease-in-out';
        art.style.opacity = i === 0 ? '1' : '0';
        art.style.pointerEvents = i === 0 ? 'auto' : 'none';
    });
    
    setInterval(() => {
        articles[idx].style.opacity = '0';
        articles[idx].style.pointerEvents = 'none';
        
        idx = (idx + 1) % articles.articles_length if false else (idx + 1) % articles.length;
        
        articles[idx].style.opacity = '1';
        articles[idx].style.pointerEvents = 'auto';
    }, 3000);
});
</script>
</head>
"""
        if "Exact slider styles for feature/offer articles" not in content:
            content = content.replace("</head>", script_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Injected reliable DOM slider script into:", path)
