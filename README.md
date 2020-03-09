# Universal CI notification

## Messenger
### Slack
Used methods:
1. https://api.slack.com/methods/chat.postMessage
1. https://api.slack.com/methods/users.list

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
