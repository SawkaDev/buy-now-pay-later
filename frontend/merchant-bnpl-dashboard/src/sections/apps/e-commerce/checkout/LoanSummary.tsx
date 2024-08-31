import { Stack, Table, TableBody, TableCell, TableContainer, TableRow, Typography } from '@mui/material';
import MainCard from 'components/MainCard';
import { LoanOptionInterface } from 'types/common';

const LoanSummary = ({ loan, show }: { loan: LoanOptionInterface; show?: boolean }) => {
  return (
    <Stack spacing={3}>
      <MainCard content={false} sx={{ borderRadius: show ? '4px' : '0 0 4px 4px', borderTop: show ? '1px inherit' : 'none' }}>
        <TableContainer>
          <Table sx={{ minWidth: 'auto' }} size="small" aria-label="simple table">
            <TableBody>
              {show && (
                <TableRow>
                  <TableCell>
                    <Typography variant="subtitle1">Loan Summary</Typography>
                  </TableCell>
                  <TableCell />
                </TableRow>
              )}
              <TableRow>
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>Purchase Amount</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  {loan.id && <Typography variant="subtitle1">${(loan.loan_amount_cents / 100).toFixed(2)}</Typography>}
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>APR</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  <Typography variant="subtitle1">{loan.interest_rate.toFixed(2)}%</Typography>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>Loan Term</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  {loan.id && <Typography variant="subtitle1">{loan.loan_term_months} months</Typography>}
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>Installement</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  {loan.id && <Typography variant="subtitle1">${(loan.monthly_payment / 100).toFixed(2)} /mo</Typography>}
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      </MainCard>
      <MainCard>
        <Stack direction="row" justifyContent="space-between" alignItems="center">
          <Typography variant="subtitle1">Total of Payments</Typography>
          <Typography variant="subtitle1" color={'success.main'} align="right">
            ${(loan.total_payment_amount / 100).toFixed(2)}
          </Typography>
        </Stack>
      </MainCard>
    </Stack>
  );
};

export default LoanSummary;
