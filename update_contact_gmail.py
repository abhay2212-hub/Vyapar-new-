import re

contact_html_file = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/contact-us.html'
script_file = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/create_other_pages.py'

new_form_html = '''<div class="contact-form-section">
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
            var emailBody = "Customer Name: " + name + "\\n" +
                            "Customer Email: " + email + "\\n" +
                            "Category: " + subjectCategory + "\\n\\n" +
                            "Message:\\n" + message;
                            
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
        </script>'''

# 1. Update contact-us.html
with open(contact_html_file, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

old_section_pattern = re.compile(r'<div class="contact-form-section">.*?</div>\s*</div>\s*<div style="height: 60px;"></div>', re.DOTALL)

updated_content = old_section_pattern.sub(new_form_html + '\n    </div>\n    <div style="height: 60px;"></div>', content)

with open(contact_html_file, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Updated contact-us.html with Gmail redirect functionality.")

# 2. Also update create_other_pages.py
with open(script_file, 'r', encoding='utf-8', errors='ignore') as f:
    script_content = f.read()

script_updated = old_section_pattern.sub(new_form_html + '\n    </div>\n    <div style="height: 60px;"></div>', script_content)

with open(script_file, 'w', encoding='utf-8') as f:
    f.write(script_updated)

print("Updated create_other_pages.py script template.")
