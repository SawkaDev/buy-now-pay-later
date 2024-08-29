import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';

import Main from 'layouts/Main';
import Container from 'components/Container';

import { Orders, SummeryBox } from './components';
import { useCart } from 'contexts/CartContext';
import EmptyCart from 'views/EmptyCart';

const Cart = (): JSX.Element => {
  const { items } = useCart();

  const total = items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0,
  );

  if (items.length == 0) {
    return <EmptyCart />;
  }

  return (
    <Main>
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          minHeight: '100vh',
        }}
      >
        <Box sx={{ flexGrow: 1 }}>
          <Container>
            <Box>
              <Grid container spacing={4}>
                <Grid item xs={12} md={8}>
                  <Typography variant="h6" fontWeight={700} marginBottom={4}>
                    Shopping Cart
                  </Typography>
                  <Orders items={items} />
                </Grid>
                <Grid item xs={12} md={4}>
                  <Card
                    elevation={0}
                    sx={{
                      bgcolor: 'alternate.main',
                      padding: { xs: 2, sm: 4 },
                    }}
                  >
                    <Typography variant="h6" fontWeight={700} marginBottom={4}>
                      Order summary
                    </Typography>
                    <SummeryBox subTotal={total} />
                  </Card>
                </Grid>
              </Grid>
            </Box>
          </Container>
        </Box>
      </Box>
    </Main>
  );
};

export default Cart;
