SNAP_NAME := snapattack
VERSION := $(shell yq ".version" snap/snapcraft.yaml)
ARCH := amd64
SNAP_FILE := $(SNAP_NAME)_$(VERSION)_$(ARCH).snap

.PHONY: all build clean install uninstall

