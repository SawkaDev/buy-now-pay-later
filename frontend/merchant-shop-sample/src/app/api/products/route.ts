// app/api/products/route.ts
import { NextResponse } from 'next/server';
import products from './products.json';

export async function GET() {
  try {
    // Read and parse the JSON file
    return NextResponse.json(products);
  } catch (error) {
    console.error('Error reading products:', error);
    return NextResponse.json(
      { error: 'Unable to fetch products' },
      { status: 500 },
    );
  }
}
