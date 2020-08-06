#!/bin/bash

mkdir ../saves/$2
cp ../scenarios/$1/* ../saves/$2/
mkdir ../saves/$2/wallets
cp -r ../wallets/* ../saves/$2/wallets/
cp ../plottingTools/* ../saves/$2/