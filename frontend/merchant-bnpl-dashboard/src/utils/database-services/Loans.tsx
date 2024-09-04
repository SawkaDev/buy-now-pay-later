import axios from 'axios';

const serverBaseUrl = 'http://localhost:8080';

const selectLoanCheckout = async (
  user_id: string,
  checkout_session_id: string,
  loan_term_months: number,
  interest_rate: number,
  monthly_payment_cents: number,
  total_payment_amount_cents: number
) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/credit-service/select-loan`, {
      user_id: user_id,
      checkout_session_id: checkout_session_id,
      loan_term_months: loan_term_months,
      interest_rate: interest_rate,
      monthly_payment_cents: monthly_payment_cents,
      total_payment_amount_cents: total_payment_amount_cents
    });
    return response.data;
  } catch (error) {
    console.error('Error Getting Loan Opions:', error);
    throw error;
  }
};

const LoanService = {
  selectLoanCheckout
};

export default LoanService;
