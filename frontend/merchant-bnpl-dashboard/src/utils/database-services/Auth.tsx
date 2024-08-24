import axios from 'axios';

const serverBaseUrl = 'http://localhost:8080';

const axiosInstance = axios.create({
  baseURL: serverBaseUrl,
  withCredentials: true
});

const checkSession = async () => {
  try {
    const response = await axiosInstance.get(`/auth/session`);
    return response.data;
  } catch (error) {
    console.error('Error checking session In User:', error);
    throw error;
  }
};

const UserService = {
  checkSession
};

export default UserService;
