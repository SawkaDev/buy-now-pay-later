const pages = [
  {
    title: 'Home',
    href: '/',
    id: 'demo__ecommerece-home',
  },
  {
    title: 'Shop',
    id: 'demo__ecommerece-listing',
    href: '/listing',
  },
  {
    title: 'Product Overview',
    href: '/product-overview',
    id: 'demo__ecommerece-product-overview',
  },
  {
    title: 'Pages',
    id: 'demo__ecommerece-pages',
    children: [
      {
        title: 'Cart',
        href: '/cart',
        id: 'demo__ecommerece-pages--cart',
      },
      {
        title: 'Checkout',
        href: '/checkout',
        id: 'demo__ecommerece-pages--checkout',
      },
      {
        title: 'Empty Cart',
        href: '/empty-cart',
        id: 'demo__ecommerece-pages--empty-cart',
      },
      {
        title: 'Order Complete',
        href: '/order-complete',
        id: 'demo__ecommerece-pages--order-complete',
      },
    ],
  },
];

export default pages;
