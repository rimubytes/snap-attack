#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages

VERSION = os.environ.get("SNAPATTACK_VERSION", "0.1")

PACKAGE_INFO = {
    "name": "snapattack",
    "version": 0.1,
    "description": "A lightweight Python-based event collection and publishing system, designed for streamlined data processing. It includes a modular architecture for gathering, processing, and forwarding events, with optional Snap packaging for easy deployment.",
    "author": "Marvin Murithi",
    "license": "MIT",
    "url": "https://snapcraft.io/snapattack",
}