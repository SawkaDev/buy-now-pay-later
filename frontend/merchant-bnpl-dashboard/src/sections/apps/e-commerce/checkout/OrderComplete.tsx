// next
import NextLink from 'next/link';
import Image from 'next/legacy/image';

// material-ui
import { useTheme } from '@mui/material/styles';
import { Box, Button, Dialog, Grid, Stack, Typography, useMediaQuery } from '@mui/material';

// third-party

// project imports
import MainCard from 'components/MainCard';
import { PopupTransition } from 'components/@extended/Transitions';

// assets
const completed = '/assets/images/e-commerce/completed.png';

// ==============================|| CHECKOUT - ORDER COMPLETE ||============================== //

const OrderComplete = ({ open }: { open: boolean }) => {
  const theme = useTheme();
  const matchDownMD = useMediaQuery(theme.breakpoints.down('md'));

  return (
    <Dialog
      open={open}
      fullScreen
      TransitionComponent={PopupTransition}
      sx={{ '& .MuiDialog-paper': { bgcolor: 'background.paper', backgroundImage: 'none' } }}
    >
      <Grid container justifyContent="center" alignItems="center" sx={{ minHeight: '100vh' }}>
        <Grid item>
          <MainCard border={false}>
            <Stack spacing={2} alignItems="center">
              <Box sx={{ position: 'relative', width: { xs: 320, sm: 500 } }}>
                <Image
                  src={completed}
                  alt="Order Complete"
                  width={matchDownMD ? 320 : 500}
                  height={matchDownMD ? 200 : 312}
                  layout="intrinsic"
                />
              </Box>
              <Typography variant={matchDownMD ? 'h3' : 'h1'} align="center">
                Thank you for checking out with BNPL!
              </Typography>
              <Stack direction="row" justifyContent="center" spacing={3} pt={2}>
                <NextLink href="/apps/e-commerce/products" passHref legacyBehavior>
                  <Button variant="contained" color="primary" size={matchDownMD ? 'small' : 'medium'}>
                    View BNPL (Consumer) Loan Dashboard
                  </Button>
                </NextLink>
              </Stack>
            </Stack>
          </MainCard>
        </Grid>
      </Grid>
    </Dialog>
  );
};

export default OrderComplete;
