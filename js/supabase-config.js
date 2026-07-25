/* Vyapar Vault Supabase & Order Sync Module */
const SUPABASE_URL = 'https://vxykfgwwceunkwipavfn.supabase.co';
const SUPABASE_KEY = 'sb_publishable_4FzRJqCsGY2PtGl7ciRLOA_kkTLfgZJ';

let supabaseClient = null;

if (window.supabase) {
    try {
        supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
        console.log('Supabase Realtime Client Initialized');
    } catch (err) {
        console.warn('Supabase Client init fallback:', err);
    }
}

// Local fallback helper for orders
function getLocalOrders() {
    try {
        return JSON.parse(localStorage.getItem('vyapar_all_orders')) || [];
    } catch (e) {
        return [];
    }
}

function saveLocalOrder(order) {
    const orders = getLocalOrders();
    orders.unshift(order);
    localStorage.setItem('vyapar_all_orders', JSON.stringify(orders));
    return orders;
}

function updateLocalOrderStatus(orderId, newStatus) {
    const orders = getLocalOrders();
    const target = orders.find(o => o.id === orderId);
    if (target) {
        target.status = newStatus;
        localStorage.setItem('vyapar_all_orders', JSON.stringify(orders));
    }
    return orders;
}

// Global Order Submission Handler
window.createVyaparOrder = async function(customerDetails, cartItems, totalAmount, paymentMethod = 'COD') {
    const orderId = 'VV-' + Math.floor(100000 + Math.random() * 900000);
    const orderDate = new Date().toISOString();

    const orderData = {
        id: orderId,
        created_at: orderDate,
        customer_name: customerDetails.name,
        customer_email: customerDetails.email,
        customer_phone: customerDetails.phone,
        address: `${customerDetails.address}, ${customerDetails.city} - ${customerDetails.pincode}`,
        city: customerDetails.city,
        pincode: customerDetails.pincode,
        payment_method: paymentMethod,
        items: cartItems,
        items_count: cartItems.reduce((sum, i) => sum + i.quantity, 0),
        total_amount: totalAmount,
        status: 'Pending'
    };

    // Save locally first for instant responsiveness
    saveLocalOrder(orderData);

    // Sync to Supabase
    if (supabaseClient) {
        try {
            const { data, error } = await supabaseClient
                .from('orders')
                .insert([orderData]);

            if (error) {
                console.warn('Supabase DB Insert note:', error.message);
            } else {
                console.log('Order successfully inserted into Supabase DB:', data);
            }
        } catch (e) {
            console.warn('Supabase async sync note:', e);
        }
    }

    return orderData;
};

// Global Order Fetcher for Admin Dashboard
window.fetchVyaparOrders = async function() {
    let orders = getLocalOrders();

    if (supabaseClient) {
        try {
            const { data, error } = await supabaseClient
                .from('orders')
                .select('*')
                .order('created_at', { ascending: false });

            if (!error && data && data.length > 0) {
                // Merge Supabase orders with local orders
                const map = new Map();
                orders.forEach(o => map.set(o.id, o));
                data.forEach(o => map.set(o.id, o));
                orders = Array.from(map.values()).sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
                localStorage.setItem('vyapar_all_orders', JSON.stringify(orders));
            }
        } catch (e) {
            console.warn('Supabase fetch note:', e);
        }
    }

    return orders;
};

// Update Order Status Helper
window.updateOrderStatusInDB = async function(orderId, newStatus) {
    updateLocalOrderStatus(orderId, newStatus);

    if (supabaseClient) {
        try {
            await supabaseClient
                .from('orders')
                .update({ status: newStatus })
                .eq('id', orderId);
        } catch (e) {
            console.warn('Supabase update note:', e);
        }
    }
};
