import { ReactElement, useState } from 'react';
import { Alert, AlertTitle, Grid, Stack, Tabs, Typography } from '@mui/material';
import MainCard from 'components/MainCard';
import Layout from 'layout';
import { useTheme } from '@mui/material/styles';
import Page from 'components/Page';
import { StyledTab, TabPanel, tabsOption } from './tabs/tab_helper';
import { CheckOutlined, InfoCircleFilled } from '@ant-design/icons';
import Avatar from 'components/@extended/Avatar';
import UserLogin from './tabs/UserLogin';
import OrderComplete from 'sections/apps/e-commerce/checkout/OrderComplete';
import LoanSelections from './tabs/LoanSelection';
import { useRouter } from 'next/router';

const Cart = () => {
  const [value, setValue] = useState(0);
  const theme = useTheme();
  const router = useRouter();

  const { session } = router.query;

  const onNext = () => {
    setValue((index) => index + 1);
  };

  const [user, setUser] = useState();

  return (
    <Page title="Checkout">
      <Stack spacing={2}>
        {value == 0 && (
          <Alert color={'info'} variant="border" icon={<InfoCircleFilled />} style={{ marginBottom: 0 }}>
            <AlertTitle>
              <b>
                After being redirected from the merchant to this checkout session page, users would normally log in to the Buy Now Pay Later
                service. For easier testing, we simulate the login by allowing you to select a user from a list to "log in" as and click
                "Next." This user will be used for credit decisioning, fraud detection, etc.
              </b>
            </AlertTitle>
          </Alert>
        )}
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
        {JSON.stringify(user)}
        <Grid container>
          <Grid item xs={12}>
            <TabPanel value={value} index={0}>
              <UserLogin onNext={onNext} setUser={setUser} />
            </TabPanel>
            <TabPanel value={value} index={1}>
              {user && session && <LoanSelections user={user} onNext={onNext} sessionId={session as string} />}
            </TabPanel>
            <TabPanel value={value} index={2}>
              <OrderComplete open={true} />
            </TabPanel>
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
