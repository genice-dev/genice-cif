# [{{package}}]({{url}})

{{summary}}

version {{version}}

## Requirements

{% for i in requires %}
* {{i}}
{%- endfor %}

## Installation from PyPI

```shell
% pip install {{package}}
```

## Manual Installation

### System-wide installation

```shell
% make install
```

### Private installation

Copy the files in {{base}}/formats/ into your local formats/ folder.

## Usage

{%- filter indent %}
    {{usage}}
{%- endfilter %}

## Test in place

```shell
% make test
```
