import json
import spotipy
import requests
import structlog

spotipy.Spotify()
logger = structlog.get_logger()

client_id = "51e504413e18451b983e95d3d33bb336"
secret_key = "52ae74ac3e354ef79df882807729e53d"


DUMMY_FEED = { "statusCode": 200,
                "body": json.dumps({
                    "message": f"Generated feed for salito",
                    "Post": {
                        "User": f"salito",
                        "Song": {
                            "name": "Everlong",
                            "artist": "Foo Fighters",
                            "artistUrl": "https://open.spotify.com/artist/7jy3rLJdDQY21OgRLCZ9sD",
                            "albumArt": "https://i.scdn.co/image/ab67616d00001e020389027010b78a5e7dce426b",
                            "songUrl": "https://open.spotify.com/track/5UWwZ5lm5PKu6eKsHAGxOk?si=c85aed7d81a848ef",
                            "previewUrl": "placeholder string here"
                        }
                    }
                })
            }

def lambda_handler(event, context):

    logger.info(event)

    try:
        body = event["body"]
        # json.loads() takes in a string and turns it to a json parseable structure
        userid = json.loads(body)["userid"]
    except:
        logger.info("No id passed in!")
        return DUMMY_FEED
    
    result = { "statusCode": 200,
                "body": json.dumps({
                    "message": f"Generated feed for {userid}",
                    "Post": {
                        "User": f"{userid}",
                        "Song": {
                            "name": "Everlong",
                            "artist": "Foo Fighters",
                            "artistUrl": "https://open.spotify.com/artist/7jy3rLJdDQY21OgRLCZ9sD",
                            "albumArt": "https://i.scdn.co/image/ab67616d00001e020389027010b78a5e7dce426b",
                            "songUrl": "https://open.spotify.com/track/5UWwZ5lm5PKu6eKsHAGxOk?si=c85aed7d81a848ef",
                            "previewUrl": "placeholder string here"
                        }
                    }
                })
            }

    return result
