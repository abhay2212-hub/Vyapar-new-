import glob

files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

remnant_str = 'These jeans fit true to size with stretch for comfort, ideal for daily wear in Indian climates. Some users note color fading after 10-15 washes, but the quality holds up better than budget alternatives. Perfect for bathroom and tile cleaning, priced around ₹2,000-3,000 on sale.'
replacement_str = 'This bathroom cleaner works exceptionally well on hard water stains and tiles! Highly recommended for daily bathroom hygiene and deep stain removal.'

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if remnant_str in content:
        content = content.replace(remnant_str, replacement_str)

    # Also catch any partial substring
    content = content.replace('These jeans fit true to size with stretch for comfort', 'This bathroom cleaner works exceptionally well on hard water stains and tiles')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final review remnant replaced across all HTML files successfully!")
