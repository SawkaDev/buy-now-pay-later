import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import { useMutation } from '@tanstack/react-query';
import { createCheckoutSession } from 'app/lib/BNPLWrapper';
import { useRouter } from 'next/navigation';

interface SummaryBoxProps {
  subTotal: number;
}

const SummaryBox = ({ subTotal }: SummaryBoxProps): JSX.Element => {
  const [openModal, setOpenModal] = useState(false);
  const [checkoutUrl, setCheckoutUrl] = useState('');

  const tax = subTotal * 0.07;
  const shipping = 9.99;
  const router = useRouter();
  const total = tax + shipping + subTotal;

  const { mutate: createCheckoutSessionMutation, isPending } = useMutation({
    mutationFn: (params: any) => createCheckoutSession(params),
    onSuccess: (data) => {
      console.log('Checkout session created:', data);
      router.push(data.checkout_url);
      // setCheckoutUrl(data.checkout_url);
      // setOpenModal(true);
    },
    onError: (error) => {
      console.error('Error creating checkout session:', error);
    },
  });

  const handleCreateCheckout = () => {
    createCheckoutSessionMutation({
      loan_amount_cents: Math.round(total * 100), // Convert to cents
      merchant_id: 12,
      order_id: 'order_9f99_1',
      success_redirect_url: 'http://localhost:3010/success',
      cancel_redirect_url: 'http://localhost:3010/cart',
    });
  };

  const handleCloseModal = () => {
    setOpenModal(false);
  };

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
        <Box display={'flex'} justifyContent={'space-between'}>
          <Typography color={'text.secondary'}>Shipping</Typography>
          <Typography color={'text.secondary'} fontWeight={700}>
            $9.99
          </Typography>
        </Box>
        <Divider />
        <Box display={'flex'} justifyContent={'space-between'}>
          <Typography variant={'h6'} fontWeight={700}>
            Order Total
          </Typography>
          <Typography variant={'h6'} fontWeight={700}>
            ${total.toFixed(2)}
          </Typography>
        </Box>
        <Button
          variant={'contained'}
          size={'large'}
          fullWidth
          onClick={handleCreateCheckout}
          disabled={isPending}
        >
          {isPending ? 'Processing...' : 'Pay with BNPL'}
        </Button>
      </Stack>

      <Modal
        open={openModal}
        onClose={handleCloseModal}
        aria-labelledby="checkout-modal"
        aria-describedby="checkout-iframe"
      >
        <Box
          sx={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: '80%',
            height: '80%',
            bgcolor: 'background.paper',
            boxShadow: 24,
            // p: 4,
          }}
        >
          <iframe
            src={checkoutUrl}
            width="100%"
            height="100%"
            frameBorder="0"
            title="Checkout"
          />
        </Box>
      </Modal>
    </Box>
  );
};

export default SummaryBox;
