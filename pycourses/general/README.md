# General

This file lists good practise and tips on how to sucseful create and mantain a python project/package.

**Disclaimer**
Not a complete list. Growth with experience and time to exctually write it down here.


---

## Coding principles

### SOLID

Stands for:

- **S**ingle resonsibility
- **O**pen/closed
- **L**liskov substitution
- **I**interface sgregation
- **D**ependency inversion

**Links**:

- AjranCodes (Youtube video. Explained with code): https://www.youtube.com/watch?v=pTB30aXS77U

---

## Testing

- pytest
  - **code testing**
- pylint
  - **static code analyser**
  - https://pypi.org/project/pylint/
  - identifies bad coding practise (duplicate code, cyclic import, naming, ...)
  - to create a config file to define code style: pylint --genate-rcfile > .pylintrc