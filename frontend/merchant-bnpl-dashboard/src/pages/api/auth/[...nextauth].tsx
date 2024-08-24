import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import axios from 'axios'; // Import axios directly

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8080',
  withCredentials: true
});

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
          const response = await axiosInstance.post('/auth/login', {
            password: credentials?.password,
            email: credentials?.email
          });

          if (response.data && response.data.user) {
            return { ...response.data.user, sessionData: response.headers['set-cookie'] };
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
          const response = await axiosInstance.post('/auth/register', {
            name: credentials?.name,
            email: credentials?.email,
            password: credentials?.password
          });

          if (response.status === 201) {
            return null;
          } else {
            throw new Error(response?.data?.error || 'Registration failed');
          }
        } catch (error: any) {
          throw new Error(error.response?.data?.error || 'Registration failed');
        }
      }
    })
  ],
  callbacks: {
    jwt: async ({ token, user, account }) => {
      if (user) {
        token.id = user.id;
        token.name = user.name;
        token.email = user.email;
        token.image = user.image;
        // @ts-ignore
        token.sessionData = user.sessionData;
      }
      return token;
    },
    session: ({ session, token }) => {
      session.user = {
        id: token.id,
        name: token.name,
        email: token.email,
        // @ts-ignore
        image: token.image
      };
      // @ts-ignore
      session.sessionData = token.sessionData;
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
