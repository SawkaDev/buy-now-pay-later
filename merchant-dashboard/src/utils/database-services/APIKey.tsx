import axios from 'axios';

const serverBaseUrl = 'http://localhost:8080';

const create = async (userId: number) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/api-key-service/key/generate`, { user_id: userId });
    return response.data;
  } catch (error) {
    console.error('Error generating API key:', error);
    throw error;
  }
};

const revoke = async (keyId: string) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/api-key-service/key/revoke`, { key_id: keyId });
    return response.data;
  } catch (error) {
    console.error('Error generating API key:', error);
    throw error;
  }
};

const getKeys = async (userId: number) => {
  let { data } = await axios.get(`${serverBaseUrl}/api/api-key-service/keys/${userId}`);
  return data;
};

const APIKeyService = {
  create,
  revoke,
  getKeys
};

export default APIKeyService;
