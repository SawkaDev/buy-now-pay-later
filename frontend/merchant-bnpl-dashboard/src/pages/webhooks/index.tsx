import { ReactElement, useMemo } from 'react';
import { Grid, Tooltip } from '@mui/material';
import Layout from 'layout';
import Page from 'components/Page';
import MainCard from 'components/MainCard';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { Chip } from '@mui/material';
import { Column, Row } from 'react-table';
import { Stack } from '@mui/material';
import { IconButton } from '@mui/material';
import { CloseCircleTwoTone, EyeOutlined } from '@ant-design/icons';
import { ReactTable } from 'components/ui/Tables/ReactTable';
import { ShowSnackBar } from 'utils/global-helpers';
import { APIResponse } from 'types/database';
import useUser, { UserProps } from 'hooks/useUser';
import { useRouter } from 'next/router';
import WebhookService from 'utils/database-services/Webhook';
import { useTheme } from '@mui/material';

const APIKeys = () => {
  const queryClient = useQueryClient();
  const user = useUser();
  const router = useRouter();
  const theme = useTheme();

  const { data: webhooks } = useQuery({
    queryKey: ['webhooks', (user as UserProps).id],
    queryFn: () => WebhookService.getWebhooks((user as UserProps).id),
    enabled: !!user && !!user.id
  });

  const { mutate: disableWebHook } = useMutation({
    mutationFn: WebhookService.disableWebhooks,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['webhooks'] });
      ShowSnackBar('Webhook Disabled', 'success');
    },
    onError: (error: APIResponse) => {
      const errorMessage = error.response?.data?.error || 'Failed to Diabled Webhook' + JSON.stringify(error);
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
        Header: 'URL',
        accessor: 'url'
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
        Header: 'Created At',
        accessor: 'created_at',
        className: 'cell-left',
        Cell: ({ value }: any) => <>{new Date(value).toLocaleDateString()}</>
      },
      {
        Header: 'Actions',
        className: 'cell-center',
        disableSortBy: true,
        Cell: ({ row }: any) => {
          return (
            <Stack direction="row" alignItems="center" justifyContent="center" spacing={0}>
              <Tooltip title="View Activity">
                <IconButton
                  onClick={(e: any) => {
                    e.stopPropagation();
                  }}
                >
                  <EyeOutlined style={{ color: theme.palette.success.main }} />
                </IconButton>
              </Tooltip>
              <Tooltip title="Disable Webhook">
                <IconButton
                  disabled={!row.original.is_active}
                  onClick={(e: any) => {
                    e.stopPropagation();
                    disableWebHook(row.original.id);
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
    <Page title="Webhooks">
      <MainCard title="" content={false}>
        <Grid item xs={12}>
          <ReactTable
            columns={columns}
            data={webhooks ? webhooks.webhooks : []}
            getHeaderProps={(column: any) => column.getSortByToggleProps()}
            handleAdd={() => {
              router.push('/webhooks/add');
            }}
            addButtonText="Add Endpoint"
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
