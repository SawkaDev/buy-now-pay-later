import { AxiosError } from 'axios';

interface APIError {
  message: string;
}

export type APIErrorResponse = AxiosError<APIError>;
