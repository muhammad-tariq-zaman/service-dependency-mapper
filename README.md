# service-dependency-mapper

Work out a safe start order for services from a JSON dependency map, and report dependency cycles instead of looping.

## How to run

```sh
python3 main.py services.json
```

## Example output

```
Start order (dependencies first):
1. db
2. web
```

Standard library only. Run the tests with `python3 -m unittest discover`.
