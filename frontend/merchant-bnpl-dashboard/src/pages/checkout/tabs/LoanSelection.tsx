import { Grid, Typography, CircularProgress, Stack, Divider, Button, Alert, AlertTitle } from '@mui/material';
import { LoanOptionInterface, User } from 'types/common';
import { useQuery, UseQueryResult } from '@tanstack/react-query';
import LoanService from 'utils/database-services/Loans';
import LoanSelectionOption from './LoanSelectionOptions';
import MainCard from 'components/MainCard';
import LoanSummary from 'sections/apps/e-commerce/checkout/LoanSummary';
import { useState } from 'react';
import { InfoCircleFilled } from '@ant-design/icons';

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
    queryFn: () => LoanService.getLoanOptions(user?.user_id, sessionId),
    refetchOnWindowFocus: false
  });

  const [selectedLoan, setSelectedLoan] = useState<LoanOptionInterface>();

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
            <Button variant="contained" sx={{ textTransform: 'none' }} fullWidth onClick={onNext} disabled={!selectedLoan}>
              Confirm Loan Selection
            </Button>
          </Stack>
        </Grid>
      </Grid>
    </>
  );
};

export default LoanSelections;
