import React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import { useTheme } from '@mui/material/styles';

import NavItem from './components/NavItem';

interface Props {
  pages: {
    home: Array<PageItem>;
    company: Array<PageItem>;
    account: Array<PageItem>;
    contact: Array<PageItem>;
  };
}

const SidebarNav = ({ pages }: Props): JSX.Element => {
  const theme = useTheme();
  const { mode } = theme.palette;

  const {
    home: landingPages,
    company: companyPages,
    account: accountPages,
    contact: contactPages,
  } = pages;

  return (
    <Box>
      <Box width={1} paddingX={2} paddingY={1}>
        <Box
          display={'flex'}
          component="a"
          href="/"
          title="theFront"
          width={{ xs: 100, md: 120 }}
        >
          <Box
            component={'img'}
            src={
              mode === 'light'
                ? 'https://assets.maccarianagency.com/the-front/logos/logo.svg'
                : 'https://assets.maccarianagency.com/the-front/logos/logo-negative.svg'
            }
            height={1}
            width={1}
          />
        </Box>
      </Box>
      <Box paddingX={2} paddingY={2}>
        <Box>
          <NavItem title={'Home'} items={landingPages} />
        </Box>
        <Box>
          <NavItem title={'Company'} items={companyPages} />
        </Box>
        <Box>
          <NavItem title={'Account'} items={accountPages} />
        </Box>
        <Box>
          <NavItem title={'Contact'} items={contactPages} />
        </Box>
        <Box marginTop={1}>
          <Button
            size={'large'}
            variant="contained"
            color="primary"
            fullWidth
            component="a"
            target="blank"
            href="https://mui.com/store/items/the-front-landing-page/"
          >
            Sign In
          </Button>
        </Box>
      </Box>
    </Box>
  );
};

export default SidebarNav;
