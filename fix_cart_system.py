import os
import re

root_dir = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com'

# 1. Write standalone cart-drawer.js
js_dir = os.path.join(root_dir, 'js')
os.makedirs(js_dir, exist_ok=True)
cart_js_path = os.path.join(js_dir, 'cart-drawer.js')

cart_js_code = """/* Vyapar Vault Shopping Cart & Toast System */
(function() {
    function getCart() {
        try {
            return JSON.parse(localStorage.getItem('vyapar_cart_items')) || [];
        } catch (e) {
            return [];
        }
    }

    function saveCart(cart) {
        localStorage.setItem('vyapar_cart_items', JSON.stringify(cart));
        updateCartBadgeCount();
    }

    function updateCartBadgeCount() {
        const cart = getCart();
        const totalQty = cart.reduce((sum, item) => sum + item.quantity, 0);
        const counters = document.querySelectorAll('.cart-counter, .counter, .header-cart-count');
        counters.forEach(counter => {
            counter.textContent = totalQty;
            if (totalQty > 0) {
                counter.classList.remove('hidden');
                counter.style.display = 'inline-flex';
            } else {
                counter.style.display = 'none';
            }
        });
    }

    window.addToVyaparCart = function(event, title, price, image) {
        if (event) {
            event.preventDefault();
            event.stopPropagation();
        }

        const cart = getCart();
        const existingIndex = cart.findIndex(item => item.title === title);

        if (existingIndex > -1) {
            cart[existingIndex].quantity += 1;
        } else {
            cart.push({
                title: title,
                price: price,
                image: image,
                quantity: 1
            });
        }

        saveCart(cart);

        // Visual feedback on clicked button
        let targetBtn = null;
        if (event && event.target) {
            targetBtn = event.target.closest('a, button');
        }
        if (targetBtn) {
            const origText = targetBtn.innerText;
            targetBtn.innerText = '✓ Added!';
            targetBtn.style.background = '#2e7d32';
            targetBtn.style.color = '#ffffff';
            setTimeout(() => {
                targetBtn.innerText = origText;
                targetBtn.style.background = '#1f1f1f';
                targetBtn.style.color = '#ffffff';
            }, 1500);
        }

        // Show Toast Notification
        showVyaparToast(title, price, image);

        // Update drawer if active
        if (document.getElementById('vyapar-cart-drawer')?.classList.contains('active')) {
            renderCartDrawer();
        }

        return false;
    };

    window.showVyaparToast = function(title, price, image) {
        let toastContainer = document.getElementById('vyapar-toast-container');
        if (!toastContainer) {
            toastContainer = document.createElement('div');
            toastContainer.id = 'vyapar-toast-container';
            document.body.appendChild(toastContainer);
        }

        const toast = document.createElement('div');
        toast.className = 'vyapar-toast-item';
        toast.innerHTML = `
            <div class="vyapar-toast-icon">✓</div>
            <img src="${image}" class="vyapar-toast-img" alt="${title}" onerror="this.src='image/logo.png'">
            <div class="vyapar-toast-details">
                <div class="vyapar-toast-status">Added to Cart!</div>
                <div class="vyapar-toast-title">${title}</div>
                <div class="vyapar-toast-price">${price}</div>
            </div>
            <button class="vyapar-toast-view-btn" onclick="openVyaparCartDrawer(); closeVyaparToast(this);">View Cart</button>
            <button class="vyapar-toast-close" onclick="closeVyaparToast(this)">&times;</button>
        `;

        toastContainer.appendChild(toast);

        setTimeout(() => {
            if (toast.parentNode) {
                toast.classList.add('fade-out');
                setTimeout(() => toast.remove(), 400);
            }
        }, 3500);
    };

    window.closeVyaparToast = function(btn) {
        const item = btn.closest('.vyapar-toast-item');
        if (item) {
            item.classList.add('fade-out');
            setTimeout(() => item.remove(), 300);
        }
    };

    window.openVyaparCartDrawer = function() {
        ensureCartDrawerMarkup();
        renderCartDrawer();
        document.getElementById('vyapar-cart-backdrop').classList.add('active');
        document.getElementById('vyapar-cart-drawer').classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    window.closeVyaparCartDrawer = function() {
        const backdrop = document.getElementById('vyapar-cart-backdrop');
        const drawer = document.getElementById('vyapar-cart-drawer');
        if (backdrop) backdrop.classList.remove('active');
        if (drawer) drawer.classList.remove('active');
        document.body.style.overflow = '';
    };

    window.updateVyaparQuantity = function(index, change) {
        const cart = getCart();
        if (cart[index]) {
            cart[index].quantity += change;
            if (cart[index].quantity <= 0) {
                cart.splice(index, 1);
            }
            saveCart(cart);
            renderCartDrawer();
        }
    };

    window.removeVyaparCartItem = function(index) {
        const cart = getCart();
        if (cart[index]) {
            cart.splice(index, 1);
            saveCart(cart);
            renderCartDrawer();
        }
    };

    window.clearVyaparCart = function() {
        saveCart([]);
        renderCartDrawer();
    };

    function ensureCartDrawerMarkup() {
        if (document.getElementById('vyapar-cart-drawer')) return;

        const backdrop = document.createElement('div');
        backdrop.id = 'vyapar-cart-backdrop';
        backdrop.onclick = window.closeVyaparCartDrawer;
        document.body.appendChild(backdrop);

        const drawer = document.createElement('div');
        drawer.id = 'vyapar-cart-drawer';
        drawer.innerHTML = `
            <div class="vyapar-cart-header">
                <h3>Shopping Cart <span id="vyapar-drawer-count-badge">(0)</span></h3>
                <button class="vyapar-cart-close-btn" onclick="closeVyaparCartDrawer()">&times;</button>
            </div>
            <div class="vyapar-cart-body" id="vyapar-cart-body"></div>
            <div class="vyapar-cart-footer" id="vyapar-cart-footer"></div>
        `;
        document.body.appendChild(drawer);
    }

    function parsePriceNum(priceStr) {
        if (!priceStr) return 0;
        const cleaned = priceStr.toString().replace(/[^0-9.]/g, '');
        return parseFloat(cleaned) || 0;
    }

    function renderCartDrawer() {
        const cart = getCart();
        const bodyEl = document.getElementById('vyapar-cart-body');
        const footerEl = document.getElementById('vyapar-cart-footer');
        const badgeEl = document.getElementById('vyapar-drawer-count-badge');

        const totalQty = cart.reduce((sum, item) => sum + item.quantity, 0);
        if (badgeEl) badgeEl.textContent = `(${totalQty})`;

        if (cart.length === 0) {
            if (bodyEl) {
                bodyEl.innerHTML = `
                    <div class="vyapar-cart-empty">
                        <div class="vyapar-empty-icon">🛒</div>
                        <h4>Your Cart is Empty</h4>
                        <p>Explore our premium cleaning products and add your favorites to the cart!</p>
                        <a href="#shop-section" onclick="closeVyaparCartDrawer()" class="vyapar-shop-now-btn">Start Shopping</a>
                    </div>
                `;
            }
            if (footerEl) footerEl.innerHTML = '';
            return;
        }

        let totalAmount = 0;
        let itemsHtml = '';

        cart.forEach((item, index) => {
            const unitPrice = parsePriceNum(item.price);
            const itemTotal = unitPrice * item.quantity;
            totalAmount += itemTotal;

            itemsHtml += `
                <div class="vyapar-cart-item">
                    <img src="${item.image}" class="vyapar-item-img" alt="${item.title}" onerror="this.src='image/logo.png'">
                    <div class="vyapar-item-info">
                        <div class="vyapar-item-title">${item.title}</div>
                        <div class="vyapar-item-price">${item.price}</div>
                        <div class="vyapar-item-qty-row">
                            <button class="vyapar-qty-btn" onclick="updateVyaparQuantity(${index}, -1)">-</button>
                            <span class="vyapar-qty-val">${item.quantity}</span>
                            <button class="vyapar-qty-btn" onclick="updateVyaparQuantity(${index}, 1)">+</button>
                            <button class="vyapar-remove-btn" onclick="removeVyaparCartItem(${index})" title="Remove item">🗑 Remove</button>
                        </div>
                    </div>
                    <div class="vyapar-item-total">₹${itemTotal.toLocaleString('en-IN', {minimumFractionDigits:2, maximumFractionDigits:2})}</div>
                </div>
            `;
        });

        if (bodyEl) bodyEl.innerHTML = itemsHtml;

        if (footerEl) {
            footerEl.innerHTML = `
                <div class="vyapar-cart-subtotal-row">
                    <span>Subtotal:</span>
                    <span class="vyapar-subtotal-val">₹${totalAmount.toLocaleString('en-IN', {minimumFractionDigits:2, maximumFractionDigits:2})}</span>
                </div>
                <div class="vyapar-shipping-notice">🚚 <strong>FREE Express Shipping</strong> on all orders!</div>
                <div class="vyapar-cart-actions">
                    <button class="vyapar-checkout-btn" onclick="alert('Thank you for ordering with Vyapar Vault! Proceeding to Checkout...'); closeVyaparCartDrawer();">Proceed to Checkout</button>
                    <button class="vyapar-clear-btn" onclick="clearVyaparCart()">Clear Cart</button>
                </div>
            `;
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initBindings);
    } else {
        initBindings();
    }

    function initBindings() {
        updateCartBadgeCount();
        document.querySelectorAll('.header-cart a, [data-target="cart-modal"], .icon-cart').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                openVyaparCartDrawer();
            });
        });
    }
})();
"""

with open(cart_js_path, 'w', encoding='utf-8') as f:
    f.write(cart_js_code)
print(f"Created {cart_js_path}")

# 2. Add Cart Styles into HTML files or separate CSS
cart_css_code = """
<style id="custom-vyapar-cart-styles">
/* Toast Notification Styling */
#vyapar-toast-container {
    position: fixed;
    bottom: 25px;
    right: 25px;
    z-index: 999999;
    display: flex;
    flex-direction: column;
    gap: 12px;
    pointer-events: none;
}
.vyapar-toast-item {
    pointer-events: auto;
    background: #1f1f1f;
    color: #ffffff;
    padding: 14px 18px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
    display: flex;
    align-items: center;
    gap: 14px;
    min-width: 320px;
    max-width: 420px;
    animation: vyaparSlideIn 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    transition: opacity 0.3s ease, transform 0.3s ease;
    border: 1px solid rgba(255,255,255,0.1);
}
.vyapar-toast-item.fade-out {
    opacity: 0;
    transform: translateY(15px);
}
@keyframes vyaparSlideIn {
    from { opacity: 0; transform: translateY(30px) scale(0.95); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}
.vyapar-toast-icon {
    width: 28px;
    height: 28px;
    background: #2e7d32;
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 14px;
    flex-shrink: 0;
}
.vyapar-toast-img {
    width: 48px;
    height: 48px;
    object-fit: contain;
    background: #fff;
    border-radius: 8px;
    padding: 4px;
    flex-shrink: 0;
}
.vyapar-toast-details {
    flex-grow: 1;
    overflow: hidden;
}
.vyapar-toast-status {
    font-size: 11px;
    color: #81c784;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.vyapar-toast-title {
    font-size: 13px;
    font-weight: 600;
    color: #ffffff !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-top: 2px;
}
.vyapar-toast-price {
    font-size: 13px;
    font-weight: 700;
    color: #ffb400 !important;
    margin-top: 1px;
}
.vyapar-toast-view-btn {
    background: #ffffff;
    color: #1f1f1f !important;
    border: none;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    white-space: nowrap;
    transition: background 0.2s;
}
.vyapar-toast-view-btn:hover {
    background: #f0f0f0;
}
.vyapar-toast-close {
    background: transparent;
    border: none;
    color: #888;
    font-size: 20px;
    cursor: pointer;
    padding: 0 4px;
    line-height: 1;
}
.vyapar-toast-close:hover {
    color: #fff;
}

/* Slide-over Cart Drawer */
#vyapar-cart-backdrop {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(3px);
    z-index: 999990;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
}
#vyapar-cart-backdrop.active {
    opacity: 1;
    visibility: visible;
}
#vyapar-cart-drawer {
    position: fixed;
    top: 0; right: -420px; bottom: 0;
    width: 400px;
    max-width: 90vw;
    background: #ffffff;
    box-shadow: -5px 0 25px rgba(0,0,0,0.15);
    z-index: 999995;
    display: flex;
    flex-direction: column;
    transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
#vyapar-cart-drawer.active {
    right: 0;
}
.vyapar-cart-header {
    padding: 20px;
    background: #1f1f1f;
    color: #ffffff;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.vyapar-cart-header h3 {
    margin: 0;
    font-size: 18px;
    font-weight: 700;
    color: #ffffff !important;
}
#vyapar-drawer-count-badge {
    font-size: 14px;
    color: #ffb400;
    margin-left: 6px;
}
.vyapar-cart-close-btn {
    background: transparent;
    border: none;
    color: #ffffff;
    font-size: 26px;
    cursor: pointer;
    line-height: 1;
}
.vyapar-cart-body {
    flex-grow: 1;
    overflow-y: auto;
    padding: 20px;
}
.vyapar-cart-empty {
    text-align: center;
    padding: 60px 20px;
}
.vyapar-empty-icon {
    font-size: 48px;
    margin-bottom: 15px;
}
.vyapar-cart-empty h4 {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 8px;
}
.vyapar-cart-empty p {
    color: #666;
    font-size: 13px;
    margin-bottom: 20px;
}
.vyapar-shop-now-btn {
    display: inline-block;
    background: #1f1f1f;
    color: #fff !important;
    padding: 10px 24px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
}
.vyapar-cart-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 0;
    border-bottom: 1px solid #f0f0f0;
}
.vyapar-item-img {
    width: 60px;
    height: 60px;
    object-fit: contain;
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 4px;
}
.vyapar-item-info {
    flex-grow: 1;
}
.vyapar-item-title {
    font-size: 13px;
    font-weight: 600;
    color: #1f1f1f !important;
    margin-bottom: 4px;
    line-height: 1.3;
}
.vyapar-item-price {
    font-size: 13px;
    color: #666;
    margin-bottom: 6px;
}
.vyapar-item-qty-row {
    display: flex;
    align-items: center;
    gap: 8px;
}
.vyapar-qty-btn {
    width: 24px;
    height: 24px;
    background: #f0f0f0;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}
.vyapar-qty-val {
    font-size: 13px;
    font-weight: 600;
    min-width: 16px;
    text-align: center;
}
.vyapar-remove-btn {
    background: transparent;
    border: none;
    color: #d32f2f;
    font-size: 11px;
    cursor: pointer;
    margin-left: 8px;
}
.vyapar-item-total {
    font-weight: 700;
    font-size: 14px;
    color: #1f1f1f;
}
.vyapar-cart-footer {
    padding: 20px;
    border-top: 1px solid #eee;
    background: #f9f9f9;
}
.vyapar-cart-subtotal-row {
    display: flex;
    justify-content: space-between;
    font-size: 16px;
    font-weight: 700;
    color: #1f1f1f;
    margin-bottom: 10px;
}
.vyapar-subtotal-val {
    color: #000;
}
.vyapar-shipping-notice {
    font-size: 12px;
    color: #2e7d32;
    background: #e8f5e9;
    padding: 8px 12px;
    border-radius: 6px;
    margin-bottom: 15px;
    text-align: center;
}
.vyapar-cart-actions {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.vyapar-checkout-btn {
    width: 100%;
    padding: 12px;
    background: #1f1f1f;
    color: #ffffff !important;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: 14px;
    cursor: pointer;
    transition: background 0.2s;
}
.vyapar-checkout-btn:hover {
    background: #333333;
}
.vyapar-clear-btn {
    background: transparent;
    border: none;
    color: #777;
    font-size: 12px;
    cursor: pointer;
    text-decoration: underline;
}
</style>
<script src="js/cart-drawer.js"></script>
"""

# 3. Update update_site.py
update_site_path = os.path.join(root_dir, 'update_site.py')
if os.path.exists(update_site_path):
    with open(update_site_path, 'r', encoding='utf-8') as f:
        us_content = f.read()
    us_content = us_content.replace(
        "onclick=\"alert('Added {p['title']} to cart!'); return false;\"",
        "onclick=\"addToVyaparCart(event, '{p['title']}', '{p['price']}', '{p['image']}'); return false;\""
    )
    with open(update_site_path, 'w', encoding='utf-8') as f:
        f.write(us_content)
    print("Updated update_site.py")

# 4. Helper function to replace alert() in product cards in HTML files
def process_html_file(file_name):
    path = os.path.join(root_dir, file_name)
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace alert('Added ... to cart!')
    def alert_replacer(m):
        item_title = m.group(1)
        safe_title = item_title.replace("'", "\\'")
        return f'onclick="addToVyaparCart(event, \'{safe_title}\', \'₹299.00\', \'image/shopping.webp\'); return false;"'

    alert_pattern = re.compile(r'onclick="alert\(\'Added ([^\']+?) to cart!\'\); return false;"')
    new_html = alert_pattern.sub(alert_replacer, new_html if 'new_html' in locals() else html)

    # Inject cart_css_code before </head> if not already present
    if '</head>' in new_html and 'id="custom-vyapar-cart-styles"' not in new_html:
        new_html = new_html.replace('</head>', f'{cart_css_code}\n</head>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Processed {file_name}")

for html_name in ['index.html', 'shop.html', 'shop-2.html', 'about-us.html', 'contact-us.html', 'my-account.html']:
    process_html_file(html_name)

print("Cart fix applied successfully to all HTML files!")
