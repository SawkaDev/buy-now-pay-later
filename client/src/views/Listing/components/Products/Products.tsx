import React from 'react';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import ProductThumbnail from 'components/ProductThumbnail';
import { getProducts } from 'app/lib/ProductWrapper';
import { useQuery } from '@tanstack/react-query';
import { ProductType } from 'types/products';

const Products = (): JSX.Element => {
  const {
    data: products,
    error,
    isLoading,
  } = useQuery({
    queryKey: ['products'],
    queryFn: getProducts,
  });

  if (isLoading) {
    return <Typography>Loading...</Typography>;
  }

  if (error) {
    return <Typography>Error: {error.message}</Typography>;
  }

  return (
    <Grid container spacing={{ xs: 4, md: 2 }}>
      {products.map((item: ProductType, i: number) => (
        <ProductThumbnail key={i} item={item} />
      ))}
    </Grid>
  );
};

export default Products;
