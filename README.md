# Two Factor Authentication CLI

> 2FA in your computer

## HOWTO

Just install the tool with `pip` and then use the shortcut `2fa`.

```bash
$ pip install twofactorauthcli
$ 2fa
```

In the use, the tool will show you where to config it.

## TODO

**This is a MVP**, usable but limited. There are some ideas to implement:

- The tests are stupid, rethink them.
- Explain how to get the codes.
- Improve configuration, making the path configurable or even better making it editable trought the CLI.
- Show how many time left for the next codes change.
- Get a code fast and copied to clipboard, something like `2fa copy aws`.
