export async function getProduct(id: string) {
  const res = await fetch(`http://localhost:3000/api/products/${id}`);

  if (!res.ok) {
    throw new Error('Failed to fetch product');
  }

  return res.json();
}

export async function getProducts() {
  const res = await fetch('http://localhost:3000/api/products');

  if (!res.ok) {
    throw new Error('Failed to fetch products');
  }
  return res.json();
}
