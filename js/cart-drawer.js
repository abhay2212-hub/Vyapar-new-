/* Vyapar Vault Shopping Cart & Toast System */
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

    window.addToVyaparCart = function(event, title, price, image, quantity = 1) {
        if (event) {
            event.preventDefault();
            event.stopPropagation();
        }

        const qty = parseInt(quantity) || 1;
        const cart = getCart();
        const existingIndex = cart.findIndex(item => item.title === title);

        if (existingIndex > -1) {
            cart[existingIndex].quantity += qty;
        } else {
            cart.push({
                title: title,
                price: price,
                image: image,
                quantity: qty
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
            <button class="vyapar-toast-view-btn" onclick="window.location.href='cart.html'">View Cart</button>
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
        window.location.href = 'cart.html';
    };

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
                window.location.href = 'cart.html';
            });
        });
    }
})();
