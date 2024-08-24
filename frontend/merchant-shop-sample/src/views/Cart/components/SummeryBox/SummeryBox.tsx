import React from 'react';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';

interface SummeryBoxProps {
  subTotal: number;
}
const SummeryBox = ({ subTotal }: SummeryBoxProps): JSX.Element => {
  const tax = subTotal * 0.07;

  return (
    <Box>
      <Stack spacing={2} marginY={{ xs: 2, sm: 4 }}>
        <Box display={'flex'} justifyContent={'space-between'}>
          <Typography color={'text.secondary'}>Subtotal</Typography>
          <Typography color={'text.secondary'} fontWeight={700}>
            ${subTotal.toFixed(2)}
          </Typography>
        </Box>
        <Box display={'flex'} justifyContent={'space-between'}>
          <Typography color={'text.secondary'}>Taxes (7%)</Typography>
          <Typography color={'text.secondary'} fontWeight={700}>
            ${tax.toFixed(2)}
          </Typography>
        </Box>
        <Divider />
        <Box display={'flex'} justifyContent={'space-between'}>
          <Typography variant={'h6'} fontWeight={700}>
            Order Total
          </Typography>
          <Typography variant={'h6'} fontWeight={700}>
            ${(subTotal + tax).toFixed(2)}
          </Typography>
        </Box>
        <Button
          component={Link}
          href={'/checkout'}
          variant={'contained'}
          size={'large'}
          fullWidth
        >
          Checkout
        </Button>
      </Stack>
    </Box>
  );
};

export default SummeryBox;
