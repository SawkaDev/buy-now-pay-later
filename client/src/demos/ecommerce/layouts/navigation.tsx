const pages = [
  {
    title: 'Home',
    href: '/',
    id: 'demo__ecommerece-home',
  },
  {
    title: 'Listing',
    id: 'demo__ecommerece-listing',
    children: [
      {
        title: 'Search Listing',
        href: '/listing',
        id: 'demo__ecommerece-listing--search',
      },
      {
        title: 'Promotions',
        href: '/promotions',
        id: 'demo__ecommerece-listing--promotions',
      },
    ],
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
