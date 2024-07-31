// app/api/products/[id]/route.ts
import { NextResponse } from 'next/server';
import products from '../products.json';

export async function GET(
  request: Request,
  { params }: { params: { id: string } },
) {
  try {
    const id = parseInt(params.id);
    const product = products.find((p: any) => p.id === id);
    if (product) {
      return NextResponse.json(product);
    } else {
      return NextResponse.json({ error: 'Product not found' }, { status: 404 });
    }
  } catch (error) {
    console.error('Error reading product:', error);
    return NextResponse.json(
      { error: 'Unable to fetch product' },
      { status: 500 },
    );
  }
}
