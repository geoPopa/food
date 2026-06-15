#!/usr/bin/env python3
"""
Simple livereload server for the project.

Requires: pip install livereload
Run: python3 serve.py
Open: http://localhost:8000
"""
from livereload import Server
import os

server = Server()

# watch common web file types in the project
for root, dirs, files in os.walk('.'):
    for fname in files:
        if fname.endswith(('.html', '.css', '.js')):
            path = os.path.join(root, fname)
            server.watch(path)

server.serve(root='.', host='0.0.0.0', port=8000, liveport=35729)
