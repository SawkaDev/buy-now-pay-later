export interface ProductType {
  id: number;
  media: string;
  title: string;
  description: string;
  price: number;
  oldPrice?: number;
  isNew: boolean;
}

export const products: Array<ProductType> = [
  {
    id: 1,
    media: 'https://assets.maccarianagency.com/backgrounds/img56.jpg',
    title: 'Adidas Shoes',
    description: 'Discover the new collection of Adidas.',
    price: 69.9,
    isNew: true,
  },
  {
    id: 2,
    media: 'https://assets.maccarianagency.com/backgrounds/img59.jpg',
    title: 'Black Jeans',
    description: 'Discover the new collection of Black jeans.',
    price: 59.8,
    oldPrice: 101.9,
    isNew: true,
  },
  {
    id: 3,
    media: 'https://assets.maccarianagency.com/backgrounds/img61.jpg',
    title: 'Skiny Jeans',
    description: 'Discover the new collection of Skiny jeans.',
    price: 53.25,
    oldPrice: 81.24,
    isNew: true,
  },
  {
    id: 4,
    media: 'https://assets.maccarianagency.com/backgrounds/img63.jpg',
    title: 'Colorful Shoes',
    description: 'Colorful shoes designed for everyone.',
    price: 39.9,
    oldPrice: 60,
    isNew: true,
  },
];
