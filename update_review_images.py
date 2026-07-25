import glob, re

files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

# List of cleaner images to use for buyer review thumbnails (excluding logo.png)
cleaner_review_images = [
    "image/shopping.webp",
    "image/shopping (1).webp",
    "image/shopping (2).webp",
    "image/shopping (3).webp",
    "image/shopping (4).webp",
    "image/shopping (7).webp",
    "image/shopping (8).webp",
    "image/shopping (9).webp",
    "image/shopping (10).webp"
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Clean up review text remnant if present
    content = content.replace(
        'This bathroom cleaner works exceptionally well on hard water stains and tiles, ideal for daily wear in Indian climates. Some users note color fading after 10-15 washes, but the quality holds up better than budget alternatives. Perfect for bathroom and tile cleaning, priced around ₹2,000-3,000 on sale.',
        'This bathroom cleaner works exceptionally well on hard water stains and tiles! Highly recommended for daily bathroom hygiene and deep stain removal.'
    )

    # Find all <div class="testi-image">...</div> blocks and replace their img src
    def replace_testi_img(match):
        # Pick an image index based on match position or counter
        img_src = cleaner_review_images[replace_testi_img.counter % len(cleaner_review_images)]
        replace_testi_img.counter += 1
        return f'<div class="testi-image"><img loading="lazy" decoding="async" width="100" height="100" src="{img_src}" class="attachment-thumbnail size-thumbnail" alt="Cleaner Product" style="object-fit: contain; background: #fff; border-radius: 6px; padding: 4px;" /></div>'

    replace_testi_img.counter = 0

    testi_pattern = re.compile(r'<div class="testi-image">.*?</div>', re.DOTALL)
    content = testi_pattern.sub(replace_testi_img, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated review images and text across all HTML files successfully!")
