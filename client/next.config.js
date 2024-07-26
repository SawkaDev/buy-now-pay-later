/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: ['assets.maccarianagency.com'],
  },
  output: 'standalone'
}
 
module.exports = nextConfig