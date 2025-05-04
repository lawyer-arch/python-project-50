### Hexlet tests and linter status:
[![Actions Status](https://github.com/lawyer-arch/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lawyer-arch/python-project-50/actions)


### SonarQube code scanning:
[![SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=lawyer-arch_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lawyer-arch_python-project-50)


# Project "Difference Calculator".

As a result of the project implementation, we receive a utility ***Gendiff***.

**Gendiff** - is a console utility and library for comparing two configuration files (JSON or YAML). Highlights the differences between them in convenient formats: `stylish`, `plain`, `json`.

The project implements the following features:  
 1. Output of data differences between the data of two files.
 2. Output data in flat format.
 3. Data output in json format.
 4. Ability to compare flat files (yaml).
 5. Possibility of recursive comparison.

Supported input file formats `JSON`, `YAML (.yml, .yaml)`.

## Installation

Make sure you have Python 3.10+ installed.
```
git clone https://github.com/pavel-lexrus/python-project-50.git
cd python-project-50
make install или uv pip install -e .
```

If necessary, install pytest, ruff.

```
uv pip install pytest
uv pip install ruff
```

## Usage

```
gendiff file1.json file2.json
```

Default output example (stylish format):

```
{
  common: {
    + follow: false
      setting1: Value 1
    - setting2: 200
    - setting3: true
    + setting3: [complex value]
    ...
  }
}
```

CLI options:

```
gendiff [OPTIONS] FILE1 FILE2

Опции:
  -f, --format [stylish|plain|json]   Формат вывода(по молчанию: stylish)
  -h, --help                          Показать справку и выйти
```

Output examples:

```
plain:
gendiff file1.yaml file2.yaml --format plain

text:
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
Property 'group1.baz' was updated. From 'bas' to 'bars'

json:

gendiff file1.yaml file2.yaml --format json
```

Example of use as a library:

```
from gendiff import generate_diff

diff = generate_diff('file1.yaml', 'file2.yaml', format='plain')
print(diff)
```

### VIDEO File asciinema

[video gendiff_file.cast](https://asciinema.org/a/G64TG227y5p5eX35GprmYoE44)

[video gendiff_yaml.cast](https://asciinema.org/a/37nwSIIExOWAmqpjirMloi6bw)

[video test_json_recursion.cast](https://asciinema.org/a/Zd5PvHZOn8ObyNgXsqTSOp1l2)

[video test_plain.cast](https://asciinema.org/a/QjwnynfbiOdNO4FDBeIaNkr2o)

[video test_json.cast](https://asciinema.org/a/V2aX9qJ9lMMvGshdU3gy5FZ9K)
