import CopyOutlined from '@ant-design/icons/CopyOutlined';
import { IconButton, InputAdornment, Stack, TextField, Tooltip } from '@mui/material';
import { CopyToClipboard } from 'react-copy-to-clipboard';
import { ShowSnackBar } from 'utils/global-helpers';

interface TextFieldCopyProps {
  value: string;
}
const TextFieldCopy = ({ value }: TextFieldCopyProps) => {
  return (
    <Stack spacing={0.5}>
      <TextField
        fullWidth
        placeholder="Website"
        type="text"
        disabled
        value={value}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <CopyToClipboard text={value} onCopy={() => ShowSnackBar('API Key Copied', 'success')}>
                <Tooltip title="Copy">
                  <IconButton aria-label="Copy from another element" color="secondary" edge="end" size="large">
                    <CopyOutlined />
                  </IconButton>
                </Tooltip>
              </CopyToClipboard>
            </InputAdornment>
          )
        }}
      />
    </Stack>
  );
};

export default TextFieldCopy;
