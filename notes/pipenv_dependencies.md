# `pipenv` Dependencies

## `Pipfile`

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"
docutils = "*"
pytest = "*"
flake8 = "*"
isort = "*"
python-dotenv = "*"
pytest-cov = "*"
pytest-django = "*"

[dev-packages]

[requires]
python_version = "3.13"
```
