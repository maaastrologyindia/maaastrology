import glob
import re

for path in glob.glob("public/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if the offer boxes exist in the file
    if "₹399 Each" in content and "WELCOME10" in content:
        # Let's write CSS and JS to turn the offer cards container into a single sliding box
        slider_injection = """
<style>
/* Single rotating offer box container */
section#approach .reviews, .offers-carousel {
    position: relative;
    overflow: hidden;
    min-height: 110px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}
section#approach .reviews article.review, .offers-carousel article {
    position: absolute;
    width: 100%;
    max-width: 400px;
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
    pointer-events: none;
    box-sizing: border-box;
    margin: 0 auto;
    left: 0;
    right: 0;
}
section#approach .reviews article.review.active, .offers-carousel article.active {
    opacity: 1;
    pointer-events: auto;
    position: relative;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
    const reviews = document.querySelectorAll('section#approach .reviews article.review, .offers-carousel article');
    if (reviews.length === 0) return;
    let currentIndex = 0;
    reviews[currentIndex].classList.add('active');
    
    setInterval(() => {
        reviews[currentIndex].classList.remove('active');
        currentIndex = (currentIndex + 1) % reviews.length;
        reviews[currentIndex].classList.add('active');
    }, 3000);
});
</script>
</head>
"""
        if "Single rotating offer box container" not in content:
            content = content.replace("</head>", slider_injection)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Converted offer boxes into a single auto-rotating card in:", path)
