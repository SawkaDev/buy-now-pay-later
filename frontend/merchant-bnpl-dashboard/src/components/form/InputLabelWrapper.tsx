import { InputLabel, Stack, Typography } from '@mui/material';
import { ReactNode } from 'react';

interface InputLabelWrapperProps {
  req?: boolean;
  children: ReactNode;
  labelSize?:
    | 'inherit'
    | 'button'
    | 'caption'
    | 'h1'
    | 'h2'
    | 'h3'
    | 'h4'
    | 'h5'
    | 'h6'
    | 'subtitle1'
    | 'subtitle2'
    | 'body1'
    | 'body2'
    | 'overline'
    | undefined;
}

const InputLabelWrapper = ({ req, children, labelSize = 'inherit' }: InputLabelWrapperProps) => (
  <InputLabel
    sx={{
      // color: 'red',
      fontWeight: 500,
      marginBottom: '3px',
      whiteSpace: 'break-spaces'
    }}
  >
    <Stack direction="row" spacing={0.5}>
      <Typography variant={labelSize}>{children}</Typography>
      {req && <Typography color="red">*</Typography>}
    </Stack>
  </InputLabel>
);

export default InputLabelWrapper;
