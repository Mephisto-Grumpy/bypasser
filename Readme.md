# Bypass Website 🕸️

This is a simple Python-based project to bypass URL restrictions of certain websites using the `api.bypass.vip` service.

## Features

- **URL history**: Once a URL has been entered, it will be remembered for future autocompletion.
- **Auto-suggestion**: When typing a URL, any previous URLs that match the input will be suggested.

## Requirements

This project requires the following Python packages

- `requests` module
- `gratient` module
- `colorama` module
- `prompt_toolkit` module
- `cachetools` module

## Setup

To setup the project, run the following command in the project directory

```bash
pip install -r requirements.txt
```

## Usage

To use the project, run the following command in the project directory

```bash
python main.py
```

After running the script, you will see a prompt. There are four possible choices:

1. Enter a single URL: You will be asked to enter a URL which will then be bypassed.
2. Enter multiple URLs from a file: You will be asked to enter a file path. The file should contain one URL per line. All URLs will be bypassed.
3. View supported websites: Shows a list of websites that this script supports bypassing.
4. Exit: Exit the program.

## Supported Websites

### Ad links:

- linkvertise.com (all of their domains)
- adf.ly (all of their domains)
- exe.io/exey.io/exee.io/exe.app/eio.io
- ouo.io/ouo.press
- adfoc.us
- ay.live
- bc.vc/bcvc.live
- fc.lc/fc-lc.com
- za.gl/za.uy/zee.gl
- freehottip.com
- ph.apps2app.com
- gestyy.com
- shortconnect.com
- shorte.st/sh.st
- aylink.co

### Socials:

- sub2get.com
- sub2unlock.net/sub2unlock.com
- rekonise.com
- letsboost.net
- mboost.me
- sub4unlock.com
- ytsubme.com
- steps2unlock.com
- social-unlock.com
- boost.ink
- boostme.link/boost.fusedgt.com

### Shorteners:

- bit.ly/bitly.com
- cutt.ly
- shrto.ml
- goo.gl
- t.co
- tinyurl.com
- onlyme.ga

### Redirects:

- youtube.com
- justpaste.it
