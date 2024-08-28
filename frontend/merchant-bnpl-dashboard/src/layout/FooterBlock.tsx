// material-ui
import { useTheme } from '@mui/material/styles';
import { Box, Container, CardMedia, Divider, Grid, Typography } from '@mui/material';

// third party
import { motion } from 'framer-motion';

// types
import { ThemeMode } from 'types/config';

const imgfooterlogo = 'assets/images/landing/codedthemes-logo.svg';

// ==============================|| LANDING - FOOTER PAGE ||============================== //

type showProps = {
  isFull?: boolean;
  layout?: string;
};

const FooterBlock = ({ isFull, layout }: showProps) => {
  const theme = useTheme();

  return (
    <>
      <Box sx={{ pt: isFull ? 0 : 5, pb: 5, bgcolor: theme.palette.grey.A700 }}>
        <Container>
          <Grid container spacing={2}>
            <Grid item xs={12} md={4}>
              <motion.div
                initial={{ opacity: 0, translateY: 550 }}
                animate={{ opacity: 1, translateY: 0 }}
                transition={{
                  type: 'spring',
                  stiffness: 150,
                  damping: 30
                }}
              >
                <Grid container spacing={2}>
                  <Grid item xs={12}>
                    <CardMedia component="img" image={imgfooterlogo} sx={{ width: 'auto' }} />
                  </Grid>
                  <Grid item xs={12}>
                    <Typography variant="subtitle1" sx={{ fontWeight: 400, color: theme.palette.common.white }}>
                      Sample footer
                    </Typography>
                  </Grid>
                </Grid>
              </motion.div>
            </Grid>
          </Grid>
        </Container>
      </Box>
      <Divider sx={{ borderColor: 'grey.700' }} />
      <Box
        sx={{
          py: 1.5,
          bgcolor: theme.palette.mode === ThemeMode.DARK ? theme.palette.grey[50] : theme.palette.grey[800]
        }}
      >
        <Container>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={8}>
              <Typography variant="subtitle2" color="secondary">
                © All rights reserved.
              </Typography>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </>
  );
};

export default FooterBlock;
