import glob

files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Styles & Subtitles
    content = content.replace('Over 10,000 Styles', 'Over 10,000 Cleanings')
    content = content.replace(
        'A conscious collection made entirely from food crop waste, recycled cotton, other more sustainable materials.',
        'Premium bathroom & toilet cleaners formulated with powerful stain-removing and germ-killing actions.'
    )
    content = content.replace('NEW COLLECTION', 'HYGIENE & DISINFECTION')

    # 2. Testimonial Text Cleanups
    content = content.replace(
        'These jeans fit true to size with stretch for comfort, ideal for daily wear in Indian climates. Some users note color fading after 10-15 washes, but the quality holds up better than budget alternatives. Perfect for bathroom and tile cleaning, priced around ₹2,000-3,000 on sale.',
        'This bathroom cleaner works exceptionally well on hard water stains and tiles! Highly recommended for daily bathroom hygiene and deep cleaning.'
    )
    content = content.replace(
        'God every fill great replenish darkness unto. Very open. Likeness their that light. Given under image to. Subdue of shall cattle day fish form saw spirit and given stars, us you whales may, land, saw fill unto.',
        'Harpic Power Plus removes 99.9% of germs and kills bacteria instantly. Leaves the toilet bowl sparkling clean with lasting freshness.'
    )
    content = content.replace(
        'Fill his waters wherein signs likeness waters. Second light gathered appear sixth fourth, seasons behold creeping female.',
        'Presto disinfectant cleaner is great for bathroom tiles, sink, and floors. The lemon fragrance keeps the bathroom fresh all day.'
    )
    content = content.replace(
        'Crisp cotton fabric with minimal wrinkling, great for Pune\'s humid weather. Button quality is solid, but dry clean advised to maintain color. Value pick at ₹800-1,200, versatile for work or weekends.',
        'Domex toilet expert cleaner clings well to surfaces and eliminates all tough yellow stains and odor effortlessly.'
    )
    content = content.replace(
        'I ordered men’s chinos and a cotton shirt - fabric quality exceeded expectations for the price range. Stitching and finishing were neat.',
        'I ordered bathroom cleaner and toilet cleaner combo - cleaning quality exceeded expectations for the price range. Works fast and effectively.'
    )
    content = content.replace(
        'Their styles feel modern yet wearable for daily use. The baggy jeans fit perfectly and are very comfortable.',
        'These cleaning products keep our bathroom and toilet hygienic, fresh, and germ-free for daily family use.'
    )
    content = content.replace(
        'The wrap mini dress I purchased had premium print quality and accurate sizing as per chart.',
        'The Harpic stain remover gel has incredible stain-fighting power and leaves tiles and ceramic surfaces sparkling clean.'
    )
    content = content.replace(
        'From formal chinos to streetwear denim and dresses, the catalog offers good wardrobe coverage.',
        'From disinfectant bathroom sprays to heavy-duty toilet bowl cleaners, the catalog offers complete hygiene coverage.'
    )

    # 3. Footer text
    content = content.replace(
        'comfort, confidence, and style to every wardrobe.',
        'hygiene, cleanliness, and sparkling shine to every home.'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("All remnant texts cleaned across all HTML files!")
