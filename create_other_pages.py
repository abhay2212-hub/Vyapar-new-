import re

# Read the full index.html
with open('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find the content boundaries
header_end_marker = '</header>'
header_end = content.find(header_end_marker)
if header_end != -1:
    header_end += len(header_end_marker)

# Find campaign bar end, then next section
campaign_idx = content.find('id="campaign-bar"')
if campaign_idx != -1:
    campaign_end = content.find('</div>', campaign_idx)
    next_section = content.find('<section', campaign_end)
    slideshow_start = next_section
else:
    slideshow_start = header_end

mobile_menu_start = content.find('<div id="mobile-menu-modal"')

print(f"slideshow_start={slideshow_start}, mobile_menu_start={mobile_menu_start}")

# ========== CONTACT US PAGE ==========
contact_content = '''
    <!-- Contact Us Page Content -->
    <style>
        .contact-breadcrumb { max-width: 1200px; margin: 0 auto; padding: 20px 15px; font-size: 14px; color: #999; }
        .contact-breadcrumb a { color: #333; text-decoration: none; }
        .contact-breadcrumb a:hover { color: #2DA815; }
        
        .contact-hero { position: relative; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); padding: 90px 20px; text-align: center; overflow: hidden; }
        .contact-hero::before { content: ''; position: absolute; width: 350px; height: 350px; border-radius: 50%; background: rgba(45, 168, 21, 0.12); top: -80px; right: -80px; }
        .contact-hero h1 { color: #fff; font-size: 48px; font-weight: 700; position: relative; z-index: 1; margin: 0 0 14px; }
        .contact-hero p { color: rgba(255,255,255,0.8); font-size: 18px; position: relative; z-index: 1; }
        
        .contact-wrapper { max-width: 1100px; margin: 60px auto; padding: 0 15px; display: grid; grid-template-columns: 1fr 1fr; gap: 50px; }
        .contact-info h2, .contact-form-section h2 { font-size: 28px; font-weight: 700; color: #1a1a2e; margin-bottom: 20px; }
        .contact-info p { font-size: 15px; color: #555; line-height: 1.7; margin-bottom: 24px; }
        
        .info-card { display: flex; align-items: flex-start; gap: 16px; margin-bottom: 20px; padding: 22px; background: #f8f9fa; border-radius: 14px; border: 1px solid #eee; transition: border-color 0.3s; }
        .info-card:hover { border-color: #2DA815; }
        .info-card-icon { font-size: 28px; flex-shrink: 0; }
        .info-card h4 { font-size: 16px; font-weight: 600; color: #1a1a2e; margin: 0 0 4px; }
        .info-card p { font-size: 14px; color: #666; margin: 0; line-height: 1.5; }
        
        .contact-form-section .form-group { margin-bottom: 18px; }
        .contact-form-section label { display: block; font-size: 14px; font-weight: 500; margin-bottom: 6px; color: #444; }
        .contact-form-section input, .contact-form-section textarea, .contact-form-section select {
            width: 100%; padding: 13px 16px; border: 1.5px solid #ddd; border-radius: 10px;
            font-size: 15px; font-family: inherit; transition: border-color 0.3s; background: #fafafa;
        }
        .contact-form-section input:focus, .contact-form-section textarea:focus, .contact-form-section select:focus {
            outline: none; border-color: #2DA815; background: #fff;
        }
        .contact-form-section textarea { resize: vertical; min-height: 120px; }
        .contact-submit {
            background: linear-gradient(135deg, #2DA815, #1e8a0e); color: #fff; border: none;
            padding: 14px 40px; font-size: 16px; font-weight: 600; border-radius: 10px;
            cursor: pointer; transition: transform 0.2s, box-shadow 0.3s; width: 100%;
        }
        .contact-submit:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(45,168,21,0.3); }
        .contact-success { background: #d4edda; color: #155724; padding: 14px 20px; border-radius: 10px; font-size: 15px; display: none; margin-bottom: 18px; }
        
        @media (max-width: 768px) {
            .contact-wrapper { grid-template-columns: 1fr; gap: 40px; }
            .contact-hero h1 { font-size: 32px; }
        }
    </style>
    
    <div class="contact-breadcrumb"><a href="index.html">Home</a> &nbsp;›&nbsp; Contact Us</div>
    
    <section class="contact-hero">
        <h1>Get In Touch</h1>
        <p>We would love to hear from you. Reach out for orders, support, or partnerships.</p>
    </section>
    
    <div class="contact-wrapper">
        <div class="contact-info">
            <h2>Contact Information</h2>
            <p>Have a question about an order, a product, or need help choosing the right cleaner? Our team is here to help you.</p>
            
            <div class="info-card">
                <span class="info-card-icon">📧</span>
                <div><h4>Email Us</h4><p>support@vyaaparvault.com</p></div>
            </div>
            <div class="info-card">
                <span class="info-card-icon">📞</span>
                <div><h4>Call Us</h4><p>+91 98765 43210</p></div>
            </div>
            <div class="info-card">
                <span class="info-card-icon">📍</span>
                <div><h4>Visit Us</h4><p>Pune, Maharashtra, India</p></div>
            </div>
            <div class="info-card">
                <span class="info-card-icon">🕐</span>
                <div><h4>Business Hours</h4><p>Mon - Sat: 9:00 AM - 7:00 PM IST</p></div>
            </div>
        </div>
        
        <div class="contact-form-section">
            <h2>Send Us a Message</h2>
            <div class="contact-success" id="contactSuccess">✅ Opening Gmail with your message draft ready to send...</div>
            <form onsubmit="handleContactSubmit(event)">
                <div class="form-group">
                    <label for="contactName">Full Name *</label>
                    <input type="text" id="contactName" placeholder="Enter your full name" required>
                </div>
                <div class="form-group">
                    <label for="contactEmail">Email Address *</label>
                    <input type="email" id="contactEmail" placeholder="Enter your email" required>
                </div>
                <div class="form-group">
                    <label for="contactSubject">Subject</label>
                    <select id="contactSubject">
                        <option>Order Inquiry</option>
                        <option>Product Question</option>
                        <option>Return/Refund</option>
                        <option>Partnership</option>
                        <option>Other</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="contactMessage">Your Message *</label>
                    <textarea id="contactMessage" placeholder="Tell us how we can help..." required></textarea>
                </div>
                <button type="submit" class="contact-submit">Send Message</button>
            </form>
        </div>
        <script>
        function handleContactSubmit(event) {
            event.preventDefault();
            var name = document.getElementById('contactName').value;
            var email = document.getElementById('contactEmail').value;
            var subjectCategory = document.getElementById('contactSubject').value;
            var message = document.getElementById('contactMessage').value;
            
            var recipient = "vyaparvaultpvt@gmail.com";
            var emailSubject = subjectCategory + " - " + name + " (Vyaapar Vault Website Inquiry)";
            var emailBody = "Customer Name: " + name + "
" +
                            "Customer Email: " + email + "
" +
                            "Category: " + subjectCategory + "

" +
                            "Message:
" + message;
                            
            var gmailUrl = "https://mail.google.com/mail/?view=cm&fs=1&to=" + encodeURIComponent(recipient) +
                           "&su=" + encodeURIComponent(emailSubject) +
                           "&body=" + encodeURIComponent(emailBody);
                           
            var successEl = document.getElementById('contactSuccess');
            if (successEl) {
                successEl.innerHTML = "✅ Redirecting to Gmail with draft pre-filled for <strong>vyaparvaultpvt@gmail.com</strong>...";
                successEl.style.display = "block";
            }
            
            var win = window.open(gmailUrl, '_blank');
            if (!win || win.closed || typeof win.closed == 'undefined') {
                window.location.href = gmailUrl;
            }
        }
        </script>
    </div>
    <div style="height: 60px;"></div>
    
'''

# ========== MY ACCOUNT PAGE ==========
account_content = '''
    <!-- My Account Page Content -->
    <style>
        .account-breadcrumb { max-width: 1200px; margin: 0 auto; padding: 20px 15px; font-size: 14px; color: #999; }
        .account-breadcrumb a { color: #333; text-decoration: none; }
        .account-breadcrumb a:hover { color: #2DA815; }
        
        .account-page-wrapper { display: flex; align-items: center; justify-content: center; min-height: 70vh; padding: 40px 20px; background: #f5f6f8; }
        .account-card { background: #fff; border-radius: 20px; box-shadow: 0 8px 40px rgba(0,0,0,0.07); max-width: 460px; width: 100%; padding: 44px 36px; }
        .account-card .ac-logo { text-align: center; margin-bottom: 28px; }
        .account-card .ac-logo img { max-height: 65px; }
        
        .ac-tabs { display: flex; border-bottom: 2px solid #eee; margin-bottom: 28px; }
        .ac-tab { flex: 1; text-align: center; padding: 12px; font-size: 15px; font-weight: 600; color: #888; cursor: pointer; border-bottom: 2px solid transparent; transition: all 0.3s; margin-bottom: -2px; }
        .ac-tab.ac-active { color: #2DA815; border-bottom-color: #2DA815; }
        .ac-tab:hover { color: #2DA815; }
        
        .ac-panel { display: none; }
        .ac-panel.ac-active { display: block; }
        
        .ac-form-group { margin-bottom: 18px; }
        .ac-form-group label { display: block; font-size: 14px; font-weight: 500; margin-bottom: 6px; color: #444; }
        .ac-form-group input {
            width: 100%; padding: 12px 16px; border: 1.5px solid #ddd; border-radius: 10px;
            font-size: 15px; font-family: inherit; transition: border-color 0.3s; background: #fafafa; box-sizing: border-box;
        }
        .ac-form-group input:focus { outline: none; border-color: #2DA815; background: #fff; }
        
        .ac-remember { display: flex; align-items: center; gap: 8px; margin-bottom: 18px; }
        .ac-remember input { width: auto; }
        .ac-remember label { font-size: 14px; color: #666; margin: 0; }
        
        .ac-submit {
            background: linear-gradient(135deg, #2DA815, #1e8a0e); color: #fff; border: none;
            padding: 14px; font-size: 16px; font-weight: 600; border-radius: 10px;
            cursor: pointer; transition: transform 0.2s, box-shadow 0.3s; width: 100%; display: block;
        }
        .ac-submit:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(45,168,21,0.3); }
        
        .ac-forgot { text-align: center; margin-top: 14px; }
        .ac-forgot a { color: #2DA815; text-decoration: none; font-size: 14px; }
        
        .ac-divider { text-align: center; margin: 22px 0; position: relative; }
        .ac-divider::before { content: ''; position: absolute; left: 0; right: 0; top: 50%; height: 1px; background: #eee; }
        .ac-divider span { background: #fff; padding: 0 16px; font-size: 13px; color: #aaa; position: relative; }
        
        .ac-social { display: flex; gap: 12px; }
        .ac-social-btn { flex: 1; padding: 12px; border: 1.5px solid #ddd; border-radius: 10px; background: #fff; font-size: 14px; cursor: pointer; text-align: center; transition: background 0.3s; font-family: inherit; }
        .ac-social-btn:hover { background: #f5f5f5; }
        
        .ac-msg { background: #d4edda; color: #155724; padding: 12px 16px; border-radius: 10px; font-size: 14px; display: none; margin-bottom: 16px; text-align: center; }
        
        @media (max-width: 768px) {
            .account-card { padding: 28px 20px; margin: 0 10px; }
        }
    </style>
    
    <div class="account-breadcrumb"><a href="index.html">Home</a> &nbsp;›&nbsp; My Account</div>
    
    <div class="account-page-wrapper">
        <div class="account-card">
            <div class="ac-logo"><img src="image/logo.png" alt="Vyaapar Vault"></div>
            
            <div class="ac-tabs">
                <div class="ac-tab ac-active" onclick="acSwitch('acLogin',this)">Login</div>
                <div class="ac-tab" onclick="acSwitch('acRegister',this)">Register</div>
            </div>
            
            <div class="ac-msg" id="acMsg"></div>
            
            <div class="ac-panel ac-active" id="acLogin">
                <form onsubmit="event.preventDefault(); acShowMsg('Welcome back! Login successful.');">
                    <div class="ac-form-group">
                        <label>Email Address *</label>
                        <input type="email" placeholder="Enter your email" required>
                    </div>
                    <div class="ac-form-group">
                        <label>Password *</label>
                        <input type="password" placeholder="Enter your password" required>
                    </div>
                    <div class="ac-remember">
                        <input type="checkbox" id="acRem"><label for="acRem">Remember me</label>
                    </div>
                    <button type="submit" class="ac-submit">Log In</button>
                    <div class="ac-forgot"><a href="#">Forgot your password?</a></div>
                </form>
            </div>
            
            <div class="ac-panel" id="acRegister">
                <form onsubmit="event.preventDefault(); acShowMsg('Account created! Welcome to Vyaapar Vault.');">
                    <div class="ac-form-group">
                        <label>Full Name *</label>
                        <input type="text" placeholder="Enter your full name" required>
                    </div>
                    <div class="ac-form-group">
                        <label>Email Address *</label>
                        <input type="email" placeholder="Enter your email" required>
                    </div>
                    <div class="ac-form-group">
                        <label>Phone Number *</label>
                        <input type="tel" placeholder="+91 XXXXX XXXXX" required>
                    </div>
                    <div class="ac-form-group">
                        <label>Password *</label>
                        <input type="password" placeholder="Create a password" required>
                    </div>
                    <button type="submit" class="ac-submit">Create Account</button>
                </form>
            </div>
            

        </div>
    </div>
    
    <script>
    function acSwitch(id, el) {
        document.querySelectorAll('.ac-tab').forEach(t => t.classList.remove('ac-active'));
        document.querySelectorAll('.ac-panel').forEach(p => p.classList.remove('ac-active'));
        el.classList.add('ac-active');
        document.getElementById(id).classList.add('ac-active');
        document.getElementById('acMsg').style.display = 'none';
    }
    function acShowMsg(msg) {
        var m = document.getElementById('acMsg');
        m.textContent = '✅ ' + msg;
        m.style.display = 'block';
    }
    </script>
    
'''

# Generate Contact Us page
contact_page = content[:slideshow_start] + contact_content + content[mobile_menu_start:]
contact_page = contact_page.replace('<title>Vasro Ventures</title>', '<title>Contact Us – Vyaapar Vault</title>')
contact_page = contact_page.replace(
    'current-menu-item current_page_item menu-item-home menu-item-12532 active"><a href="index.html">Home</a>',
    'menu-item-home menu-item-12532"><a href="index.html">Home</a>'
)
contact_page = contact_page.replace(
    'menu-item-12536"><a href="contact-us.html">Contact Us</a>',
    'menu-item-12536 active current-menu-item"><a href="contact-us.html">Contact Us</a>'
)

with open('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/contact-us.html', 'w', encoding='utf-8') as f:
    f.write(contact_page)
print("Contact Us page created successfully!")

# Generate My Account page
account_page = content[:slideshow_start] + account_content + content[mobile_menu_start:]
account_page = account_page.replace('<title>Vasro Ventures</title>', '<title>My Account – Vyaapar Vault</title>')
account_page = account_page.replace(
    'current-menu-item current_page_item menu-item-home menu-item-12532 active"><a href="index.html">Home</a>',
    'menu-item-home menu-item-12532"><a href="index.html">Home</a>'
)
account_page = account_page.replace(
    'menu-item-16042"><a href="my-account.html">My account</a>',
    'menu-item-16042 active current-menu-item"><a href="my-account.html">My account</a>'
)

with open('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/my-account.html', 'w', encoding='utf-8') as f:
    f.write(account_page)
print("My Account page created successfully!")

print("\nAll 3 pages now use the full site theme with matching header, footer, and styling!")
