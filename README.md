# OrpheusSay

Command-line tool similar to cowsay, but featuring Hack Club's mascot
Orpheus :3

## Installation

``` bash
pip install orpheussay
```

## Usage

``` bash
# Basic usage
orpheussay "Hello, world!"

# Pipe text to orpheussay
echo "Hello from the command line!" | orpheussay

# Custom width
orpheussay -w 30 "This is a longer message that will wrap at 30 characters"
```

## Example

``` bash
$ orpheussay "bla bla bla bla bla"
 __________________
< bla bla bla bla bla >
 ------------------
          \
           \
            \  __
              / _)
     _.----._/ /
    /         /
 __/ (| | (  |
/__.-'|_|--|_|
```

## Development

To contribute or modify:

``` bash
git clone https://github.com/nullsec0x/orpheussay.git
cd orpheussay
pip install -e .
```
