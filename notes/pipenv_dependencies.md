# `pipenv` Dependencies

## `Pipfile`

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"
python-dotenv = "*"
docutils = "*"
pytest = "*"
flake8 = "*"
isort = "*"

[dev-packages]

[requires]
python_version = "3.13"
```
