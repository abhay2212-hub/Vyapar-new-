import glob

css_file = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/wp-content/uploads/elementor/css/post-1350.css'

if glob.os.path.exists(css_file):
    with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
        css_content = f.read()

    # Update gradient to solid navy blue in post-1350.css
    css_content = css_content.replace(
        'background: linear-gradient(92.37deg, #FF8200 0%, #735C22 100%);',
        'background: none !important;'
    )
    css_content = css_content.replace(
        '-webkit-text-fill-color: transparent;',
        '-webkit-text-fill-color: #000080 !important;'
    )
    css_content = css_content.replace(
        'color: #FF8200;',
        'color: #000080 !important;'
    )

    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

navy_css_snippet = """<style id="custom-navy-blue-scrolling-fonts">
/* Navy Blue font color for brand banner headings */
.razzi-heading-auto-scrolling .razzi-heading-title,
.elementor-element-a659fde .razzi-heading-title,
.razzi-heading-wrapper.razzi-heading-auto-scrolling .razzi-heading-title {
    background: none !important;
    -webkit-background-clip: unset !important;
    -webkit-text-fill-color: #000080 !important;
    background-clip: unset !important;
    color: #000080 !important;
    font-weight: 700 !important;
}
</style>
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if '</head>' in content and 'custom-navy-blue-scrolling-fonts' not in content:
        content = content.replace('</head>', f'{navy_css_snippet}</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated scrolling brand headings to Navy Blue (#000080) across all CSS and HTML files.")
