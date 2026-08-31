with open("public/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "Energized & Charged" in line:
        # Print surrounding lines to see the exact HTML structure
        start = max(0, i - 10)
        end = min(len(lines), i + 10)
        print("--- HTML STRUCTURE AROUND BANNER ---")
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
        break
