import React from 'react';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import { useCart } from 'contexts/CartContext';
import { ProductType } from 'types/products';

const mock = [
  {
    title: '30 Days return',
    subtitle: 'We offer you a full refund within 30 days of purchase.',
    icon: (
      <svg
        width={24}
        height={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
        />
      </svg>
    ),
  },
  {
    title: 'Fast delivery',
    subtitle: 'Automatically receive free standard shipping on every order.',
    icon: (
      <svg
        width={24}
        height={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z" />
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0"
        />
      </svg>
    ),
  },
];

interface DetailsProps {
  product: ProductType;
}

const Details = ({ product }: DetailsProps): JSX.Element => {
  const { addItem } = useCart();

  return (
    <Box>
      <Box display={'flex'} justifyContent={'space-between'}>
        <Typography fontWeight={700} noWrap>
          {product.title}
        </Typography>
        <Typography fontWeight={700} noWrap>
          ${product.price.toFixed(2)}
        </Typography>
      </Box>
      <Box marginTop={4}>
        <Typography>Description</Typography>
        <Typography
          variant={'subtitle2'}
          color={'text.secondary'}
          marginTop={1}
        >
          {product.description}
        </Typography>
      </Box>
      <Box marginTop={4}>
        <Button
          onClick={() =>
            addItem({
              id: product.id,
              title: product.title,
              price: product.price,
              media: product.media,
              quantity: 1,
              description: product.description,
              isNew: product.isNew,
            })
          }
          variant={'contained'}
          color={'primary'}
          size={'large'}
          fullWidth
        >
          Add to cart
        </Button>
      </Box>
      <Divider sx={{ marginTop: 4 }} />
      <Box marginTop={4}>
        <Grid container spacing={2}>
          {mock.map((item, i) => (
            <Grid key={i} item xs={6}>
              <ListItem
                component="div"
                disableGutters
                sx={{
                  alignItems: 'flex-start',
                  padding: 0,
                }}
              >
                <ListItemAvatar sx={{ minWidth: 0, mr: 1 }}>
                  <Box color={'text.secondary'}>{item.icon}</Box>
                </ListItemAvatar>
                <ListItemText
                  primary={item.title}
                  secondary={item.subtitle}
                  primaryTypographyProps={{
                    variant: 'body2',
                    fontWeight: 700,
                  }}
                  secondaryTypographyProps={{
                    variant: 'caption',
                  }}
                  sx={{
                    margin: 0,
                  }}
                />
              </ListItem>
            </Grid>
          ))}
        </Grid>
      </Box>
    </Box>
  );
};

export default Details;
