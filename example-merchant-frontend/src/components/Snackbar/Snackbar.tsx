// components/SnackbarNotification.tsx
import React from 'react';
import Snackbar from '@mui/material/Snackbar';
import Alert, { AlertProps } from '@mui/material/Alert';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import ErrorIcon from '@mui/icons-material/Error';
import InfoIcon from '@mui/icons-material/Info';
import WarningIcon from '@mui/icons-material/Warning';
import { useSnackbar } from 'contexts/SnackbarContext';

const SnackbarNotification: React.FC = () => {
  const { snackbarOpen, snackbarMessage, snackbarSeverity, closeSnackbar } =
    useSnackbar();

  const getIcon = (severity: AlertProps['severity']) => {
    switch (severity) {
      case 'success':
        return <CheckCircleIcon sx={{ color: '#fff' }} />;
      case 'error':
        return <ErrorIcon sx={{ color: '#fff' }} />;
      case 'warning':
        return <WarningIcon sx={{ color: '#fff' }} />;
      case 'info':
        return <InfoIcon sx={{ color: '#fff' }} />;
      default:
        return null;
    }
  };

  return (
    <Snackbar
      open={snackbarOpen}
      autoHideDuration={6000}
      onClose={closeSnackbar}
      anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
    >
      <Alert
        onClose={closeSnackbar}
        severity={snackbarSeverity}
        icon={getIcon(snackbarSeverity)}
        sx={{
          width: '100%',
          backgroundColor:
            snackbarSeverity === 'error'
              ? '#d32f2f'
              : snackbarSeverity === 'warning'
                ? '#ed6c02'
                : snackbarSeverity === 'info'
                  ? '#1976d2'
                  : snackbarSeverity === 'success'
                    ? '#388e3c'
                    : '#fff',
          color: '#fff',
          fontWeight: 'bold',
          padding: '10px',
        }}
      >
        {snackbarMessage}
      </Alert>
    </Snackbar>
  );
};

export default SnackbarNotification;
