import glob

# 1. Update post-1350.css
css_file = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/wp-content/uploads/elementor/css/post-1350.css'

if glob.os.path.exists(css_file):
    with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
        css = f.read()

    # Replace any orange colors or gradient text fill in post-1350.css
    css = css.replace('#FF8200', '#000080')
    css = css.replace('linear-gradient(92.37deg, #FF8200 0%, #735C22 100%)', 'none')
    css = css.replace('linear-gradient(92.37deg, #000080 0%, #735C22 100%)', 'none')

    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Add aggressive CSS override in all HTML files
navy_css_override = """<style id="custom-navy-blue-scrolling-fonts-override">
/* Aggressive Navy Blue Font Override for Ticker Brand Headings */
.elementor-element-a659fde .razzi-heading-title,
.elementor-widget-razzi-heading .razzi-heading-title,
.razzi-heading-auto-scrolling .razzi-heading-title,
.razzi-heading-wrapper .razzi-heading-title,
.razzi-heading-title,
.elementor-element-a659fde *,
.razzi-heading-auto-scrolling * {
    background: none !important;
    -webkit-background-clip: border-box !important;
    -webkit-text-fill-color: #000080 !important;
    background-clip: border-box !important;
    color: #000080 !important;
    font-weight: 700 !important;
}
</style>
"""

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if '</head>' in content:
        if 'custom-navy-blue-scrolling-fonts-override' in content:
            # Replace existing snippet
            content = content.replace(
                content[content.find('<style id="custom-navy-blue-scrolling-fonts-override">'):content.find('</style>', content.find('<style id="custom-navy-blue-scrolling-fonts-override">'))+8],
                navy_css_override
            )
        else:
            content = content.replace('</head>', f'{navy_css_override}</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied force Navy Blue font styling to all ticker brand headings.")
