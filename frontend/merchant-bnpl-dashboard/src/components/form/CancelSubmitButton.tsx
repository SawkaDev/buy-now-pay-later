import React from 'react';
import { Stack, Button } from '@mui/material';
import NextLinkWrapper from './NextLinkWrapper';

interface CancelSubmitButtonProps {
  url: string;
  isSubmitting?: boolean;
  justify: 'right' | 'left' | 'center';
  customSubmitButtonName?: string;
}

const CancelSubmitButton = ({ url, justify, customSubmitButtonName, isSubmitting = false }: CancelSubmitButtonProps) => {
  return (
    <Stack direction="row" spacing={1} justifyContent={justify} sx={{ width: 0, px: 0, py: 3 }}>
      <NextLinkWrapper linkType="button" href={url} disabled={isSubmitting} color="error" size="small">
        Cancel
      </NextLinkWrapper>
      <Button type="submit" disabled={isSubmitting} variant="contained" size="small">
        {customSubmitButtonName ? customSubmitButtonName : 'Submit'}
      </Button>
    </Stack>
  );
};

export default CancelSubmitButton;
