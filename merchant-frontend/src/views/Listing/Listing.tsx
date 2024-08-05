import React from 'react';
import Box from '@mui/material/Box';

import Main from 'layouts/Main';
import Container from 'components/Container';

import { Headline, Products, SidebarFilters } from './components';
import Newsletter from 'components/Newsletter';

const Listing = (): JSX.Element => {
  return (
    <Main>
      <Box bgcolor={'alternate.main'}>
        <Container paddingY={{ xs: 2, sm: 2.5 }}>
          <Headline />
        </Container>
      </Box>
      <Container>
        <SidebarFilters>
          <Products />
        </SidebarFilters>
      </Container>
      <Box bgcolor={'alternate.main'}>
        <Container>
          <Newsletter />
        </Container>
      </Box>
    </Main>
  );
};

export default Listing;
