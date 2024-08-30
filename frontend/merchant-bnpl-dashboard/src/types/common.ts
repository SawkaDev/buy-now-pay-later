export type Nullable<T> = T | null | undefined;

export interface User {
  id: number;
  name: string;
}

export interface LoanOptionInterface {
  id: string;
  loan_amount_cents: number;
  loan_term_months: number;
  interest_rate: number;
  monthly_payment: number;
  total_payment_amount: number;
}
