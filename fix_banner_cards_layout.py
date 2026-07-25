import glob, re

# Absolute side-by-side positioning layout: Text on Left (55%), Image on Right (42%)
banner_layout_style = """<style id="custom-best-picks-banner-images">
/* Fix Best Picks 4 Banner Cards Layout */
.elementor-element-14c2608 .razzi-banner,
.elementor-element-9d0417c .razzi-banner,
.elementor-element-5099ff3 .razzi-banner,
.elementor-element-1a84e99 .razzi-banner {
    position: relative !important;
    height: 260px !important;
    min-height: 260px !important;
    background: #f4f5f8 !important;
    border-radius: 16px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

.elementor-element-14c2608 .razzi-banner:hover,
.elementor-element-9d0417c .razzi-banner:hover,
.elementor-element-5099ff3 .razzi-banner:hover,
.elementor-element-1a84e99 .razzi-banner:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 8px 25px rgba(0,0,0,0.09) !important;
}

/* Force text block to Left half (55% width) */
.elementor-element-14c2608 .razzi-banner-content,
.elementor-element-9d0417c .razzi-banner-content,
.elementor-element-5099ff3 .razzi-banner-content,
.elementor-element-1a84e99 .razzi-banner-content {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    bottom: 0 !important;
    right: auto !important;
    width: 55% !important;
    max-width: 55% !important;
    height: 100% !important;
    transform: none !important;
    margin: 0 !important;
    padding: 30px !important;
    z-index: 10 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: flex-start !important;
    text-align: left !important;
}

.elementor-element-14c2608 .razzi-banner-content-inner,
.elementor-element-9d0417c .razzi-banner-content-inner,
.elementor-element-5099ff3 .razzi-banner-content-inner,
.elementor-element-1a84e99 .razzi-banner-content-inner {
    width: 100% !important;
    text-align: left !important;
    margin: 0 !important;
    padding: 0 !important;
}

.elementor-element-14c2608 .razzi-banner-content__title,
.elementor-element-9d0417c .razzi-banner-content__title,
.elementor-element-5099ff3 .razzi-banner-content__title,
.elementor-element-1a84e99 .razzi-banner-content__title {
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #000000 !important;
    text-align: left !important;
    margin: 0 0 12px 0 !important;
    line-height: 1.3 !important;
}

.elementor-element-14c2608 .razzi-banner-content__button,
.elementor-element-9d0417c .razzi-banner-content__button,
.elementor-element-5099ff3 .razzi-banner-content__button,
.elementor-element-1a84e99 .razzi-banner-content__button {
    color: #000000 !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    padding: 0 !important;
}

/* Force image block to Right half (42% width) with contain fit */
.elementor-element-14c2608 .razzi-banner__featured-image,
.elementor-element-14c2608 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/1.jpg') !important;
    background-size: contain !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    position: absolute !important;
    top: 15px !important;
    right: 15px !important;
    bottom: 15px !important;
    left: auto !important;
    width: 42% !important;
    height: calc(100% - 30px) !important;
    z-index: 5 !important;
}

.elementor-element-9d0417c .razzi-banner__featured-image,
.elementor-element-9d0417c .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/2.jpg') !important;
    background-size: contain !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    position: absolute !important;
    top: 15px !important;
    right: 15px !important;
    bottom: 15px !important;
    left: auto !important;
    width: 42% !important;
    height: calc(100% - 30px) !important;
    z-index: 5 !important;
}

.elementor-element-5099ff3 .razzi-banner__featured-image,
.elementor-element-5099ff3 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/3.jpg') !important;
    background-size: contain !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    position: absolute !important;
    top: 15px !important;
    right: 15px !important;
    bottom: 15px !important;
    left: auto !important;
    width: 42% !important;
    height: calc(100% - 30px) !important;
    z-index: 5 !important;
}

.elementor-element-1a84e99 .razzi-banner__featured-image,
.elementor-element-1a84e99 .razzi-banner .razzi-banner__featured-image {
    background-image: url('image/sq/4.jpg') !important;
    background-size: contain !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    position: absolute !important;
    top: 15px !important;
    right: 15px !important;
    bottom: 15px !important;
    left: auto !important;
    width: 42% !important;
    height: calc(100% - 30px) !important;
    z-index: 5 !important;
}
</style>"""

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'id="custom-best-picks-banner-images"' in content:
        content = re.sub(r'<style id="custom-best-picks-banner-images">.*?</style>', banner_layout_style, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', banner_layout_style + '\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated banner layout CSS in all HTML files.")
