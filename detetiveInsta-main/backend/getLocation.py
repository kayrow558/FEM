import requests

def getLocation():
    try:
        # Usando um serviço de localização por IP
        response = requests.get('https://ipinfo.io')
        data = response.json()
        
        # Capturando os principais dados de localização
        location_data = {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "loc": data.get("loc")
        }
        return location_data
    except Exception as e:
        return {"error": str(e)}
