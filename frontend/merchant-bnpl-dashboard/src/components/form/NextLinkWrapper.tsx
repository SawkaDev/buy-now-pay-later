/* eslint-disable @typescript-eslint/no-unused-vars */
import NextLink from 'next/link';
import MuiLink from '@mui/material/Link';
import Button from '@mui/material/Button';

export default function NextLinkWrapper({ linkType, href = '/', children, ...props }: any) {
  if (linkType === 'link' || !linkType) {
    return (
      <NextLink href={href} passHref>
        <MuiLink {...props}>{children}</MuiLink>
      </NextLink>
    );
  } else if (linkType === 'button') {
    return (
      <NextLink href={href} passHref>
        <Button {...props}>{children}</Button>
      </NextLink>
    );
  } else {
    return <p>Invalid Button</p>;
  }
}
