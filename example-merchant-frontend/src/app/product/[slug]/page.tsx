'use client'; // This is a client component 👈🏽

import { useParams } from 'next/navigation';
import React from 'react';
import ProductOverviewView from 'views/ProductOverview';
import NotFoundPage from 'app/not-found'; // Adjust the import path as needed

const ProductOverviewPage = (): JSX.Element => {
  const params = useParams();

  // Check if slug exists and is a string
  if (!params || typeof params.slug !== 'string') {
    return <NotFoundPage />;
  }

  // If we reach here, we know slug is a string
  return <ProductOverviewView slug={params.slug} />;
};

export default ProductOverviewPage;
