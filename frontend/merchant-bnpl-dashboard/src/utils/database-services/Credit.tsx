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

const getLoanOptions = async (userId: string, sessionId: string) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/credit-service/loan-options`, { user_id: userId, session_id: sessionId });
    return response.data.loan_options;
  } catch (error) {
    console.error('Error Getting Loan Opions:', error);
    throw error;
  }
};

const getLoanStatus = async (checkoutSessionId: string, userId: string) => {
  try {
    const response = await axios.get(`${serverBaseUrl}/api/credit-service/loan-status`, {
      params: {
        checkout_session_id: checkoutSessionId,
        user_id: userId
      }
    });
    return response.data.status;
  } catch (error) {
    console.error('Error Getting Loan Status:', error);
    throw error;
  }
};

const CreditService = {
  getCreditProfiles,
  getLoanOptions,
  getLoanStatus
};

export default CreditService;
