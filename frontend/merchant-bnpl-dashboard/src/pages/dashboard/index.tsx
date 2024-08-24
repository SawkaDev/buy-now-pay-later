import { useState, ReactElement } from 'react';

// material-ui
import { useTheme } from '@mui/material/styles';
import { Box, Grid, MenuItem, Select, SelectChangeEvent, Stack, ToggleButton, ToggleButtonGroup, Typography } from '@mui/material';

// project import
import Layout from 'layout';
import Page from 'components/Page';
import MainCard from 'components/MainCard';
import AnalyticsDataCard from 'components/cards/statistics/AnalyticsDataCard';
import IncomeChart from 'sections/dashboard/analytics/IncomeChart';
import MarketingCardChart from 'sections/dashboard/analytics/MarketingCardChart';
import OrdersCardChart from 'sections/dashboard/analytics/OrdersCardChart';
import OrdersList from 'sections/dashboard/analytics/OrdersList';
import PageViews from 'sections/dashboard/analytics/PageViews';
import SalesCardChart from 'sections/dashboard/analytics/SalesCardChart';
import TransactionHistory from 'sections/dashboard/analytics/TransactionHistory';
import UsersCardChart from 'sections/dashboard/analytics/UsersCardChart';

// assets
import { CaretDownOutlined } from '@ant-design/icons';

// ==============================|| DASHBOARD - ANALYTICS ||============================== //

const DashboardAnalytics = () => {
  const theme = useTheme();
  const [slot, setSlot] = useState('week');
  const [quantity, setQuantity] = useState('By volume');

  const handleQuantity = (e: SelectChangeEvent) => {
    setQuantity(e.target.value as string);
  };

  const handleChange = (event: React.MouseEvent<HTMLElement>, newAlignment: string) => {
    if (newAlignment) setSlot(newAlignment);
  };

  return (
    <Page title="Analytic Dashboard">
      <Grid container rowSpacing={4.5} columnSpacing={3}>
        {/* row 1 */}
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <AnalyticsDataCard title="Total Users" count="78,250" percentage={70.5}>
            <UsersCardChart />
          </AnalyticsDataCard>
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <AnalyticsDataCard title="Total Order" count="18,800" percentage={27.4} isLoss color="warning">
            <OrdersCardChart />
          </AnalyticsDataCard>
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <AnalyticsDataCard title="Total Sales" count="$35,078" percentage={27.4} isLoss color="warning">
            <SalesCardChart />
          </AnalyticsDataCard>
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <AnalyticsDataCard title="Total Marketing" count="$1,12,083" percentage={70.5}>
            <MarketingCardChart />
          </AnalyticsDataCard>
        </Grid>

        <Grid item md={8} sx={{ display: { sm: 'none', md: 'block', lg: 'none' } }} />

        {/* row 2 */}
        <Grid item xs={12} md={7} lg={8}>
          <Grid container alignItems="center" justifyContent="space-between">
            <Grid item>
              <Typography variant="h5">Income Overview</Typography>
            </Grid>
          </Grid>
          <MainCard content={false} sx={{ mt: 1.5 }}>
            <Grid item>
              <Grid container>
                <Grid item xs={12} sm={6}>
                  <Stack sx={{ ml: 2, mt: 3 }} alignItems={{ xs: 'center', sm: 'flex-start' }}>
                    <Stack direction="row" alignItems="center">
                      <CaretDownOutlined style={{ color: theme.palette.error.main, paddingRight: '4px' }} />
                      <Typography color={theme.palette.error.main}>$1,12,900 (45.67%)</Typography>
                    </Stack>
                    <Typography color="textSecondary" sx={{ display: 'block' }}>
                      Compare to : 01 Dec 2021-08 Jan 2022
                    </Typography>
                  </Stack>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Stack
                    direction="row"
                    spacing={1}
                    alignItems="center"
                    justifyContent={{ xs: 'center', sm: 'flex-end' }}
                    sx={{ mt: 3, mr: 2 }}
                  >
                    <ToggleButtonGroup exclusive onChange={handleChange} size="small" value={slot}>
                      <ToggleButton disabled={slot === 'week'} value="week" sx={{ px: 2, py: 0.5 }}>
                        Week
                      </ToggleButton>
                      <ToggleButton disabled={slot === 'month'} value="month" sx={{ px: 2, py: 0.5 }}>
                        Month
                      </ToggleButton>
                    </ToggleButtonGroup>
                    <Select value={quantity} onChange={handleQuantity} size="small">
                      <MenuItem value="By volume">By Volume</MenuItem>
                      <MenuItem value="By margin">By Margin</MenuItem>
                      <MenuItem value="By sales">By Sales</MenuItem>
                    </Select>
                  </Stack>
                </Grid>
              </Grid>
            </Grid>
            <Box sx={{ pt: 1 }}>
              <IncomeChart slot={slot} quantity={quantity} />
            </Box>
          </MainCard>
        </Grid>
        <Grid item xs={12} md={5} lg={4}>
          <PageViews />
        </Grid>

        {/* row 3 */}
        <Grid item xs={12} md={7} lg={8}>
          <Grid container alignItems="center" justifyContent="space-between">
            <Grid item>
              <Typography variant="h5">Recent Orders</Typography>
            </Grid>
            <Grid item />
          </Grid>
          <MainCard sx={{ mt: 2 }} content={false}>
            <OrdersList />
          </MainCard>
        </Grid>

        {/* row 4 */}
        <Grid item xs={12} md={5} lg={4}>
          <TransactionHistory />
        </Grid>
      </Grid>
    </Page>
  );
};

DashboardAnalytics.getLayout = function getLayout(page: ReactElement) {
  return <Layout>{page}</Layout>;
};

export default DashboardAnalytics;
