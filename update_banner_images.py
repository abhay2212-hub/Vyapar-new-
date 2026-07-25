import glob, re

css_file = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/wp-content/uploads/elementor/css/post-1350.css'

with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
    css_content = f.read()

# Replace the 6 background-image URLs in post-1350.css
css_content = css_content.replace(
    'https://vasroventures.com/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-24-at-16.51.49-1.jpeg',
    '../../../../image/shopping (3).webp'
)
css_content = css_content.replace(
    'https://vasroventures.com/wp-content/uploads/2020/12/home1-banner-grid-1.jpg',
    '../../../../image/shopping (4).webp'
)
css_content = css_content.replace(
    'https://vasroventures.com/wp-content/uploads/2020/12/home1-banner-grid-3.jpg',
    '../../../../image/shopping (5).webp'
)
css_content = css_content.replace(
    'https://vasroventures.com/wp-content/uploads/2026/01/WhatsApp-Image-2026-01-18-at-6.01.35-AM-1.jpeg',
    '../../../../image/shopping (6).webp'
)
css_content = css_content.replace(
    'https://vasroventures.com/wp-content/uploads/2020/12/home1-deal-carousel-b1.jpg',
    '../../../../image/shopping (7).webp'
)
css_content = css_content.replace(
    'https://vasroventures.com/wp-content/uploads/2026/01/WhatsApp-Image-2026-01-18-at-6.25.05-AM-1.jpeg',
    '../../../../image/shopping (8).webp'
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated post-1350.css background images successfully.")

# Inject CSS override snippet into all HTML files
banner_override_style = """
<style id="custom-best-picks-banner-images">
.elementor-element-14c2608 .razzi-banner__featured-image,
.elementor-element-14c2608 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/shopping (3).webp') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
.elementor-element-9d0417c .razzi-banner__featured-image,
.elementor-element-9d0417c .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/shopping (4).webp') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
.elementor-element-5099ff3 .razzi-banner__featured-image,
.elementor-element-5099ff3 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/shopping (5).webp') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
.elementor-element-1a84e99 .razzi-banner__featured-image,
.elementor-element-1a84e99 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/shopping (6).webp') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
</style>
"""

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'custom-best-picks-banner-images' not in content:
        content = content.replace('</head>', banner_override_style + '\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected banner override CSS into all HTML files.")
