from dotenv import dotenv_values
import requests as rq
import pymongo
import typing


def auth(
    spotify_client_id: str,
    spotify_client_secret: str
) -> str:
    TOKEN_URL = "https://accounts.spotify.com/api/token" 

    response = rq.post(
        url=TOKEN_URL,
        auth=(spotify_client_id, spotify_client_secret),
        data={
            'Content-Type': 'application/x-www-form-urlencoded',
            'grant_type': 'client_credentials',
        }
    )

    response_data = response.json()
    access_token = response_data.get('access_token')
    return access_token


def clean_unicode(text: str) -> str:
    return text \
        .encode("ascii", "ignore") \
        .decode()

        
def get_pods(
    access_token: str, 
    podcast_show_id: str, 
    offset: int = 0,
    limit: int = 50,
    market: str = 'ES'
) -> typing.Tuple[typing.List[dict], typing.Union[str, None]]:

    res = rq.get(
        url = f"https://api.spotify.com/v1/shows/{podcast_show_id}/episodes" + \
            f"?market={market}&limit={limit}&offset={offset}",
        headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }    
    )

    res_data = res.json()
    pods = res_data["items"]
    next = res_data["next"]

    cleaned_podcasts = []

    for pod in pods:
    
        podcast_url = pod["external_urls"]["spotify"]
        duration = round(int(pod["duration_ms"]) / 60000)
        release_date = pod["release_date"]
        name = clean_unicode(pod["name"])

        description = clean_unicode(
            pod["description"][0:pod["description"] \
                .find("See Privacy Policy")] \
                .strip()
        )
        
        cleaned_podcasts.append({
            "name": name,
            "description": description,
            "spotify_url": podcast_url,
            "duration_mins": duration,
            "release_date": release_date
        })

    return (cleaned_podcasts, next)


def all_pods(
    access_token: str, 
    podcast_show_id: str, 
    db_cursor
) -> None:

    all_data, index = [], 0

    while True:
        data, next = get_pods(
            podcast_show_id = podcast_show_id, 
            access_token = access_token, 
            offset = index
        )

        all_data.extend(data)
        index += 50
        if next == None: break

    try:
        db_cursor.insert_many(all_data)
    except Exception as err:
        print("Insertion failed")


if __name__ == "__main__":
    config = dotenv_values(".env")

    SPOTIFY_CLIENT_ID = config["SPOTIFY_CLIENT_ID"]
    SPOTIFY_CLIENT_SECRET = config["SPOTIFY_CLIENT_SECRET"]

    MONGO_DB_USERNAME = config["MONGO_DB_USERNAME"]
    MONGO_DB_PASSWORD = config["MONGO_DB_PASSWORD"]
    MONGO_DB_ADDRESS = config["MONGO_DB_ADDRESS"]

    conn_str = f"mongodb+srv://{MONGO_DB_USERNAME}" + \
        f":{MONGO_DB_PASSWORD}@{MONGO_DB_ADDRESS}" + \
        f"/podcast?retryWrites=true&w=majority"

    client = pymongo.MongoClient(conn_str)
    db_cursor = client["podcast"]["guy-raz"]

    PODCAST_SHOW_ID = "6E709HRH7XaiZrMfgtNCun"

    ACCESS_TOKEN = auth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

    all_pods(ACCESS_TOKEN, PODCAST_SHOW_ID, db_cursor)