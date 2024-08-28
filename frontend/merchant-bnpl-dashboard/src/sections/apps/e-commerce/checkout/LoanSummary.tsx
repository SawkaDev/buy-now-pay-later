import { Stack, Table, TableBody, TableCell, TableContainer, TableRow, Typography } from '@mui/material';
import MainCard from 'components/MainCard';
import { LoanApplicationInterface } from 'types/LoanApplication';

const LoanSummary = ({ loan, show }: { loan: LoanApplicationInterface; show?: boolean }) => {
  var loanInterest = (loan.interest / 100) * loan.loanAmount;
  var installment = (loan.loanAmount + loanInterest) / loan.loanTermMonths;

  var total = loanInterest + loan.loanAmount;

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
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>Merchant</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  {loan.merchant && <Typography variant="subtitle1">{loan.merchant}</Typography>}
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>Installement</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  {loan.interest && <Typography variant="subtitle1">${installment.toFixed(2)} /mo</Typography>}
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>APR</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  <Typography variant="subtitle1">{loan.interest.toFixed(2)}%</Typography>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>Interest</TableCell>
                <TableCell align="right" sx={{ borderBottom: 'none' }}>
                  {loan.interest && <Typography variant="subtitle1">${loanInterest.toFixed(2)}</Typography>}
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      </MainCard>
      <MainCard>
        <Stack direction="row" justifyContent="space-between" alignItems="center">
          <Typography variant="subtitle1">Total</Typography>
          <Typography variant="subtitle1" color={'success.main'} align="right">
            ${total.toFixed(2)}
          </Typography>
        </Stack>
      </MainCard>
    </Stack>
  );
};

export default LoanSummary;
