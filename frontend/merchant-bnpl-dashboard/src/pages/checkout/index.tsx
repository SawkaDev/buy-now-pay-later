import { ReactElement } from 'react';
// material-ui
import { Button, Divider, Grid, Stack, Typography } from '@mui/material';

// types
import { CartCheckoutStateProps } from 'types/cart';

// project imports
import MainCard from 'components/MainCard';
import LoanOption from './LoanOption';
import OrderSummary from 'sections/apps/e-commerce/checkout/OrderSummery';
import Layout from 'layout';

// ==============================|| CART - MAIN ||============================== //

const Cart = () => {
  const loanOptions = [
    <Grid item xs={12} lg={12} pt={2}>
      <LoanOption
        address={{
          building: 'asasdf',
          city: 'asdf',
          country: 'usa',
          destination: 'asdf',
          isDefault: true,
          name: 'mat',
          phone: '10',
          post: '4242',
          state: 'asdf',
          street: 'asdfsd'
        }}
        change={true}
      />
    </Grid>,
    <Grid item xs={12} lg={12} pt={2}>
      <LoanOption
        address={{
          building: 'asasdf',
          city: 'asdf',
          country: 'usa',
          destination: 'asdf',
          isDefault: true,
          name: 'mat',
          phone: '10',
          post: '4242',
          state: 'asdf',
          street: 'asdfsd'
        }}
        change={true}
      />
    </Grid>
  ];

  const checkout: CartCheckoutStateProps = {
    billing: {
      building: 'asdf',
      city: 'asdf',
      country: 'asdf',
      destination: 'asdf',
      isDefault: true,
      name: 'asdf',
      phone: 'asdf',
      post: 'asdf',
      state: 'asdf',
      street: 'asdf'
    },
    discount: 10,
    payment: { card: 'asdf', method: 'asdf', type: 'sadfds' },
    products: [],
    shipping: 23,
    step: 1,
    subtotal: 100,
    total: 100
  };
  return (
    <Grid container spacing={3}>
      <Grid item xs={12} md={8}>
        <Stack spacing={2}>
          <MainCard content={false}>
            <Grid container>
              <Grid item xs={12} sx={{ py: 2.5, pl: 2.5 }}>
                <Stack direction="row" alignItems="center" spacing={1}>
                  <Typography variant="subtitle1">Loan Options</Typography>
                </Stack>
              </Grid>
              <Grid item xs={12}>
                <Divider />
              </Grid>
              <Grid item xs={12} sx={{ p: 2.5 }}>
                {loanOptions}
              </Grid>
            </Grid>
          </MainCard>
        </Stack>
      </Grid>
      <Grid item xs={12} md={4}>
        <Stack spacing={3}>
          <OrderSummary checkout={checkout} show />
          <Button variant="contained" sx={{ textTransform: 'none' }} fullWidth>
            Requets Loan
          </Button>
        </Stack>
      </Grid>
    </Grid>
  );
};

Cart.getLayout = function getLayout(page: ReactElement) {
  return <Layout variant='component'>{page}</Layout>;
};

export default Cart;
