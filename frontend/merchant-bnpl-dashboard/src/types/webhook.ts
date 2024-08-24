import * as yup from 'yup';
import { SchemaOf } from 'yup';

export interface WebHook {
  url: string;
}

export const mock_WebHook: WebHook = {
  url: ''
};

export const yup_WebHook: SchemaOf<WebHook> = yup.object().shape({
  url: yup.string().url('Invalid URL Format').required('URL is required')
});
