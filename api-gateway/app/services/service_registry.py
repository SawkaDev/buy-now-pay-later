import logging

logger = logging.getLogger(__name__)

services = {
    "api-service": {
        "url": "http://flaskapp:4000",
        "limits": ["10 per minute", "20 per second"]
    },
    # Add more services here with their specific limits
}

def get_service_limits(service):
    if service in services:
        limits = services[service].get("limits", ["10 per minute"])
        logger.info(f"Retrieved limits for service '{service}': {limits}")
        return limits
    else:
        logger.warning(f"Service '{service}' not found. Using default limits.")
        return ["10 per minute"]  # Default limit if service is not found
