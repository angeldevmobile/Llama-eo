import secrets

# Genera una clave de 256 bits (32 bytes) codificada en base64 URL-safe
api_key = secrets.token_urlsafe(32)

print("Tu nueva API Key segura es:")
print(api_key)
