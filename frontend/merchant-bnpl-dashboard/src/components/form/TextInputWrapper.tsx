import TextField from '@mui/material/TextField';
import { useController } from 'react-hook-form';
import InputLabelWrapper from './InputLabelWrapper';

interface TextInputWrapperProps {
  label: string;
  name: string;
  type?: string;
  placeholder?: string;
  [extraProps: string]: any;
  helperText?: string;
  textalign?: 'center' | 'right' | 'left';
  defaultValue?: any;
}

const TextInputWrapper = ({
  label,
  name,
  tightForm,
  placeholder,
  helperText,
  defaultValue = undefined,
  type = 'text',
  ...extraProps
}: TextInputWrapperProps) => {
  const {
    field: { onChange, onBlur, value, ref },
    fieldState: { error }
  } = useController({ name, defaultValue: null });

  var normal: string = '';

  if (value !== null) {
    normal = value;
  }

  if (!helperText) {
    helperText = ' ';
  }

  if (tightForm) {
    helperText = '';
  }

  return (
    <>
      {!tightForm && <InputLabelWrapper req={extraProps.required}>{label}</InputLabelWrapper>}
      <TextField
        variant={'outlined'}
        type={'text'}
        onBlur={onBlur}
        fullWidth
        sx={{ p: 0, m: 0 }}
        ref={ref}
        value={normal}
        placeholder={placeholder || 'Enter '.concat(label)}
        onChange={onChange}
        error={Boolean(error)}
        helperText={error ? error.message : helperText}
        {...extraProps}
      />
    </>
  );
};

export default TextInputWrapper;
