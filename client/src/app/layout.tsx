'use client'; // This is a client component 👈🏽

/* eslint-disable react/display-name */
import React from 'react';

import Page from '../components/Page';

import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import 'aos/dist/aos.css';

/* eslint-disable react/prop-types */
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <link
          rel="shortcut icon"
          href="https://assets.maccarianagency.com/favicons/thefront/favicon.ico"
        />
        <meta name="theme-color" content="#ffffff" />
        <meta
          name="description"
          content="A modern design system for your new landing and web pages."
        />
        <meta
          name="robots"
          content="max-snippet:-1, max-image-preview:large, max-video-preview:-1"
        />
        <meta property="og:locale" content="en_US" />
        <meta property="og:type" content="website" />
        <meta
          property="og:image"
          content="https://assets.maccarianagency.com/screenshots/the-front/social.png"
        />
        <meta
          property="og:title"
          content="theFront | UI Kit by Maccarian Agency."
        />
        <meta
          property="og:description"
          content="A modern design system for your new landing and web pages."
        />
        <meta
          property="og:url"
          content="https://thefront.maccarianagency.com/"
        />
        <link rel="preconnect" href="https://fonts.gstatic.com" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>
        <Page>
          {children}
        </Page>
      </body>
    </html>
  );
}
  