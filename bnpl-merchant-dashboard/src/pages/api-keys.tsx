import { ReactElement } from 'react';

// material-ui
import { Button, Grid, Typography } from '@mui/material';

// project imports
import Layout from 'layout';
import Page from 'components/Page';
import MainCard from 'components/MainCard';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import APIKeyService from 'utils/database-services/APIKey';
import UserService from 'utils/database-services/User';

// ==============================|| SAMPLE PAGE ||============================== //

const APIKeys = () => {
  const queryClient = useQueryClient();

  const { data } = useQuery({
    queryKey: ['myData'],
    queryFn: UserService.getKeys
  });

  const { mutate: tester } = useMutation({
    mutationFn: APIKeyService.create,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['myData'] });
    }
  });

  return (
    <Page title="API Keys">
      <MainCard title="Sample Card">
        {data &&
          data.api_keys.map((key: any) => {
            return (
              <Grid container>
                <Grid item xs={2}>
                  {key.created_at}
                </Grid>
                <Grid item xs={2}>
                  {key.expires_at}
                </Grid>
                <Grid item xs={2}>
                  {JSON.stringify(key.is_active)}
                </Grid>
                <Grid item xs={2}>
                  User_Id: {JSON.stringify(data.user.name)}
                </Grid>
                <Grid item xs={4}>
                  {key.key}
                </Grid>
              </Grid>
            );
          })}
        <Typography variant="body2">
          <Button
            variant="contained"
            onClick={() => {
              tester();
            }}
          >
            Create Key
          </Button>
        </Typography>
      </MainCard>
    </Page>
  );
};

APIKeys.getLayout = function getLayout(page: ReactElement) {
  return <Layout>{page}</Layout>;
};

export default APIKeys;
