import axios from 'axios';

const serverBaseUrl = 'http://localhost:8080';

const getCreditProfiles = async () => {
  try {
    const response = await axios.get(`${serverBaseUrl}/api/credit-service/profiles`);
    return response.data;
  } catch (error) {
    console.error('Error Getting Loan Opions:', error);
    throw error;
  }
};

const CreditService = {
  getCreditProfiles
};

export default CreditService;
