export async function createCheckoutSession(params: {
  loan_amount_cents: number;
  merchant_id: string;
  order_id: string;
  success_redirect_url: string;
  cancel_redirect_url: string;
}) {
  const res = await fetch('http://localhost:8080/api/loan-service/checkout/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(params),
  });

  if (!res.ok) {
    throw new Error('Failed to create checkout session');
  }
  return res.json();
}
