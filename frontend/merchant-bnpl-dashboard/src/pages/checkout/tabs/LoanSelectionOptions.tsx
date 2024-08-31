import { Grid } from '@mui/material';
import LoanOption from './LoanOption';
import { Dispatch, SetStateAction } from 'react';

export interface LoanSelectionOptionInterface {
  loanOptions: any;
  selectLoan: Dispatch<SetStateAction<any>>;
  selectedLoan: string | undefined;
}

const LoanSelectionOption = ({ loanOptions, selectLoan, selectedLoan }: LoanSelectionOptionInterface) => {
  return (
    <>
      <Grid container spacing={2}>
        {loanOptions &&
          loanOptions.map((loanOption: any) => {
            return (
              <Grid item xs={12} lg={6}>
                <LoanOption loan={loanOption} selected={selectedLoan == loanOption.id} selectLoan={selectLoan} />
              </Grid>
            );
          })}
      </Grid>
    </>
  );
};

export default LoanSelectionOption;
