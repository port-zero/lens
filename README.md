# lens

`lens` is a command line tool for easy traversal and
pretty printing fo data structures from the terminal.
It is extensible.

Uses the great [Pygments](http://pygments.org/) library.

It should work on both Python 2 and 3, but was developed
with Python 3 in mind.

## Installation

The package is yet registered to PyPI. That means you should
be able to install it with pip. `lens` was already taken, so
we used `lens-cli`.

```
pip install lens-cli
```

## Usage

Calling `lens -h` will print this message:

```
usage: lens [-h] [--input INPUT] [--format FORMAT]
            [--no-highlight NO_HIGHLIGHT]
            [key [key ...]]

Extensible data structure traversal from the command line

positional arguments:
  key                   the keys to traverse

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        the input file (defaults to the standard input)
  --format FORMAT, -f FORMAT
                        the data format to consume (defaults to json)
  --no-highlight NO_HIGHLIGHT, -n NO_HIGHLIGHT
                        prevent syntax highlighting
```

This should be relatively straightforward. Let's go through a few examples:

```bash
# just calling lens will print everything, syntax-highlighted
$ curl -s https://httpbin.org/get | lens
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3", 
    "Dnt": "1", 
    "Host": "httpbin.org", 
    "Referer": "https://httpbin.org/", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0"
  }, 
  "origin": "213.61.134.12", 
  "url": "https://httpbin.org/get"
}

# suppose we only want to see the "Host" header
$ curl -s https://httpbin.org/get | lens header Host
"httpbin.org"

# or use xml
$ curl -s https://httpbin.org/xml | lens -f=xml
<slideshow 
    title="Sample Slide Show"
    date="Date of publication"
    author="Yours Truly"
    >
    <slide type="all">
      <title>Wake up to WonderWidgets!</title>
    </slide>
    <slide type="all">
        <title>Overview</title>
        <item>Why <em>WonderWidgets</em> are great</item>
        <item/>
        <item>Who <em>buys</em> WonderWidgets</item>
    </slide>
</slideshow>

# suppose we want to only get the title of the second slide
$ curl -s https://httpbin.org/xml | lens -f=xml slide 1 title
<title>Overview</title>
```

We can also read from files by providing an `-i` option.
lens also discovers if its output is redirected to a file, in which case
no syntax highlighting will be applied (the same can be achieved through
the `--no-highlighting/-n` option).

## Extending

You can write your own parsers/traversers - admittedly, parsers
is not a great name, but for now we stick with it.

They should inherit from `LensParser` in `lens.parsers.base`,
and at least implement the method `treat(self, inpt, keys)`,
where `inpt` is the input string and `keys` are the keys to
traverse. It should return the traversed data structure as a
string.

Optionally, the parser can specify a Pygments lexer by exposing
the static attribute `lexer`, if highlighting is applicable. It
will work without one, though.

The plugins can be third party `pip` modules, in which case they
should follow the naming scheme `lens-{format-name}` and export
the parser under the name `Parser`.

An example of a plugin can be found in the
[bson](https://github.com/port-zero/lens_bson) parser repository.

That is all you need to know!

<hr/>

Have fun!
