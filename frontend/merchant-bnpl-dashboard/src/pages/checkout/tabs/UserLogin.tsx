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
  TableContainer
} from '@mui/material';
import MainCard from 'components/MainCard';
import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { User } from 'types/common';

interface UserLoginInterface {
  onNext: () => void;
  setUser: Dispatch<SetStateAction<any>>;
}

const UserLogin = ({ onNext, setUser }: UserLoginInterface) => {
  const [selectedUser, setSelectedUser] = useState();

  const handleUserChange = (event: any) => {
    setSelectedUser(event.target.value);
  };

  const users: Array<User> = [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Jane Smith' },
    { id: 3, name: 'Bob Johnson' }
  ];

  const selectedUserData = users.find((user) => user.id === selectedUser);

  useEffect(() => {
    setUser(selectedUserData);
  }, [selectedUserData]);

  return (
    <Grid container spacing={3}>
      <Grid item xs={12} md={8}>
        <MainCard>
          <FormControl fullWidth>
            <InputLabel id="user-select-label">Select User</InputLabel>
            <Select labelId="user-select-label" id="user-select" value={selectedUser} label="Select User" onChange={handleUserChange}>
              {users.map((user) => (
                <MenuItem key={user.id} value={user.id}>
                  {user.name}
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
                      <Typography variant="subtitle1">User Login Summary</Typography>
                    </TableCell>
                    <TableCell />
                  </TableRow>
                  <TableRow>
                    <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>Name</TableCell>
                    <TableCell align="right" sx={{ borderBottom: 'none' }}>
                      <Typography variant="subtitle1">{selectedUserData?.name || 'N/A'}</Typography>
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell sx={{ borderBottom: 'none', opacity: 0.5 }}>User ID</TableCell>
                    <TableCell align="right" sx={{ borderBottom: 'none' }}>
                      <Typography variant="subtitle1">{selectedUserData?.id || 'N/A'}</Typography>
                    </TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </TableContainer>
          </MainCard>
          <Button variant="contained" sx={{ textTransform: 'none' }} fullWidth onClick={onNext} disabled={!selectedUser}>
            Next
          </Button>
        </Stack>
      </Grid>
    </Grid>
  );
};

export default UserLogin;
