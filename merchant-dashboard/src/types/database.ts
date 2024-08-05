import { AxiosError } from 'axios';

interface APIResponses {
  message?: string;
  error?: string;
}

export type APIResponse = AxiosError<APIResponses>;
