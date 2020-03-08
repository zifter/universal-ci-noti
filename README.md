# Universal CI notification

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

### Teamcity TODO
