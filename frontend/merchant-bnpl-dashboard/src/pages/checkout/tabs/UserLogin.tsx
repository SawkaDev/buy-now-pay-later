import {
  Button,
  Stack,
  TableBody,
  TableCell,
  Typography,
  TableRow,
  FormControl,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  Table,
  TableContainer,
  CircularProgress
} from '@mui/material';
import { useQuery } from '@tanstack/react-query';
import MainCard from 'components/MainCard';
import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import CreditService from 'utils/database-services/Credit';

interface UserLoginInterface {
  onNext: () => void;
  setUser: Dispatch<SetStateAction<any>>;
}

const UserLogin = ({ onNext, setUser }: UserLoginInterface) => {
  const [selectedUser, setSelectedUser] = useState('');

  const {
    data: creditProfiles,
    isLoading,
    error
  } = useQuery({
    queryKey: ['creditProfiles'],
    queryFn: () => CreditService.getCreditProfiles(),
    refetchOnWindowFocus: false
  });

  const handleUserChange = (event: any) => {
    setSelectedUser(event.target.value);
  };

  const profiles = Array.isArray(creditProfiles) ? creditProfiles : creditProfiles?.profiles || [];

  const selectedUserData = profiles.find((profile: any) => profile.user_id === selectedUser);

  useEffect(() => {
    setUser(selectedUserData);
  }, [selectedUserData, setUser]);

  if (isLoading) return <CircularProgress />;
  if (error) return <Typography color="error">Error loading credit profiles</Typography>;

  const fieldsToDisplay = [
    'name',
    'credit_score',
    'number_of_accounts',
    'credit_utilization_ratio',
    'recent_soft_inquiries',
    'bankruptcies',
    'tax_liens',
    'judgments'
  ];

  return (
    <Grid container spacing={3}>
      <Grid item xs={12} md={8}>
        <MainCard>
          <FormControl fullWidth>
            <InputLabel id="user-select-label">Select User</InputLabel>
            <Select labelId="user-select-label" id="user-select" value={selectedUser} label="Simulate Login As" onChange={handleUserChange}>
              {profiles.map((profile: any) => (
                <MenuItem key={profile.user_id} value={profile.user_id}>
                  {profile.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </MainCard>
      </Grid>
      <Grid item xs={12} md={4}>
        <Stack spacing={3}>
          <MainCard content={false}>
            <TableContainer>
              <Table sx={{ minWidth: 'auto' }} size="small" aria-label="user summary table">
                <TableBody>
                  <TableRow>
                    <TableCell>
                      <Typography variant="subtitle1">User Credit Profile</Typography>
                    </TableCell>
                    <TableCell />
                  </TableRow>
                  {selectedUserData &&
                    fieldsToDisplay.map((key) => (
                      <TableRow key={key}>
                        <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>
                          {key.charAt(0).toUpperCase() + key.slice(1).replace(/_/g, ' ')}
                        </TableCell>
                        <TableCell align="right" sx={{ borderBottom: 'none' }}>
                          <Typography variant="subtitle1">
                            {selectedUserData[key] !== null && selectedUserData[key] !== undefined ? String(selectedUserData[key]) : 'N/A'}
                          </Typography>
                        </TableCell>
                      </TableRow>
                    ))}
                </TableBody>
              </Table>
            </TableContainer>
          </MainCard>
          <Button variant="contained" sx={{ textTransform: 'none' }} fullWidth onClick={onNext} disabled={!selectedUser}>
            "Login" with Selected Credit Profile
          </Button>
        </Stack>
      </Grid>
    </Grid>
  );
};

export default UserLogin;
