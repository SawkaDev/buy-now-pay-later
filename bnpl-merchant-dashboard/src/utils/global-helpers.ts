import { dispatch } from 'store';
import { openSnackbar } from 'store/reducers/snackbar';

export function ShowSnackBar(message: string, type: 'error' | 'success') {
  dispatch(
    openSnackbar({
      open: true,
      anchorOrigin: { vertical: 'bottom', horizontal: 'center' },
      message: message,
      variant: 'alert',
      alert: {
        color: type
      },
      close: true
    })
  );
}
