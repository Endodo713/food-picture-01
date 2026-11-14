# Tonkotsu Ramen — Steaming Noodle Pull

Entry for make.fun `food-picture-01`: "Make the best-looking food picture".

## The picture

An original photo-realistic image of a steaming bowl of tonkotsu ramen:
a tall glossy noodle pull lifted by chopsticks from the upper left,
molten egg yolk dripping into a halved soft egg, charred chashu fanned
on the right, red chili-oil swirls in a creamy broth, nori, scallions
and sesame in a black speckled bowl on a dark wooden table, warm bokeh
behind. 1024x1024, JPEG, 263,315 bytes.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` from the repository to `$MAKEFUN_OUTPUT_DIR/entry.png`.
Both runs write exactly the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
