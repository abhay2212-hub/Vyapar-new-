import re

# Read the full index.html
with open('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Change the title
content = content.replace('<title>Vasro Ventures</title>', '<title>About Us – Vyaapar Vault</title>')

# Find the main content area between the header and footer sections
# The main content starts after the closing of the header area and ends before the footer area
# We'll replace everything between the campaign-bar/slider and the footer section

# Replace the body content - keep header, replace main content, keep footer
# Find the main content section (after the header icon boxes and before the footer)
# The main content starts around the slideshow section

# Strategy: find the first major <section after the header, and the review section end / footer start
# Replace from after icon-box section through the reviews section

# Let's find the start of main content (after the feature boxes like FREE SHIPPING)
# and replace through just before the footer

# Find marker: after the last header icon-box section ends and before the footer
# The content between the slideshow banners and the footer/mobile-menu is the main body

# Find the slideshow section start
slideshow_start = content.find('<section class="elementor-section elementor-top-section elementor-element elementor-element-c8fb47c')
if slideshow_start == -1:
    # Try alternate marker
    slideshow_start = content.find('elementor-element-c8fb47c')
    if slideshow_start != -1:
        slideshow_start = content.rfind('<section', 0, slideshow_start)

# Find the mobile menu modal start (this is where main content ends)
mobile_menu_start = content.find('<div id="mobile-menu-modal"')

if slideshow_start == -1 or mobile_menu_start == -1:
    print(f"Markers not found: slideshow_start={slideshow_start}, mobile_menu_start={mobile_menu_start}")
    # Let's try different approach - find by the campaign bar end and footer/mobile menu
    # Use broader markers
    # After the header-mobile section
    header_end_marker = '</header>'
    header_end = content.find(header_end_marker)
    if header_end != -1:
        header_end += len(header_end_marker)
        slideshow_start = header_end
    
    # Find campaign bar end
    campaign_end = content.find('</div>', content.find('id="campaign-bar"'))
    if campaign_end != -1:
        # Find the next section after campaign bar
        next_section = content.find('<section', campaign_end)
        if next_section != -1:
            slideshow_start = next_section

print(f"slideshow_start={slideshow_start}, mobile_menu_start={mobile_menu_start}")

# New about us content to replace the main body
about_content = '''
    <!-- About Us Page Content -->
    <style>
        .about-breadcrumb { max-width: 1200px; margin: 0 auto; padding: 20px 15px; font-size: 14px; color: #999; }
        .about-breadcrumb a { color: #333; text-decoration: none; }
        .about-breadcrumb a:hover { color: #2DA815; }
        
        .about-hero-section { position: relative; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); padding: 100px 20px; text-align: center; overflow: hidden; }
        .about-hero-section::before { content: ''; position: absolute; width: 400px; height: 400px; border-radius: 50%; background: rgba(45, 168, 21, 0.12); top: -100px; right: -100px; }
        .about-hero-section::after { content: ''; position: absolute; width: 250px; height: 250px; border-radius: 50%; background: rgba(45, 168, 21, 0.08); bottom: -80px; left: -50px; }
        .about-hero-section h1 { color: #fff; font-size: 52px; font-weight: 700; position: relative; z-index: 1; margin: 0 0 16px; }
        .about-hero-section p { color: rgba(255,255,255,0.8); font-size: 20px; position: relative; z-index: 1; max-width: 600px; margin: 0 auto; }
        
        .about-section { max-width: 1000px; margin: 70px auto; padding: 0 15px; }
        .about-section h2 { font-size: 34px; font-weight: 700; color: #1a1a2e; margin-bottom: 24px; }
        .about-section p { font-size: 16px; line-height: 1.9; color: #555; margin-bottom: 16px; }
        
        .values-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; }
        .value-card { background: #f8f9fa; border-radius: 16px; padding: 40px 28px; text-align: center; transition: transform 0.3s ease, box-shadow 0.3s ease; border: 1px solid #eee; }
        .value-card:hover { transform: translateY(-8px); box-shadow: 0 16px 48px rgba(0,0,0,0.08); border-color: #2DA815; }
        .value-icon { font-size: 48px; margin-bottom: 18px; display: block; }
        .value-card h3 { font-size: 20px; font-weight: 600; color: #1a1a2e; margin-bottom: 10px; }
        .value-card p { font-size: 14px; color: #666; line-height: 1.7; margin: 0; }
        
        .stats-bar { background: linear-gradient(135deg, #1a1a2e, #0f3460); padding: 70px 20px; }
        .stats-grid { max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; text-align: center; }
        .stat-number { font-size: 48px; font-weight: 700; color: #2DA815; display: block; }
        .stat-label { font-size: 14px; color: rgba(255,255,255,0.65); margin-top: 8px; text-transform: uppercase; letter-spacing: 1.5px; display: block; }
        
        .about-mission { background: #f8f9fa; padding: 70px 20px; }
        .about-mission-inner { max-width: 1000px; margin: 0 auto; }
        .about-mission h2 { font-size: 34px; font-weight: 700; color: #1a1a2e; margin-bottom: 24px; }
        .about-mission p { font-size: 16px; line-height: 1.9; color: #555; margin-bottom: 16px; }
        
        @media (max-width: 768px) {
            .about-hero-section h1 { font-size: 32px; }
            .about-hero-section p { font-size: 16px; }
            .values-grid { grid-template-columns: 1fr; }
            .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 24px; }
            .stat-number { font-size: 36px; }
        }
    </style>
    
    <div class="about-breadcrumb"><a href="index.html">Home</a> &nbsp;›&nbsp; About Us</div>
    
    <section class="about-hero-section">
        <h1>About Vyaapar Vault</h1>
        <p>Your Trusted Partner for Premium Bathroom &amp; Toilet Cleaning Solutions</p>
    </section>
    
    <section class="about-section">
        <h2>Our Story</h2>
        <p>At Vyaapar Vault, we believe a clean home is a happy home. Founded with a passion for quality hygiene products, we curate the finest bathroom and toilet cleaning solutions from top Indian and international brands.</p>
        <p>Our mission is simple — to make premium cleaning products accessible to every Indian household at competitive prices, with fast delivery and exceptional customer service. Whether you need a powerful disinfectant for daily bathroom maintenance or a heavy-duty toilet cleaner to tackle tough stains, Vyaapar Vault has you covered.</p>
        <p>We partner with trusted brands like Harpic, Domex, Presto!, urbanWipe, Lizol, and many more to bring you a comprehensive selection of cleaners that are safe, effective, and value for money.</p>
    </section>
    
    <section class="about-section">
        <h2>Why Choose Us</h2>
        <div class="values-grid">
            <div class="value-card">
                <span class="value-icon">🚚</span>
                <h3>Free Shipping</h3>
                <p>Free delivery on all orders across India. No minimum purchase required.</p>
            </div>
            <div class="value-card">
                <span class="value-icon">✅</span>
                <h3>100% Genuine Products</h3>
                <p>Every product sourced directly from authorized distributors. No fakes, guaranteed.</p>
            </div>
            <div class="value-card">
                <span class="value-icon">🔄</span>
                <h3>Easy Returns</h3>
                <p>Hassle-free 7-day return policy. If you are not satisfied, we will make it right.</p>
            </div>
            <div class="value-card">
                <span class="value-icon">💰</span>
                <h3>Best Prices</h3>
                <p>Competitive pricing with regular deals, combos, and festive season offers.</p>
            </div>
            <div class="value-card">
                <span class="value-icon">🛡️</span>
                <h3>Secure Payments</h3>
                <p>All transactions encrypted with SSL. Multiple payment options including UPI, cards, and COD.</p>
            </div>
            <div class="value-card">
                <span class="value-icon">📞</span>
                <h3>24/7 Support</h3>
                <p>Our customer support team is available round the clock to assist you with any queries.</p>
            </div>
        </div>
    </section>
    
    <section class="stats-bar">
        <div class="stats-grid">
            <div><span class="stat-number">10K+</span><span class="stat-label">Happy Customers</span></div>
            <div><span class="stat-number">50+</span><span class="stat-label">Premium Products</span></div>
            <div><span class="stat-number">99%</span><span class="stat-label">Satisfaction Rate</span></div>
            <div><span class="stat-number">24/7</span><span class="stat-label">Customer Support</span></div>
        </div>
    </section>
    
    <section class="about-mission">
        <div class="about-mission-inner">
            <h2>Our Mission</h2>
            <p>We are on a mission to transform the way India shops for cleaning essentials. By combining technology with trust, we are building a platform where quality meets convenience. Every product in our catalog is hand-picked, tested, and verified to ensure it meets the highest standards of cleaning performance.</p>
            <p>Join thousands of Indian households who trust Vyaapar Vault for their daily cleaning needs.</p>
        </div>
    </section>
    
'''

if slideshow_start != -1 and mobile_menu_start != -1:
    new_content = content[:slideshow_start] + about_content + content[mobile_menu_start:]
    
    # Fix the active menu item
    new_content = new_content.replace(
        'current-menu-item current_page_item menu-item-home menu-item-12532 active"><a href="index.html">Home</a>',
        'menu-item-home menu-item-12532"><a href="index.html">Home</a>'
    )
    new_content = new_content.replace(
        'menu-item-12535"><a href="about-us.html">About Us</a>',
        'menu-item-12535 active current-menu-item"><a href="about-us.html">About Us</a>'
    )
    
    with open('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/about-us.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("About Us page created successfully using the full site theme!")
else:
    print("ERROR: Could not find content markers in index.html")
