import React from 'react';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Grid from '@mui/material/Grid';

import { Headline, Image, Details } from './components';

import Main from 'layouts/Main';
import Container from 'components/Container';
import Newsletter from 'components/Newsletter';
import NotFoundPage from 'app/not-found';
import { getProduct } from 'app/lib/ProductWrapper';
import { useQuery } from '@tanstack/react-query';
import TrendingItems from 'components/TrendingItems';

interface ProductOverviewProps {
  slug: string;
}

const ProductOverview = ({ slug }: ProductOverviewProps) => {
  const {
    data: product,
    error,
    isLoading,
  } = useQuery({
    queryKey: ['product', slug],
    queryFn: () => getProduct(slug),
  });

  if (isLoading) {
    return <div></div>;
  }

  if (error || !product) {
    return <NotFoundPage />;
  }

  return (
    <Main>
      <Box bgcolor={'alternate.main'}>
        <Container paddingY={{ xs: 2, sm: 2.5 }}>
          <Headline />
        </Container>
      </Box>
      <Container>
        <Box>
          <Grid container spacing={{ xs: 2, md: 4 }}>
            <Grid item xs={12} md={7}>
              <Image image={product.media} title={product.title} />
            </Grid>
            <Grid item xs={12} md={5}>
              <Details product={product} />
            </Grid>
          </Grid>
        </Box>
      </Container>
      <Container paddingY={0}>
        <Divider />
      </Container>
      <Container>
        <TrendingItems />
      </Container>
      <Box bgcolor={'alternate.main'}>
        <Container>
          <Newsletter />
        </Container>
      </Box>
    </Main>
  );
};

export default ProductOverview;
