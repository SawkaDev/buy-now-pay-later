import React from 'react';
import Box from '@mui/material/Box';

import Main from 'layouts/Main';
import Container from 'components/Container';

import { PromoGrid, Features } from './components';
import TrendingItems from 'components/TrendingItems';

const IndexView = (): JSX.Element => {
  return (
    <Main>
      <Box bgcolor={'alternate.main'}>
        <Container>
          <PromoGrid />
        </Container>
      </Box>
      <Container>
        <Features />
      </Container>
      <Box bgcolor={'alternate.main'}>
        <Container>
          <TrendingItems />
        </Container>
      </Box>
    </Main>
  );
};

export default IndexView;
