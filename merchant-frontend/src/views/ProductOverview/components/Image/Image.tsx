import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

interface Props {
  image: string;
  title: string;
}

const Image = ({ image, title }: Props): JSX.Element => {
  return (
    <Grid container spacing={2} sx={{ height: 1 }}>
      <Grid item xs={12}>
        <Box
          sx={{
            display: 'flex',
            height: 1,
            '& img': {
              width: 1,
              height: 1,
              objectFit: 'cover',
              borderRadius: 2,
            },
          }}
        >
          <img src={image} alt={title} loading={'lazy'} />
        </Box>
      </Grid>
    </Grid>
  );
};

export default Image;
