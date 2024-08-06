import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import axios from 'utils/axios';

export default NextAuth({
  secret: process.env.NEXTAUTH_SECRET_KEY,
  providers: [
    CredentialsProvider({
      id: 'login',
      name: 'Login',
      credentials: {
        email: { label: 'Email', type: 'email', placeholder: 'Enter Email' },
        password: { label: 'Password', type: 'password', placeholder: 'Enter Password' }
      },
      async authorize(credentials) {
        try {
          const response = await axios.post('http://localhost:8080/api/user-service/auth/login', {
            password: credentials?.password,
            email: credentials?.email
          });

          if (response.data && response.data.user) {
            return {
              ...response.data.user,
              accessToken: response.data.serviceToken
            };
          }
          return null;
        } catch (error: any) {
          throw new Error(error.response?.data?.message || 'Authentication failed');
        }
      }
    }),
    CredentialsProvider({
      id: 'register',
      name: 'Register',
      credentials: {
        name: { label: 'Name', type: 'text', placeholder: 'Enter Name' },
        email: { label: 'Email', type: 'email', placeholder: 'Enter Email' },
        password: { label: 'Password', type: 'password', placeholder: 'Enter Password' }
      },
      async authorize(credentials) {
        try {
          const response = await axios.post('http://localhost:8080/api/user-service/auth/register', {
            name: credentials?.name,
            password: credentials?.password,
            email: credentials?.email
          });

          if (response.data && response.data.user) {
            return response.data.user;
          }
          return null;
        } catch (error: any) {
          throw new Error(error.response?.data?.message || 'Registration failed');
        }
      }
    })
  ],
  callbacks: {
    jwt: async ({ token, user, account }) => {
      if (user) {
        token.accessToken = user.accessToken;
        token.id = user.id;
        token.provider = account?.provider;
      }
      return token;
    },
    session: ({ session, token }) => {
      if (token) {
        session.id = token.id;
        session.provider = token.provider;
        session.tocken = token;
      }
      return session;
    }
  },
  session: {
    strategy: 'jwt',
    maxAge: Number(process.env.REACT_APP_JWT_TIMEOUT!)
  },
  jwt: {
    secret: process.env.REACT_APP_JWT_SECRET
  },
  pages: {
    signIn: '/login',
    newUser: '/register'
  }
});
