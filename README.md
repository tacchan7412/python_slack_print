# python_slack_print

## About

python_slack_print is a simple printer for both stdout and slack channel

## Examples

```python
from slack_print import SlackPrint

sp = SlackPrint('<your-slack-access-token>', '#general')

# Print
sp.print('hello world')

# Upload a file
sp.upload('hello.txt')
```

## Installation

```
$ pip install python_slack_print
```

## Tip

### Replace your print() with sp.print()

You can replace your print() with sp.print() with UNIX command.
Below is one of the simplest ways. (There must be a better way.)
 
```
sed -i -e "s/print(/sp.print(/g" <file-to-be-replaced>
```
