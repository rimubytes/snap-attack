SNAP_NAME := snapattack
VERSION := $(shell yq ".version" snap/snapcraft.yaml)
ARCH := amd64
SNAP_FILE := $(SNAP_NAME)_$(VERSION)_$(ARCH).snap

.PHONY: all build clean install uninstall

all: build

build:
	@echo "Building $(SNAP_NAME) version $(VERSION)..."
	snapcraft --debug

install: build
	@echo "Installing $(SNAP_FILE)..."
	sudo snap install $(SNAP_FILE) --dangerous

