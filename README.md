# dc-flutter-bot
An automation tool, bot, that can display latest stable version of Flutter and Dart SDK on Discord.
# Purpose
There is a massive amount of computer engineering students taking a mobile programming course in which Flutter framework is used. 
It is a very big deal in Flutter to stay updated. Therefore, the students must update their installed version of Flutter and Dart SDK. 
However, there are some issues:
- It is boring to check latest SDK versions on Android Studio.
- You can check it on local terminal but it will not show all sorts of information like platforms.
- Sometimes Android Studio will not tell you whether something needs to be updated.

Luckily, they managed to stay online with a Discord Server so that a student can easily check the latest updates of Flutter and Dart SDKs  with a single line of command `!flutter`

- To sum up, this project addresses the sophisticated process of displaying Flutter and Dart SDK versions by Python automation.

![](https://github.com/Quelich/dc-flutter-bot/blob/main/images/commands-1.png?raw=true)
# Software Components

## Data
- Python web scraping utilities are used in this project to fetch data.
- Resources: [Flutter SDK](https://docs.flutter.dev/development/tools/sdk/releases), [Dart SDK](https://dart.dev/get-dart/archive)
## Deployment
- Python app is running on [Heroku](https://dashboard.heroku.com/apps)
# What I learned
  - Scrape data from the internet by Python.
  - Fetch data from dynamic web sites, by using Python's Selenium, Chrome Driver Manager modules
- Connect Discord API to create Discord automation bots
- Deploy a Python bot on Heroku and configure server for CI/CD
