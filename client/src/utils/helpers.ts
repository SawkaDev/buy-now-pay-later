import { products } from 'types/products';

export function findProductById(id: number) {
  return products.find((product) => product.id === id);
}
