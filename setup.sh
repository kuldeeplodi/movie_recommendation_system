#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Download model/data files from GitHub Releases
echo "Downloading movie_dict.pkl and similarity.pkl..."

wget -O movie_dict.pkl https://github.com/kuldeeplodi/movie_recommendation_system/releases/download/movie/movie_dict.pkl
wget -O similarity.pkl https://github.com/kuldeeplodi/movie_recommendation_system/releases/download/movie/similarity.pkl
echo "Download complete."
