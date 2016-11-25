# lens

`lens` is a command line tool for easy traversal and
pretty printing fo data structures from the terminal.
Uses the great [Pygments](http://pygments.org/) library.

It should work on both Python 2 and 3, but was developed
with Python 3 in mind.

## Installation

The package is not yet registered to PyPI. As soon as it is, you will
be able to install it with pip.

```
pip install lens
```

In the meantime, you can install it like so:

```
git clone https://github.com/port-zero/lens
cd lens
python setup.py install
```

## Usage

Calling `lens -h` will print this message:

```
usage: lens [-h] [--input INPUT] [--format FORMAT] [key [key ...]]

Extensible data structure traversal from the command line

positional arguments:
  key                   the keys to traverse

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        the input file (defaults to the standard input)
  --format FORMAT, -f FORMAT
                        the data format to consume (defaults to json)
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
$ curl -s https://httpbin.org/xml | lens -f=xml 1 title
<title>Overview</title>
```

We can also read from files by providing an `-i` option.

## Extending

Coming soon.

<hr/>

Have fun!
