import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import { products } from 'types/products';
import ProductThumbnail from 'components/ProductThumbnail/ProductThumbnail';

const TrendingItems = (): JSX.Element => {
  return (
    <Box>
      <Box marginBottom={4}>
        <Typography variant={'h5'} fontWeight={700}>
          Trending products
        </Typography>
      </Box>
      <Grid container spacing={4}>
        {products.map((item, i) => (
          <ProductThumbnail key={i} item={item} />
        ))}
      </Grid>
    </Box>
  );
};

export default TrendingItems;
