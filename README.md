# youtube_me

A thin wrapper around the fantastic [youtube-dl](https://github.com/rg3/youtube-dl) that downloads videos from a list of supported URLs within a timeframe.

## Why?

* Bad reception means streaming doesn't work well.
* Timing allows for downloading in ISP's off-peak data time.

## Install

The Easy Way:

```
pip install youtube_me
```

The Harder Way:

```
git clone https://github.com/shakna-israel/youtube_me
cd youtube_me
python setup.py install
```

## Usage

```
youtube_me --start-time 0 --end-time 9
```

The start and end time are 24 hour notation, so for 1:00PM you would enter 13.

You can also see the short flags with ```python youtube_me.py -h```.

## Disclaimer

This may not be legal in your area, please consult Google's Terms and Conditions for your area, *carefully*.
