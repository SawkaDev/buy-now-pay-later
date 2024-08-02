import { ReactElement, useMemo } from 'react';
import { Grid, Tooltip } from '@mui/material';
import Layout from 'layout';
import Page from 'components/Page';
import MainCard from 'components/MainCard';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import APIKeyService from 'utils/database-services/APIKey';
import UserService from 'utils/database-services/User';
import { Chip } from '@mui/material';
import { Column } from 'react-table';
import { Stack } from '@mui/material';
import { IconButton } from '@mui/material';
import { CloseCircleTwoTone } from '@ant-design/icons';
import { ReactTable } from 'components/ui/Tables/ReactTable';
import TextFieldCopy from 'components/ui/Elements/TextFieldCopy';
import { ShowSnackBar } from 'utils/global-helpers';
import { APIErrorResponse } from 'types/database';

const APIKeys = () => {
  const queryClient = useQueryClient();

  const { data } = useQuery({
    queryKey: ['myData'],
    queryFn: UserService.getKeys
  });

  const { mutate: generateNewAPIKey } = useMutation({
    mutationFn: APIKeyService.create,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['myData'] });
      ShowSnackBar('New API Key Generated', 'success');
    },
    onError: (error: APIErrorResponse) => {
      // Handle errors, including the case where the user has reached the maximum number of API keys
      const errorMessage = error.response?.data?.message || 'Failed to generate API key';
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
        Header: 'key',
        accessor: 'key',
        Cell: ({ row }: any) => <TextFieldCopy value={`${row.original.key}`} />
      },
      {
        Header: 'Created',
        accessor: 'created_at',
        className: 'cell-left',
        Cell: ({ value }: any) => <>{new Date(value).toLocaleDateString()}</>
      },
      {
        Header: 'Expires',
        accessor: 'expires_at',
        className: 'cell-left',
        Cell: ({ value }: any) => <>{new Date(value).toLocaleDateString()}</>
      },
      {
        Header: 'Active',
        accessor: 'is_active',
        Cell: ({ value }: any) => {
          switch (value) {
            case value == true:
              return <Chip color="success" label="True" size="small" variant="light" />;
            case value == false:
              return <Chip color="error" label="False" size="small" variant="light" />;
            default:
              return <Chip color="info" label="n/a" size="small" variant="light" />;
          }
        }
      },
      {
        Header: 'Expire API Key',
        className: 'cell-center',
        disableSortBy: true,
        Cell: ({ row }: any) => {
          return (
            <Stack direction="row" alignItems="center" justifyContent="center" spacing={0}>
              <Tooltip title="Expire API Key">
                <IconButton
                  color="primary"
                  onClick={(e: any) => {
                    e.stopPropagation();
                    // localDelete(row.original._id);
                  }}
                >
                  <CloseCircleTwoTone twoToneColor="red" />
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
          <ReactTable
            columns={columns}
            data={data ? data : []}
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
