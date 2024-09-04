import { useTheme } from '@mui/material/styles';
import { Grid, Stack, Typography, Box } from '@mui/material';
import MainCard from 'components/MainCard';
import { DollarOutlined, CalendarOutlined, PercentageOutlined } from '@ant-design/icons';
import { Dispatch, SetStateAction } from 'react';
import { LoanOptionInterface } from 'types/common';

interface LoanOptionProps {
  loan: LoanOptionInterface;
  selectLoan: Dispatch<SetStateAction<any>>;
  selected: boolean;
}

const LoanOption = ({ loan, selectLoan, selected }: LoanOptionProps) => {
  const theme = useTheme();

  const selectedBoxShadow = `0 0 0 2px ${theme.palette.success.main}`;
  const selectedBoxShadowNext = `0 0 0 2px ${theme.palette.secondary.light}`;

  return (
    <MainCard
      sx={{
        boxShadow: selected ? selectedBoxShadow : 'none',
        '&:hover': {
          boxShadow: selected ? selectedBoxShadow : selectedBoxShadowNext,
          transform: selected ? 'none' : 'translateY(-4px)',
          transition: 'all 0.3s'
        },
        mt: 2,
        cursor: selected ? 'default' : 'pointer'
      }}
      onClick={() => !selected && selectLoan(loan)}
    >
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Stack direction="row" justifyContent="space-between" alignItems="center">
            <Typography variant="h4" fontWeight="bold">
              ${(loan.monthly_payment_cents / 100).toFixed(2)}
            </Typography>
            <Typography variant="subtitle1" color="textSecondary">
              per month
            </Typography>
          </Stack>
        </Grid>
        <Grid item xs={12}>
          <Box bgcolor={theme.palette.grey[100]} p={2} borderRadius={1}>
            <Stack spacing={1}>
              <Typography variant="body2" display="flex" alignItems="center">
                <CalendarOutlined style={{ marginRight: 8 }} />
                {loan.loan_term_months} monthly payments
              </Typography>
              <Typography variant="body2" display="flex" alignItems="center">
                <PercentageOutlined style={{ marginRight: 8 }} />
                {loan.interest_rate} APR
              </Typography>
              <Typography variant="body2" display="flex" alignItems="center">
                <DollarOutlined style={{ marginRight: 8 }} />${((loan.total_payment_amount_cents - loan.loan_amount_cents) / 100).toFixed(2)}{' '}
                interest paid
              </Typography>
            </Stack>
          </Box>
        </Grid>
      </Grid>
    </MainCard>
  );
};

export default LoanOption;
