import axios from 'axios';

const serverBaseUrl = 'http://localhost:8080';

const getLoanOptions = async (userId: number, sessionId: string) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/loan-service/loan-options`, { user_id: userId, session_id: sessionId });
    return response.data.loan_options;
  } catch (error) {
    console.error('Error Getting Loan Opions:', error);
    throw error;
  }
};

const LoanService = {
  getLoanOptions
};

export default LoanService;
