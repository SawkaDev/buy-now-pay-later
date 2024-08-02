import axios from 'axios';

const serverBaseUrl = 'http://localhost:4000';

const create = async () => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/flask/key/generate`, { user_id: 1 });
    return response.data;
  } catch (error) {
    console.error('Error generating API key:', error);
    throw error;
  }
};

const revoke = async (keyId: string) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/flask/key/revoke`, { key_id: keyId });
    return response.data;
  } catch (error) {
    console.error('Error generating API key:', error);
    throw error;
  }
};

const APIKeyService = {
  create,
  revoke
};

export default APIKeyService;
