# slack_spoof
A project built at BathHack 2015 to spoof messages in Slack

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Setup and Environment variables:

### INCOMING_URL
1. Go to https://YOUR_TEAM_NAME.slack.com/services/new#diy
2. Click on Incoming Webhooks
3. Chose any channel. (This slack_spoof integration works with all channels, but Slack wants you to chose a default one at this stage.) Keep in mind that in the channel that you do chose the following message will appear to all members of the channel: "*added an integration to this channel: incoming-webhook*"
4. Copy the URL in the *WebHook URL* section and paste it into the INCOMING_URL environment variable
