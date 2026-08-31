import glob

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "399 Each" in content and "WELCOME10" in content:
        carousel_fix = """
<style>
/* Exact Offer Carousel Fix */
.reviews, section#approach .reviews {
    display: block !important;
    position: relative !important;
    height: 110px !important;
    overflow: hidden !important;
    max-width: 400px !important;
    margin: 0 auto !important;
}
.reviews article, section#approach .reviews article {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    opacity: 0 !important;
    transition: opacity 0.5s ease-in-out !important;
    pointer-events: none !important;
    box-sizing: border-box !important;
}
.reviews article.active-slide, section#approach .reviews article.active-slide {
    opacity: 1 !important;
    pointer-events: auto !important;
    position: relative !important;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
    const articles = document.querySelectorAll('section#approach .reviews article, .reviews article');
    if (articles.length === 0) return;
    
    let current = 0;
    articles[current].classList.add('active-slide');
    
    setInterval(() => {
        articles[current].classList.remove('active-slide');
        current = (current + 1) % articles.length;
        articles[current].classList.add('active-slide');
    }, 3000);
});
</script>
</head>
"""
        if "Exact Offer Carousel Fix" not in content:
            content = content.replace("</head>", carousel_fix)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Applied exact offer carousel fix to:", path)
