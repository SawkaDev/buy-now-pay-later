import { Grid, Typography, CircularProgress, Stack, Divider, Button, Alert, AlertTitle } from '@mui/material';
import { LoanOptionInterface, User } from 'types/common';
import { useMutation, useQuery, UseQueryResult } from '@tanstack/react-query';
import LoanSelectionOption from './LoanSelectionOptions';
import MainCard from 'components/MainCard';
import LoanSummary from 'sections/apps/e-commerce/checkout/LoanSummary';
import { useState } from 'react';
import { InfoCircleFilled } from '@ant-design/icons';
import CreditService from 'utils/database-services/Credit';
import LoanService from 'utils/database-services/Loans';
import { ShowSnackBar } from 'utils/global-helpers';

export interface LoanSelections {
  sessionId: string;
  user: User;
  onNext: () => void;
}

const LoanSelections = ({ sessionId, user, onNext }: LoanSelections) => {
  const {
    data: loanOptions,
    isLoading,
    error
  } = useQuery<UseQueryResult<LoanOptionInterface[], Error>>({
    queryKey: ['loanOptions', user?.user_id, sessionId],
    queryFn: () => CreditService.getLoanOptions(user?.user_id, sessionId),
    refetchOnWindowFocus: false
  });

  const [disabled, setDisabled] = useState(false);

  const [selectedLoan, setSelectedLoan] = useState<LoanOptionInterface>();

  const { mutate: selectLoan } = useMutation({
    mutationFn: () => {
      setDisabled(true);
      if (selectedLoan) {
        return LoanService.selectLoanCheckout(
          user?.user_id,
          sessionId,
          selectedLoan?.loan_term_months,
          selectedLoan?.interest_rate,
          selectedLoan?.monthly_payment_cents,
          selectedLoan?.total_payment_amount_cents
        );
      } else {
        return Promise.reject('No loan selected');
      }
    },
    onSuccess: (data) => {
      if (data.success) {
        console.log('Loan Selected!');
        onNext();
        ShowSnackBar('Loan Selected!', 'success');
      } else {
        ShowSnackBar('Error Selecting Loan!', 'error');
      }
      setDisabled(false);
    },
    onError: (error) => {
      setDisabled(false);
      // const errorMessage = error.response?.data?.error || 'Failed to Diabled Webhook' + JSON.stringify(error);
      ShowSnackBar(JSON.stringify(error), 'error');
    }
  });

  const submitLoan = () => {
    selectLoan();
  };

  if (isLoading) {
    return (
      <Grid container justifyContent="center" alignItems="center" style={{ height: '25vh', textAlign: 'center' }}>
        <Grid item>
          <CircularProgress />
          <Typography variant="h5" style={{ marginTop: '16px' }}>
            Performing credit check and fetching loans
          </Typography>
        </Grid>
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
      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Stack spacing={2}>
            <MainCard content={false}>
              <Grid container>
                <Grid item xs={12} sx={{ py: 2.5, pl: 2.5 }}>
                  <Stack direction="row" alignItems="center" spacing={1}>
                    <Typography variant="subtitle1">Loan Options</Typography>
                  </Stack>
                </Grid>
                <Grid item xs={12}>
                  <Divider />
                </Grid>
                <Grid item xs={12}>
                  <p>UserId: {user.user_id}</p>
                  <p>SessionId: {sessionId}</p>
                </Grid>

                {!selectedLoan && (
                  <Grid item xs={12} sx={{ px: 2.5, pt: 2.5 }}>
                    <Alert color={'info'} variant="standard" icon={<InfoCircleFilled />}>
                      <AlertTitle>
                        <b>Please select one of the loan options below.</b>
                      </AlertTitle>
                    </Alert>
                  </Grid>
                )}
                <Grid item xs={12} sx={{ p: 2.5 }}>
                  {user && sessionId && loanOptions && (
                    <LoanSelectionOption loanOptions={loanOptions} selectLoan={setSelectedLoan} selectedLoan={selectedLoan?.id} />
                  )}
                </Grid>
              </Grid>
            </MainCard>
          </Stack>
        </Grid>
        <Grid item xs={12} md={4}>
          <Stack spacing={3}>
            <LoanSummary loan={selectedLoan} show />
            <Button variant="contained" sx={{ textTransform: 'none' }} fullWidth onClick={submitLoan} disabled={!selectedLoan || disabled}>
              Confirm Loan Selection
            </Button>
          </Stack>
        </Grid>
      </Grid>
    </>
  );
};

export default LoanSelections;
