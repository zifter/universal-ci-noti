# Universal CI notification

## Messenger
### Slack
Used methods:
1. https://api.slack.com/methods/chat.postMessage
1. https://api.slack.com/methods/users.list

SLACK_API_TOKEN could be found at your app site ``Installed App Settings``` 
```Bot User OAuth Access Token```

Add your bot to channel to receive messages.

For detailed permissions have a look at this methods.
### Telegram TODO

## Consumer
Some logic, what we need to do with notifications.

## Producer
Some CI service which produce notifications.

### Custom REST
Make post request to `HOST:PORT/job-result/`
```json
{
	"status": "success",
	"scm": {
		"name": "universal-ci-noti",
		"url": "https://github.com/zifter/universal-ci-noti",
		"branch": "master",
		"committer": "zifter"
	},
	"url": "https://jenkins.com/TODO"
}
```

### Jenkins TODO
https://plugins.jenkins.io/notification/

### Teamcity TODO


# Links
[![Release](https://img.shields.io/github/release/zifter/universal-ci-noti.svg)][releases-url]
[![Supported versions](https://img.shields.io/pypi/pyversions/universal-ci-noti.svg)][pypi-url]
[![Code Coverage](https://codecov.io/gh/zifter/universal-ci-noti/branch/master/graph/badge.svg)][codecov-url]
[![Build Status Travis CI](https://travis-ci.org/zifter/universal-ci-noti.svg?branch=master)][travis-url]
[![Contact](https://img.shields.io/badge/telegram-write%20me-blue.svg)][telegram-url]

[releases-url]: https://github.com/zifter/universal-ci-noti/releases
[codecov-url]: https://codecov.io/gh/zifter/universal-ci-noti
[travis-url]: https://travis-ci.org/zifter/universal-ci-noti
[telegram-url]: https://t.me/zifter
[pypi-url]: https://pypi.org/project/universal-ci-noti/