import { Tab } from '@mui/material';
import { ReactNode } from 'react';
import { styled, Theme } from '@mui/material/styles';

interface StyledProps {
  theme: Theme;
  value: number;
  disabled?: boolean;
  icon?: ReactNode;
  label?: ReactNode;
}

interface TabOptionProps {
  label: string;
}

export interface TabsProps {
  children?: React.ReactElement | React.ReactNode | string;
  value: string | number;
  index: number;
}

export const StyledTab = styled((props) => <Tab {...props} />)(({ theme, value, ...others }: StyledProps) => ({
  minHeight: 'auto',
  minWidth: 250,
  padding: 16,
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'flex-start',
  textAlign: 'left',
  justifyContent: 'flex-start',
  '&:after': {
    backgroundColor: 'transparent !important'
  },

  '& > svg': {
    marginBottom: '0px !important',
    marginRight: 10,
    marginTop: 2,
    height: 20,
    width: 20
  },
  [theme.breakpoints.down('md')]: {
    minWidth: 'auto'
  }
}));

// tabs option
export const tabsOption: TabOptionProps[] = [
  {
    label: 'User Login'
  },
  {
    label: 'Loan Selection'
  },
  {
    label: 'Confirmation'
  }
];

// tabs
export function TabPanel({ children, value, index, ...other }: TabsProps) {
  return (
    <div role="tabpanel" hidden={value !== index} id={`simple-tabpanel-${index}`} aria-labelledby={`simple-tab-${index}`} {...other}>
      {value === index && <div>{children}</div>}
    </div>
  );
}
