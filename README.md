# hyp

Minimal directory structure setup utility for [hy](hylang.org/).

Because manually setting up the same boilerplate file and directory structure
makes me feel the kind of tiredness sleep won't fix.

## Install

```sh
$ pip install . --use-feature=in-tree-build
```

## Usage

```sh
usage: hyp [-h] [--lang {hy,py}] [--lic {MIT,BSD2,BSD3,GPL2,GPL3,Apache}] {new,interactive} project
```

**NOTE:** `interactive` is not yet implemented.

```sh
$ hyp new foobar            # setup new hy project named 'foobar'
$ hyp --lang py new boofar  # setup new python project named 'boofar'
```
