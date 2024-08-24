import { ReactElement, useState } from 'react';

// material-ui
import { Divider, Grid } from '@mui/material';

// project imports
import Layout from 'layout';
import Page from 'components/Page';
import MainCard from 'components/MainCard';
import TextInputWrapper from 'components/form/TextInputWrapper';
import { mock_WebHook, WebHook, yup_WebHook } from 'types/webhook';
import { FormProvider, useForm } from 'react-hook-form';
import CancelSubmitButton from 'components/form/CancelSubmitButton';
import { yupResolver } from '@hookform/resolvers/yup';
import { useMutation } from '@tanstack/react-query';
import { ShowSnackBar } from 'utils/global-helpers';
import { APIResponse } from 'types/database';
import WebhookService from 'utils/database-services/Webhook';
import useUser from 'hooks/useUser';
import { useRouter } from 'next/router';

// ==============================|| AddEditWebhook ||============================== //

const AddEditWebhook = () => {
  const methods = useForm<WebHook>({
    resolver: yupResolver(yup_WebHook),
    mode: 'all',
    defaultValues: mock_WebHook,
    delayError: 1000
  });

  const user = useUser();
  const router = useRouter();
  const [isSubmitting, setisSubmitting] = useState<boolean>(false);

  const { mutate: createWebHook } = useMutation({
    mutationFn: async ({ userId, url }: any) => {
      try {
        setisSubmitting(true);
        await WebhookService.create({ userId, url });
      } catch {
        setisSubmitting(false);
      }
    },
    onSuccess: () => {
      ShowSnackBar('Webhook Created', 'success');
      router.push('/webhooks');
    },
    onError: (error: APIResponse) => {
      const errorMessage = error.response?.data?.error || 'Failed to create webhook key.';
      ShowSnackBar(errorMessage, 'error');
      setisSubmitting(false);
    }
  });

  function handleSubmit() {
    if (user && user.id) {
      createWebHook({ userId: user.id, url: methods.getValues().url as string });
    }
  }

  return (
    <Page title="Add Webhook">
      <MainCard title="Add Webhook">
        <FormProvider {...methods}>
          <form onSubmit={methods.handleSubmit(handleSubmit)}>
            <Grid container spacing={2}>
              <Grid item xs={6}>
                <TextInputWrapper name="url" label="Endpoint URL" textalign="left" />
              </Grid>
              <Grid item xs={12}>
                <Divider />
              </Grid>
              <Grid item xs={12}>
                <CancelSubmitButton url="/webhooks" isSubmitting={isSubmitting} justify="left" />
              </Grid>
            </Grid>
          </form>
        </FormProvider>
      </MainCard>
    </Page>
  );
};

AddEditWebhook.getLayout = function getLayout(page: ReactElement) {
  return <Layout>{page}</Layout>;
};

export default AddEditWebhook;
