import {
  alpha,
  Box,
  Button,
  Card,
  CardMedia,
  Grid,
  Stack,
  Typography,
  useTheme,
} from '@mui/material';
import React from 'react';
import { useRouter } from 'next/navigation';
import { ProductType } from 'types/products';

interface Props {
  item: ProductType;
  rowSize?: number;
}

const ProductThumbnail = ({ item, rowSize = 4 }: Props) => {
  const theme = useTheme();
  const router = useRouter();

  return (
    <Grid item xs={12} sm={6} md={rowSize}>
      <Box display={'block'} width={1} height={1}>
        <Card
          sx={{
            width: 1,
            height: 1,
            display: 'flex',
            flexDirection: 'column',
            boxShadow: 'none',
            bgcolor: 'transparent',
            backgroundImage: 'none',
          }}
        >
          <CardMedia
            title={item.title}
            image={item.media}
            sx={{
              position: 'relative',
              height: 320,
              overflow: 'hidden',
              borderRadius: 2,
              filter:
                theme.palette.mode === 'dark' ? 'brightness(0.7)' : 'none',
            }}
          >
            <Stack
              direction={'row'}
              spacing={1}
              sx={{
                position: 'absolute',
                top: 'auto',
                bottom: 0,
                left: 0,
                right: 0,
                padding: 2,
              }}
            >
              {item.oldPrice && (
                <Box
                  sx={{
                    bgcolor: theme.palette.error.light,
                    paddingY: '4px',
                    paddingX: '8px',
                    borderRadius: 1,
                    display: 'flex',
                    alignItems: 'center',
                  }}
                >
                  <Typography
                    variant={'caption'}
                    fontWeight={700}
                    sx={{
                      color: theme.palette.common.white,
                      textTransform: 'uppercase',
                      lineHeight: 1,
                    }}
                  >
                    promo price
                  </Typography>
                </Box>
              )}
              {item.isNew && (
                <Box
                  sx={{
                    bgcolor: theme.palette.success.light,
                    paddingY: '4px',
                    paddingX: '8px',
                    borderRadius: 1,
                    display: 'flex',
                    alignItems: 'center',
                  }}
                >
                  <Typography
                    variant={'caption'}
                    fontWeight={700}
                    sx={{
                      color: theme.palette.common.white,
                      textTransform: 'uppercase',
                      lineHeight: 1,
                    }}
                  >
                    new
                  </Typography>
                </Box>
              )}
            </Stack>
          </CardMedia>
          <Box marginTop={2}>
            <Typography fontWeight={700}>{item.title}</Typography>
          </Box>
          <Box marginTop={2} display={'flex'} alignItems={'center'}>
            {item.oldPrice && (
              <Typography
                marginRight={0.5}
                color={'text.secondary'}
                sx={{ textDecoration: 'line-through' }}
              >
                ${item.oldPrice.toFixed(2)}
              </Typography>
            )}
            <Typography
              fontWeight={700}
              color={item.oldPrice ? 'error.light' : 'text.primary'}
            >
              ${item.price.toFixed(2)}
            </Typography>
          </Box>
          <Stack marginTop={2} spacing={1} direction={'row'}>
            <Button
              variant={'contained'}
              color={'primary'}
              size={'large'}
              fullWidth
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                width={20}
                height={20}
              >
                <path d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z" />
              </svg>
            </Button>
            <Button
              color={'primary'}
              size={'large'}
              fullWidth
              sx={{ bgcolor: alpha(theme.palette.primary.light, 0.1) }}
              onClick={() => router.push(`/product/${item.id}`)}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                width={20}
                height={20}
              >
                <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                <path
                  fillRule="evenodd"
                  d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
                  clipRule="evenodd"
                />
              </svg>
            </Button>
          </Stack>
        </Card>
      </Box>
    </Grid>
  );
};

export default ProductThumbnail;
