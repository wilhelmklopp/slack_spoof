# Slack Spoof
A project built at BathHack 2015 to spoof messages in Slack

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Demo

![Demo](http://zippy.gfycat.com/QualifiedBlondIndigowingedparrot.gif)

## Setup and Environment variables:

Disclaimer: For this to work, you need to have the right to add more Slack integrations for you team(i.e. be an Admin).

To get started open the link behind the Deploy to Heroku button in a new tab and then follow the instructions here.

### INCOMING_URL
1. Go to https://YOUR_TEAM_NAME.slack.com/services/new#diy
2. Click on Incoming Webhooks
3. Choose any channel. (This slack_spoof integration works with all channels, but Slack wants you to choose a default one at this stage.) Keep in mind that in the channel that you do choose the following message will appear to all members of the channel: "*added an integration to this channel: incoming-webhook*"
4. Copy the URL in the *WebHook URL* section and paste it into the **INCOMING_URL** environment variable
5. Click Save Integration at the bottom.

### WEB_API_TOKEN
1. Go to https://YOUR_TEAM_NAME.slack.com/services/new#diy
2. Click on Slack API
3. Click on Web API on the sidebar on the left
4. Scroll down and click **Create Token** next to the relevant team name
5. At this stage Slack may ask you to re-enter your password. In this case repeat these **WEB_API_TOKEN" instructions from step 3
6. Copy the token, which should start with `xoxp` and paste it into **WEB_API_TOKEN** environment variable

### SECRET_VERIFIER
1. To get all the data that is required for this setup, the app needs to be deployed first. Heroku requires all environment variables to have a value, so far now you can just put `0`
2. Click **Deploy for Free**
3. After the build finishes, Heroku will tell you that the app was successfully deployed and will display a "View" button. Click this button and copy the URL that it navigates to. (Don't worry if you see an error at this stage. This is expected.) Unless you specified a name in the Heroku setup, the URL should be in the following format: `http://desolate-bastion-9841.herokuapp.com/`
4. Go to https://YOUR_TEAM_NAME.slack.com/services/new#diy
5. Click on Slash Commands
6. In the Choose a Command section type `/spoof` and click Add Slash Command integration
7. Scroll down to Integration Settings
8. In the URL field put the URL you copied earlier + `spoof/`. So in this example it would be `http://desolate-bastion-9841.herokuapp.com/spoof/`
9. Change the method from POST to GET
10. Copy the prepopulated content of the token field
11. Back on Heroku next to the View button, there is a Manage App button. Click on that.
12. Then navigate to the settings tab at the top of the page.
13. Click on Reveal Config Vars and change the content of the **SECRET_VERIFIER** from `0` to the token you copied in step 10
14. Back within the Slack Slash Commands configuration page, you can configure some additional settings. THIS IS OPTIONAL BUT VERY HELPFUL
15. In the Autocomplete Help Text section, check the "Show this command in the autocomplete list checkbox. In the Decription field, put `spoof message of user` and in the Usage Hint field, put `[user] [message]`.
16. Click Save Integraion at the bottom

That's it. You can now write `/spoof [username] [message]` in any channel and pretend to be somebody else!