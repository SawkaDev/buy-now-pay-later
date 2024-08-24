# TODO: add service level Rate Limiters
# "limits": ["10 per minute", "20 per second"]
services = {
    "merchant-integration-service": {
        "url": "http://merchant-integration-service:4000",
    },
    "user-service": {
        "url": "http://user-service:4000",
    },
}