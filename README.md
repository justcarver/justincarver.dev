# justincarver.dev

A static page generated from `index.md`. Edit the Markdown to update both the
readable website and its downloadable Markdown version.

## Deploy with Coolify

1. Push these files to a Git repository and connect it to a Coolify application.
2. Select the **Dockerfile** build pack, with base directory `/` and Dockerfile
   location `/Dockerfile`.
3. Set the exposed container port to **80**.
4. Point the domain's DNS `A` record to the Hetzner server's public IPv4 address.
5. Add **https://justincarver.dev** as the application's domain and deploy.
   Coolify's proxy handles HTTPS; ports 80 and 443 must reach that proxy.
6. Optionally enable automatic deployments for pushes to the selected branch.

No environment variables or persistent volumes are required. Coolify interface
labels may differ by version.

The image serves:

- `/`: HTML generated from `index.md`, with navigation and responsive styling.
- `/index.md`: the original Markdown, served as `text/markdown; charset=utf-8`.
- `/style.css`: the stylesheet.

Docker's health check requests `/`. If configuring a Coolify health check too,
use HTTP, port **80**, and path **/**.

## Run locally with Docker

```sh
docker build -t justincarver-site .
docker run --rm -p 127.0.0.1:8080:80 justincarver-site
```

Open <http://localhost:8080> and <http://localhost:8080/index.md>.

## Build without Docker

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build.py
```

Generated files are written to `dist/`. Python and the Markdown dependency are
only needed during the build; the deployed image runs Nginx.

`.dockerignore` permits only the files needed for the build. `Resume/` is
excluded from the build context and ignored by Git; the final image contains
only the generated public files in its web root. The source resume files are
not needed to build or run the site.
