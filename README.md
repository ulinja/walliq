# WallIQ

WallIQ is a smart tool for managing your wallpaper collection.

### Usage

Currently it's just a handy CLI tool.
To use it, invoke it like so:

```bash
./walliq-cli ~/pictures/wallpapers/some-cool-image.png
```

which will output some data about your wallpaper:

```
---------------------  ---------  -------  -------  -------  -------  -------
Resolution             1920x1080
Aspect Ratio           16:9
Aspect Ratio Is Exact  Yes
Colors                 #021322    #96446E  #B04D6B  #E9705A  #C55469  #DA6460
---------------------  ---------  -------  -------  -------  -------  -------
```

## Installation

### Nix / NixOS

Clone the repo, activate `shell.nix` and go.

### Other

Dependencies:

- `Python >= 3.9` (tested on `3.12.9`) with the following libraries:
    - `pillow`
    - `pywal`
    - `tabulate`
- `imagemagick`

## Roadmap

The goal of WallIQ is to be a comprehensive wallpaper manager you can use to
organize, classify and even upscale and intelligently resize your wallpapers
to your target resolution and aspect ratio.

You'll load your wallpaper images into WallIQ, which will then scan, tag,
keep track of and organize your files.

- [x] resolution detection
- [x] aspect ratio detection
- [x] colour scheme detection
- [ ] image file collection organization
- [ ] manual image tagging
- [ ] resolution upscaling
- [ ] canvas outpainting
- [ ] automated image tagging (ML)
