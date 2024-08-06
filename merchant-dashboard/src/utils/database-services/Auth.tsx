import axios from 'axios';

const serverBaseUrl = 'http://localhost:8080';

const register = async (values: any) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/user-service/auth/register`, { ...values });
    return response.data;
  } catch (error) {
    console.error('Error Registering User:', error);
    throw error;
  }
};

const login = async (values: any) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/user-service/auth/login`, { ...values });
    return response.data;
  } catch (error) {
    console.error('Error Logging In User:', error);
    throw error;
  }
};

const UserService = {
  register,
  login
};

export default UserService;
