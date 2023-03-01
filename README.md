# Digital Voice Modem Fixed Network Equipment

The DVM FNE provides server-side linking software to connect multiple DVMs together in an integrated network.

This project is a fork of the [dvmfne](https://github.com/DVMProject/dvmfne) project.

## Quick Setup Instructions

> **Warning**: These instructions are outdated.

1. Ensure python3.9, python3.9-venv, python3.9-dev are installed via apt/your favorite package manager.
2. Create the virtualenv and activate it with `python3.9 -m venv . && source bin/activate`
3. Install requirements: `pip install wheel && pip install -r requirements.txt`
4. Set up your config file and rules
5. Run `python fne_router.py` to start up the router.

## License

This project is licensed under the [GNU General Public License Version 2 (GNU GPL v2)](https://www.gnu.org/licenses/gpl-2.0.txt).\
Copyright (c) 2023 K4YT3X and contributors.
