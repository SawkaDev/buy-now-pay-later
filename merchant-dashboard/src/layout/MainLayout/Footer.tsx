// material-ui
import { Link, Stack, Typography } from '@mui/material';

const Footer = () => (
  <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ p: '24px 16px 0px', mt: 'auto' }}>
    <Typography variant="caption">&copy; All rights reserved</Typography>
    <Stack spacing={1.5} direction="row" justifyContent="space-between" alignItems="center">
      <Link href="#" variant="caption" color="textPrimary">
        Privacy
      </Link>
      <Link href="#" variant="caption" color="textPrimary">
        Terms
      </Link>
    </Stack>
  </Stack>
);

export default Footer;
