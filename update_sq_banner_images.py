import glob, re

css_file = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/wp-content/uploads/elementor/css/post-1350.css'

with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
    css_content = f.read()

# Replace background-image URLs in post-1350.css with sq folder images
css_content = css_content.replace(
    '../../../../image/shopping (3).webp',
    '../../../../image/sq/1.jpg'
)
css_content = css_content.replace(
    '../../../../image/shopping (4).webp',
    '../../../../image/sq/2.jpg'
)
css_content = css_content.replace(
    '../../../../image/shopping (5).webp',
    '../../../../image/sq/3.jpg'
)
css_content = css_content.replace(
    '../../../../image/shopping (6).webp',
    '../../../../image/sq/4.jpg'
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated post-1350.css background images to image/sq/ successfully.")

# Updated style block for all HTML files
banner_override_style = """<style id="custom-best-picks-banner-images">
.elementor-element-14c2608 .razzi-banner__featured-image,
.elementor-element-14c2608 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/1.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
.elementor-element-9d0417c .razzi-banner__featured-image,
.elementor-element-9d0417c .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/2.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
.elementor-element-5099ff3 .razzi-banner__featured-image,
.elementor-element-5099ff3 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/3.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
.elementor-element-1a84e99 .razzi-banner__featured-image,
.elementor-element-1a84e99 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/4.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
</style>"""

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace existing style block if present, or add to </head>
    if 'id="custom-best-picks-banner-images"' in content:
        content = re.sub(r'<style id="custom-best-picks-banner-images">.*?</style>', banner_override_style, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', banner_override_style + '\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated banner override CSS in all HTML files to use sq folder images.")
