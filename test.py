import requests

url = "http://127.0.0.1:47823/event"
headers = {"Content-Type": "application/json"}

print("Probando conexión con Capri...")
try:
    r = requests.post(url, json={
        "hook_event_name": "tool_use",
        "message": "¡Hola Capri, soy Hermes!",
        "tool": "Hermes Test"
    }, headers=headers, timeout=3)
    print(f"Respuesta de Capri: HTTP {r.status_code} -> {r.json()}")
except Exception as e:
    print(f"❌ Error al conectar con Capri: {e}")