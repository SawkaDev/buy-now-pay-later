import React from 'react';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { ProductType } from 'types/products';
import { useCart } from 'contexts/CartContext';
import { Button } from '@mui/material';

interface OrdersProp {
  items: ProductType[];
}
const Orders = ({ items }: OrdersProp): JSX.Element => {
  const theme = useTheme();
  const { removeItem } = useCart();
  return (
    <Box>
      {items.map((item, i) => (
        <Box key={i}>
          <Box display={'flex'}>
            <Box
              component={'img'}
              src={item.media}
              alt={item.title}
              sx={{
                borderRadius: 2,
                width: 1,
                height: 1,
                maxWidth: { xs: 500, sm: 100 },
                minWidth: { sm: 100 },
                minHeight: { sm: 100 },
                maxHeight: { sm: 100 },

                marginRight: 2,
                filter:
                  theme.palette.mode === 'dark' ? 'brightness(0.7)' : 'none',
              }}
            />
            <Box
              display={'flex'}
              flexDirection={{ xs: 'column', sm: 'row' }}
              justifyContent={'space-between'}
              alignItems={'flex-start'}
              width={1}
            >
              <Box sx={{ order: 1 }}>
                <Typography fontWeight={700} gutterBottom>
                  {item.title}
                </Typography>
                <Typography
                  color={'text.secondary'}
                  variant={'subtitle2'}
                  noWrap={true}
                  gutterBottom
                >
                  ID:{' '}
                  <Typography
                    variant={'inherit'}
                    component={'span'}
                    color={'inherit'}
                    fontWeight={700}
                  >
                    {item.id}
                  </Typography>
                </Typography>
              </Box>
              <Stack
                spacing={1}
                direction={{ xs: 'row', sm: 'column' }}
                marginTop={{ xs: 2, sm: 0 }}
                sx={{ order: { xs: 3, sm: 2 } }}
              >
                <Button
                  onClick={() => {
                    removeItem(item.id);
                  }}
                  sx={{
                    display: 'flex',
                    alignItems: 'center',
                    color: 'text.secondary',
                    '&:hover': {
                      color: 'primary.main',
                    },
                    m: 0.5,
                    p: 0.5,
                  }}
                >
                  <Box
                    component={'svg'}
                    xmlns="http://www.w3.org/2000/svg"
                    width={20}
                    height={20}
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    marginRight={0.5}
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                    />
                  </Box>
                  Remove
                </Button>
              </Stack>
              <Stack
                spacing={1}
                direction={'row'}
                alignItems={'center'}
                marginTop={{ xs: 2, sm: 0 }}
                sx={{ order: { xs: 2, sm: 3 } }}
              >
                <FormControl fullWidth>
                  <Select
                    disabled
                    value={item.quantity}
                    sx={{
                      '& .MuiSelect-select': {
                        paddingY: 0.5,
                      },
                    }}
                  >
                    {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((i) => (
                      <MenuItem key={i} value={i}>
                        {i}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
                <Typography fontWeight={700} marginLeft={2}>
                  ${(item.price * item.quantity).toFixed(2)}
                </Typography>
              </Stack>
            </Box>
          </Box>
          <Divider
            sx={{
              marginY: { xs: 2, sm: 4 },
              display: i === items.length - 1 ? 'none' : 'block',
            }}
          />
        </Box>
      ))}
    </Box>
  );
};

export default Orders;
