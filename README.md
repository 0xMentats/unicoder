# Unicoder

This script generates random sentences in UTF-8 format based on a given input string. Additionally, it can retrieve a complete list of equivalent UTF-8 characters for a specific one.

<br>

## Install

```bash
git clone https://github.com/imMentats/unicoder
cd unicoder
pip3 install -r requirements.txt
```

<br>

## Options

| Option          | Description                                       |
|------------------|---------------------------------------------------|
| `--all`          | Get all UTF-8 characters for the given character. |
| `-u, --url`      | Output UTF-8 characters as URL-encoded strings.   |
| `-i, --inline`   | Output characters in a single line.               |


<br>

## Examples

Convert a sentence to random UTF-8 characters:

```bash
python unicoder.py "'or 1=1-- -"

# ＇ō𝙧 𝟭⩶①－﹣ －
```

Get all UTF-8 characters for a specific character:

```bash
python unicoder.py "<" --all

# ≮
# ﹤
# ＜
# ≮
```

Get all UTF-8 characters for a specific character, inline:

```bash
python unicoder.py "<" --all -i

# ≮﹤＜
```

Get all UTF-8 characters for a specific character, including the URL-encoded representation:

```bash
python unicoder.py "<" --all -u

# %E2%89%AE
# ﹤
# %EF%B9%A4
# ＜
# %EF%BC%9C
```

Get all UTF-8 characters for a specific character, including the URL-encoded representation inline:

```bash
python unicoder.py "<" --all -u -i

# ≮: %E2%89%AE
# ﹤: %EF%B9%A4
# ＜: %EF%BC%9C
```


<br>

## Notes

The script uses a predefined set of UTF-8 characters stored in `utf8.json`. This JSON file has been scraped using the `scrape.py` script from [compart.com](https://www.compart.com). Full credits to their website for the dataset.