import axios from 'axios';

const serverBaseUrl = 'http://localhost:4000';
const getKeys = async () => {
  let { data } = await axios.get(`${serverBaseUrl}/api/flask/user/1/api_keys`);
  return data;
};

const UserService = {
  getKeys
};

export default UserService;
