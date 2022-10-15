---
layout: post
title: CSS Portal
subtitle: CSSPortal - Fun with CSS! ⚡
cover-img: /assets/img/webdev.jpg
thumbnail-img: /assets/img/artesdosullogo.png
share-img: /assets/img/artesdosullogo.png
tags: [development, resources, awesome]
---     

[One-Line Web Server 🖥️](https://notes.aliciasykes.com/32456/one-line-web-server)
==================================================================================

The following commands will each start a simple web server, serving up the files in the current directory.  
Just open up the browser, and navigate to the system's IP + port (e.g. `http://localhost:8080`).

### Python

    python -m http.server 8000
    

* * *

### Node.js

    npx http-server ./ --port 8080
    

* * *

### PHP

    php -S 127.0.0.1:8080
    

* * *

### Ruby

    ruby -run -e httpd ./ -p 8080
    

* * *

### R

    Rscript -e 'servr::httd()' -p8080
    

* * *

### Caddy

[Caddy](https://caddyserver.com/) is a feature-rich production-ready Go-based web server, with easy configuration. Just download and use something like the following command.

    caddy file-server
    

* * *

### Rust (with [miniserve](https://github.com/svenstaro/miniserve))

    cargo install miniserve
    miniserve -p 8080 .
    

* * *

### BusyBox

    busybox httpd -f -p 8080
    

* * *

## You can also share the server with someone remotely, Using Ngrok to expose server to the internet

This is really useful for so many use cases, for example temporarily sharing locally running services your building with colleges

1.  Download Ngrok for your platform, from [ngrok.com/download](https://ngrok.com/download)
2.  Unzip the archive, and navigate to it's path or add an alias pointing to it
3.  Simply run `./ngrok http [port num]`, so if your local app is running on port 300, that would be `./ngrok http 3000`
4.  The command line will show a public ngrok domain, which is accessible to anyone through the internet

You may need to log in, to do so, create an account on ngrok, go to dashboard --> autotoken and copy your token.  
Then run `./ngrok authtoken [your-token]`


