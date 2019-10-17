import os

# development is default
env = os.environ.get("PYTHON_ENV", "development")

all_environments = {
    "development": {"port": 5000, "debug": True, "swagger-url": "/api/swagger"},
    "proxied": {"host": "0.0.0.0", "port": 5000, "debug": True, "swagger-url": "/api/swagger"},
    "production": {"port": 8080, "debug": False, "swagger-url": None}
}

# The config for the current environment
environment_config = all_environments[env]
