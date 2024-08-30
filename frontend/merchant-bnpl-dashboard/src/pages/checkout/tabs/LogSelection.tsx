import { Grid, Typography, CircularProgress } from '@mui/material';
import { LoanOptionInterface, User } from 'types/common';
import { useQuery, UseQueryResult } from '@tanstack/react-query';
import LoanService from 'utils/database-services/Loans';
import LoanOption from './LoanOption';

interface LoanSelections {
  sessionId: string;
  user: User;
}

const LoanSelections = ({ sessionId, user }: LoanSelections) => {
  const {
    data: loanOptions,
    isLoading,
    error
  } = useQuery<UseQueryResult<LoanOptionInterface[], Error>>({
    queryKey: ['loanOptions', user?.id, sessionId],
    queryFn: () => LoanService.getLoanOptions(user?.id, sessionId)
  });

  if (isLoading) {
    return (
      <Grid container justifyContent="center" alignItems="center" style={{ height: '100vh' }}>
        <CircularProgress />
      </Grid>
    );
  }

  if (error) {
    return (
      <Grid container justifyContent="center" alignItems="center" style={{ height: '100vh' }}>
        <Typography variant="h6" color="error">
          Error fetching loan options.
        </Typography>
      </Grid>
    );
  }

  return (
    <>
      <Typography variant="h6">Session ID: {sessionId}</Typography>
      <Typography variant="body1">User Info: {JSON.stringify(user)}</Typography>
      <Grid container spacing={2} pt={2}>
        <Grid item xs={12} lg={12}>
          {loanOptions &&
            Object.entries(loanOptions).map((loanOption: any) => {
              return (
                <LoanOption
                  address={{
                    building: loanOption.loan_term_months, // Replace with actual data
                    city: loanOption.loan_amount_cents , // Replace with actual data
                    country: loanOption.monthly_payment, // Replace with actual data
                    destination: 'asdf', // Replace with actual data
                    isDefault: true,
                    name: 'mat', // Replace with actual data
                    phone: '10', // Replace with actual data
                    post: '4242', // Replace with actual data
                    state: 'asdf', // Replace with actual data
                    street: 'asdfsd' // Replace with actual data
                  }}
                  change={true} // Adjust this prop based on your logic
                />
              );
            })}
        </Grid>
      </Grid>
    </>
  );
};

export default LoanSelections;
