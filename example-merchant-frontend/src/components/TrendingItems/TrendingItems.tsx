import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import ProductThumbnail from 'components/ProductThumbnail/ProductThumbnail';
import { getProducts } from 'app/lib/ProductWrapper';
import { useQuery } from '@tanstack/react-query';

const TrendingItems = (): JSX.Element => {
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
    <Box>
      <Box marginBottom={4}>
        <Typography variant={'h5'} fontWeight={700}>
          Trending products
        </Typography>
      </Box>
      <Grid container spacing={4}>
        {products.map((item, i) => (
          <ProductThumbnail key={i} item={item} rowSize={3} />
        ))}
      </Grid>
    </Box>
  );
};

export default TrendingItems;
