import axios from 'axios';

const serverBaseUrl = 'http://localhost:8080';

const create = async ({ userId, url }: { userId: number; url: string }) => {
  try {
    const response = await axios.post(`${serverBaseUrl}/api/merchant-integration-service/webhooks`, { user_id: userId, url: url });
    return response.data;
  } catch (error) {
    console.error('Error creating webhooks:', error);
    throw error;
  }
};

const getWebhooks = async (userId: number) => {
  let { data } = await axios.get(`${serverBaseUrl}/api/merchant-integration-service/webhooks/user/${userId}`);
  return data;
};

const disableWebhooks = async (webhookId: number) => {
  let { data } = await axios.delete(`${serverBaseUrl}/api/merchant-integration-service/webhooks/${webhookId}`);
  return data;
};

const WebhookService = {
  create,
  getWebhooks,
  disableWebhooks
};

export default WebhookService;
