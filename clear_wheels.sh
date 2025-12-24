#!/usr/bin/env bash

rm -rf build/*
rmdir build

rm -rf dist/*
rmdir dist

rm -rf metaerrors.egg-info/*
rmdir metaerrors.egg-info

echo "Cleaning success!"