from webhook_service.client.v1.client import WebhookClientV1

def test_webhook_service():
    client = WebhookClientV1()
    
    # Test creating a webhook
    response = client.create_webhook(user_id=1, url="https://matt.com/webhook")
    print("Created webhook:", response)
    
    # Test getting webhooks
    response = client.get_webhooks(user_id=1)
    print("Got webhooks:", response)

if __name__ == "__main__":
    test_webhook_service()
