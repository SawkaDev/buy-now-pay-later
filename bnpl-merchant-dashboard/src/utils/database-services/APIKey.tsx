import axios from 'axios';

const serverBaseUrl = 'http://localhost:4000';
const get = async () => {
  let { data } = await axios.get(`${serverBaseUrl}/api/flask/users`);
  return data;
};

const create = async () => {
  try {
    const response = await axios.post(
      `${serverBaseUrl}/api/flask/generate_key`,
      { user_id: 1 },
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error generating API key:', error);
    throw error;
  }
};

// const update = async (apiData: INarrativeTemplates, meta: APIMetaData) => {
//   let { data } = await axios.put(`/api/narrativeTemplates`, { data: { data: apiData, meta: meta } });
//   return data;
// };

const APIKeyService = {
  get,
  create
};

export default APIKeyService;
