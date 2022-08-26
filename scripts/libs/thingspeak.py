from urequests import get as req_get


def post(write_api_key, **fields):
    """Post data to ThingSpeak

    Args:
            write_api_key (str): ThingSpeak write API key
            fields (dict): Data to post to ThingSpeak, e.g. field1=1, field2=2
    """
    url = f"https://api.thingspeak.com/update?api_key={write_api_key}"
    for key, value in fields.items():
        if value is not None:
            url += f"&{key}={value}"
    try:
        response = req_get(url)
        if response.status_code != 200:
            print("Error posting to ThingSpeak")
        response.close()
    except Exception:
        pass
