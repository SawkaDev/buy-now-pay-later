import { ReactElement, useMemo } from 'react';
import { Grid, Tooltip } from '@mui/material';
import Layout from 'layout';
import Page from 'components/Page';
import MainCard from 'components/MainCard';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import APIKeyService from 'utils/database-services/APIKey';
import { Chip } from '@mui/material';
import { Column, Row } from 'react-table';
import { Stack } from '@mui/material';
import { IconButton } from '@mui/material';
import { CloseCircleTwoTone } from '@ant-design/icons';
import { ReactTable } from 'components/ui/Tables/ReactTable';
import TextFieldCopy from 'components/ui/Elements/TextFieldCopy';
import { ShowSnackBar } from 'utils/global-helpers';
import { APIResponse } from 'types/database';
import UserService from 'utils/database-services/Auth';

// https://www.perplexity.ai/search/i-am-using-nextjs-and-next-aut-YvS6FrK0SIirsZphPjvDDA
const APIKeys = () => {
  const queryClient = useQueryClient();

  const { data: apiKeys } = useQuery({
    queryKey: ['apiKeys'],
    queryFn: APIKeyService.getKeys
  });

  const { data: tester } = useQuery({
    queryKey: ['sdfsd'],
    queryFn: UserService.checkSession
  });

  const { mutate: generateNewAPIKey } = useMutation({
    mutationFn: APIKeyService.create,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['apiKeys'] });
      ShowSnackBar('New API Key Generated', 'success');
    },
    onError: (error: APIResponse) => {
      // Handle errors, including the case where the user has reached the maximum number of API keys
      const errorMessage = error.response?.data?.error || 'Failed to generate API key.';
      ShowSnackBar(errorMessage, 'error');
    }
  });

  const { mutate: revokeKey } = useMutation({
    mutationFn: APIKeyService.revoke,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['apiKeys'] });
      ShowSnackBar('API Key Revoked', 'success');
    },
    onError: (error: APIResponse) => {
      const errorMessage = error.response?.data?.error || 'Failed to Revoke API Key' + JSON.stringify(error);
      ShowSnackBar(errorMessage, 'error');
    }
  });

  const columns: Column[] = useMemo(() => {
    var localCol = [
      {
        Header: 'ID',
        accessor: 'id'
      },
      {
        Header: 'API Key',
        accessor: 'key',
        Cell: ({ row }: any) => <TextFieldCopy value={`${row.original.key}`} />
      },
      {
        Header: 'Created At',
        accessor: 'created_at',
        className: 'cell-left',
        Cell: ({ value }: any) => <>{new Date(value).toLocaleDateString()}</>
      },
      {
        Header: 'Expires At',
        accessor: 'expires_at',
        className: 'cell-left',
        Cell: ({ value }: any) => <>{new Date(value).toLocaleDateString()}</>
      },
      {
        Header: 'Is Active',
        accessor: 'is_active',
        sortType: (rowA: Row<any>, rowB: Row<any>, columnId: string) => {
          const a = rowA.values[columnId];
          const b = rowB.values[columnId];
          if (a === b) return 0;
          return a ? -1 : 1; // For descending order, change to: return a ? 1 : -1;
        },
        Cell: ({ value }: any) => {
          switch (true) {
            case value:
              return <Chip color="success" label="True" size="small" variant="light" />;
            case !value:
              return <Chip color="error" label="False" size="small" variant="light" />;
            default:
              return <Chip color="info" label="n/a" size="small" variant="light" />;
          }
        }
      },
      {
        Header: 'Revoke',
        className: 'cell-center',
        disableSortBy: true,
        Cell: ({ row }: any) => {
          return (
            <Stack direction="row" alignItems="center" justifyContent="center" spacing={0}>
              <Tooltip title="Revoke API Key">
                <IconButton
                  disabled={!row.original.is_active}
                  onClick={(e: any) => {
                    e.stopPropagation();
                    revokeKey(row.original.id);
                  }}
                >
                  <CloseCircleTwoTone twoToneColor={row.original.is_active ? 'red' : '#d9d9d9'} />
                </IconButton>
              </Tooltip>
            </Stack>
          );
        }
      }
    ];
    return localCol;
  }, []);

  return (
    <Page title="API Keys">
      <MainCard title="" content={false}>
        <Grid item xs={12}>
          {JSON.stringify(tester)}
          <ReactTable
            columns={columns}
            data={apiKeys ? apiKeys.api_keys : []}
            getHeaderProps={(column: any) => column.getSortByToggleProps()}
            handleAdd={() => {
              generateNewAPIKey();
            }}
            addButtonText="Generate New Key"
          />
        </Grid>
      </MainCard>
    </Page>
  );
};

APIKeys.getLayout = function getLayout(page: ReactElement) {
  return <Layout>{page}</Layout>;
};

export default APIKeys;
