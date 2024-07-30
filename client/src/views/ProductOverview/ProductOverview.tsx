// 'use client'; // This is a client component 👈🏽

import React from 'react';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Grid from '@mui/material/Grid';

import { Headline, Image, Details } from './components';

import Main from 'layouts/Main';
import Container from 'components/Container';
import Newsletter from 'components/Newsletter';
import { useParams } from 'next/navigation';
import { findProductById } from 'utils/helpers';
import NotFoundPage from 'app/not-found';
import { TrendingItems } from 'views/IndexView/components';

const ProductOverview = (): JSX.Element => {
  const router = useParams();

  // This would normally be an API call to database
  let product: any = undefined;
  if (router && router.slug) {
    product = findProductById(parseInt(router.slug as string));
  }

  if (!product) {
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
              <Details
                title={product.title}
                description={product.description}
                price={product.price}
              />
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
