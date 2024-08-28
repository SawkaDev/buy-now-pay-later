import { useTheme } from '@mui/material/styles';
import { Button, Chip, Grid, Stack, Typography } from '@mui/material';
import MainCard from 'components/MainCard';
import { EditOutlined } from '@ant-design/icons';

interface AddressCardProps {
  address: any | null;
  change?: boolean;
}

const LoanOption = ({ address, change }: AddressCardProps) => {
  const theme = useTheme();

  return (
    <MainCard
      sx={{
        '&:hover': {
          boxShadow: theme.customShadows.primary
        },
        cursor: 'pointer'
      }}
      onClick={() => {
        console.log('clicked');
      }}
    >
      {address && (
        <Grid container spacing={0.5}>
          <Grid item xs={12}>
            <Stack direction="row" justifyContent="space-between">
              <Stack direction="row" alignItems="center" spacing={0.5}>
                <Typography variant="subtitle1">{address.name}</Typography>
                <Typography variant="caption" color="textSecondary" sx={{ textTransform: 'capitalize' }}>
                  ({address.destination})
                </Typography>
                {address.isDefault && (
                  <Chip sx={{ color: 'primary.main', bgcolor: 'primary.lighter', borderRadius: '10px' }} label="Default" size="small" />
                )}
              </Stack>
              {change && (
                <Button
                  variant="outlined"
                  size="small"
                  color="secondary"
                  startIcon={<EditOutlined />}
                  onClick={() => {
                    console.log('change');
                  }}
                >
                  Change
                </Button>
              )}
            </Stack>
          </Grid>
          <Grid item xs={12}>
            <Stack spacing={2}>
              <Typography variant="body2" color="textSecondary">
                {`${address.building}, ${address.street}, ${address.city}, ${address.state}, ${address.country} - ${address.post}`}
              </Typography>
              <Typography variant="caption" color="textSecondary">
                {address.phone}
              </Typography>
            </Stack>
          </Grid>
        </Grid>
      )}
    </MainCard>
  );
};

export default LoanOption;
