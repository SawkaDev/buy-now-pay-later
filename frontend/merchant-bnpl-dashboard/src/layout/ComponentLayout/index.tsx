import { ReactNode } from 'react';

// material-ui
import { styled, useTheme, Theme } from '@mui/material/styles';
import { Box } from '@mui/material';

// components content
const Main = styled('main', { shouldForwardProp: (prop) => prop !== 'open' })(({ theme, open }: { theme: Theme; open: boolean }) => ({
  minHeight: `calc(100vh - 188px)`,
  width: `calc(100% - 260px)`,
  flexGrow: 1,
  transition: theme.transitions.create('margin', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen
  }),
  [theme.breakpoints.down('md')]: {
    paddingLeft: 0
  },
  ...(open && {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen
    })
  })
}));

// ==============================|| COMPONENTS LAYOUT ||============================== //

interface Props {
  children: ReactNode;
  handleDrawerOpen: () => void;
  componentDrawerOpen: boolean;
}

const ComponentLayout = ({ children, handleDrawerOpen, componentDrawerOpen }: Props) => {
  const theme = useTheme();

  return (
    <Box sx={{ display: 'flex', pt: componentDrawerOpen ? { xs: 0, md: 3, xl: 5.5 } : 0, mb: 10 }}>
      <Main theme={theme} open={componentDrawerOpen}>
        {children}
      </Main>
    </Box>
  );
};

export default ComponentLayout;
