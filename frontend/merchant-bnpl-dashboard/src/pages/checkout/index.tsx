import { ReactElement, useState } from 'react';
import { Button, Divider, Grid, Stack, Tabs, Typography } from '@mui/material';
import MainCard from 'components/MainCard';
import LoanOption from './LoanOption';
import Layout from 'layout';
import { useTheme } from '@mui/material/styles';
import Page from 'components/Page';
import { LoanApplicationInterface } from 'types/LoanApplication';
import LoanSummary from 'sections/apps/e-commerce/checkout/LoanSummary';
import { StyledTab, TabPanel, tabsOption } from './tabs/tab_helper';
import { CheckOutlined } from '@ant-design/icons';
import Avatar from 'components/@extended/Avatar';
import UserLogin from './tabs/UserLogin';

// ==============================|| CART - MAIN ||============================== //

const Cart = () => {
  const [value, setValue] = useState(0);
  const theme = useTheme();

  const onNext = () => {
    setValue((index) => index + 1);
  };

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

  const selectedLoan: LoanApplicationInterface = {
    interest: 10,
    loanAmount: 100,
    loanTermMonths: 5,
    merchant: 'Sample Merchant'
  };

  return (
    <Page title="Checkout">
      <Stack spacing={2}>
        <MainCard content={false}>
          <Grid container spacing={3}>
            <Grid item xs={12}>
              <Tabs
                value={value}
                aria-label="icon label tabs example"
                variant="scrollable"
                sx={{
                  '& .MuiTabs-flexContainer': {
                    borderBottom: 'none'
                  },
                  '& .MuiTabs-indicator': {
                    display: 'none'
                  },
                  '& .MuiButtonBase-root + .MuiButtonBase-root': {
                    position: 'relative',
                    overflow: 'visible',
                    ml: 2,
                    '&:after': {
                      content: '""',
                      bgcolor: '#ccc',
                      width: 1,
                      height: 'calc(100% - 16px)',
                      position: 'absolute',
                      top: 8,
                      left: -8
                    }
                  }
                }}
              >
                {tabsOption.map((tab, index) => (
                  <StyledTab
                    theme={theme}
                    value={index}
                    disabled={index > value}
                    key={index}
                    label={
                      <Grid container>
                        <Stack direction="row" alignItems="center" spacing={1}>
                          <Avatar type={index !== value ? 'combined' : 'filled'} size="xs" color={index > value ? 'secondary' : 'primary'}>
                            {index === value ? index + 1 : <CheckOutlined />}
                          </Avatar>
                          <Typography color={index > value ? 'textSecondary' : 'inherit'}>{tab.label}</Typography>
                        </Stack>
                      </Grid>
                    }
                  />
                ))}
              </Tabs>
            </Grid>
          </Grid>
        </MainCard>
        <Grid container>
          <Grid item xs={12}>
            <TabPanel value={value} index={0}>
              <UserLogin onNext={onNext} />
            </TabPanel>
            <TabPanel value={value} index={1}>
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
                    <LoanSummary loan={selectedLoan} show />
                    <Button variant="contained" sx={{ textTransform: 'none' }} fullWidth onClick={onNext}>
                      Confirm Loan Selection
                    </Button>
                  </Stack>
                </Grid>
              </Grid>
            </TabPanel>
            <TabPanel value={value} index={2}></TabPanel>
          </Grid>
        </Grid>
      </Stack>
    </Page>
  );
};

Cart.getLayout = function getLayout(page: ReactElement) {
  return <Layout variant="component">{page}</Layout>;
};

export default Cart;
