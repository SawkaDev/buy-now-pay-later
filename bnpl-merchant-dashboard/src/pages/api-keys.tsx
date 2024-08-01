import { ReactElement } from 'react';

// material-ui
import { Button, Typography } from '@mui/material';

// project imports
import Layout from 'layout';
import Page from 'components/Page';
import MainCard from 'components/MainCard';
import { useMutation, useQuery } from '@tanstack/react-query';
import APIKeyService from 'utils/database-services/APIKey';

// ==============================|| SAMPLE PAGE ||============================== //

const APIKeys = () => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['myData'],
    queryFn: APIKeyService.get
  });

  const { mutate: tester } = useMutation({
    mutationFn: APIKeyService.create,
    onSuccess: (data) => {
      // Invalidate and refetch
      console.log('New API Key:', data.api_key);
    }
  });

  return (
    <Page title="API Keys">
      <MainCard title="Sample Card">
        {JSON.stringify(data)}
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
