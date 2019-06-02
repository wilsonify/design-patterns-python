
![](static/badges/bugs.svg)
![](static/badges/code_smells.svg)
![](static/badges/coverage.svg)
![](static/badges/duplicated_lines_density.svg)
![](static/badges/ncloc.svg)
![](static/badges/reliability_rating.svg)
![](static/badges/security_rating.svg)
![](static/badges/sqale_index.svg)
![](static/badges/sqale_rating.svg)
![](static/badges/vulnerabilities.svg)

# Design Patterns in python

based on https://www.lynda.com/Python-tutorials/Design-Patterns-Python

# lint
```bash
python -m pylint
```

# test
```bash
python -m pytest
```

# coverage

```bash
python -m pytest --cov=dpatterns_python --cov-report xml:coverage-reports/coverage-dpatterns_python.xml
```


# scan

```bash
sonar-scanner \
  -Dsonar.projectKey=design_patterns_python \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://10.152.183.181:9000 \
  -Dsonar.login=de95748e5013d29185ac125fabeaff012ffa724a
```
