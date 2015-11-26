import requests
import json
from django.http import HttpResponse, HttpResponseForbidden
import os


def spoof(request):
    secret_verifier = os.environ.get("SECRET_VERIFIER")

    url = "https://slack.com/api/users.list?token=" + os.environ.get("WEB_API_TOKEN") + "&pretty=1"

    data = request.GET
    if secret_verifier != data["token"]:
        return HttpResponseForbidden()
    channel_name = "#" + data["channel_name"]
    text = data["text"]
    array_text = text.split()
    username = array_text[0]
    message = ""
    for i in range(1, len(array_text)):
        message = message + " " + array_text[i]
    print message

    r = requests.get(url)

    response = json.loads(r.text)
    # print "Json user list response: " + str(response)

    full_name = ""
    for i in range(0, len(response["members"])):
        if response["members"][i]["name"] == username:
            full_name = response["members"][i]["name"]
            pic = response["members"][i]["profile"]["image_192"]
    if full_name == "":
        json_response = {"text": username + " does not exist."}
        return HttpResponse(json.dumps(json_response), content_type="application/json")

    url = os.environ.get("INCOMING_URL")
    payload = "{\"channel\": \"" + channel_name + "\"" + ", \"username\": \"" + full_name + "\"" + ", \"text\":" + "\"" + message + "\"" + ", \"icon_url\":" + "\"" + pic + "\"}"
    print payload
    r = requests.post(url, data=payload)
    print "Slack response: " + r.text

    # json_response = {"text": "shhh! Don't tell anybody I helped you with this!", "icon_emoji": ":santa:"}
    json_response = {"success": "true"}
    return HttpResponse(json.dumps(json_response), content_type="application/json")
