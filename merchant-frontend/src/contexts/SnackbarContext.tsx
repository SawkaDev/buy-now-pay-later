// contexts/SnackbarContext.tsx
import React, { createContext, useState, useContext } from 'react';
import { AlertColor } from '@mui/material';

type SnackbarContextType = {
  showSnackbar: (message: string, severity?: AlertColor) => void;
  snackbarOpen: boolean;
  snackbarMessage: string;
  snackbarSeverity: AlertColor;
  closeSnackbar: () => void;
};

const SnackbarContext = createContext<SnackbarContextType | undefined>(
  undefined,
);

export const SnackbarProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [snackbarSeverity, setSnackbarSeverity] = useState<AlertColor>('info');

  const showSnackbar = (message: string, severity: AlertColor = 'info') => {
    setSnackbarMessage(message);
    setSnackbarSeverity(severity);
    setSnackbarOpen(true);
  };

  const closeSnackbar = () => {
    setSnackbarOpen(false);
  };

  return (
    <SnackbarContext.Provider
      value={{
        showSnackbar,
        snackbarOpen,
        snackbarMessage,
        snackbarSeverity,
        closeSnackbar,
      }}
    >
      {children}
    </SnackbarContext.Provider>
  );
};

export const useSnackbar = () => {
  const context = useContext(SnackbarContext);
  if (context === undefined) {
    throw new Error('useSnackbar must be used within a SnackbarProvider');
  }
  return context;
};
