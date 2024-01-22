# SvelteKit Template with DaisyUI & Tailwind CSS

Dockerized SvelteKit template with DaisyUI & Tailwind CSS.

> Further information about frameworks and libraries used:
>
> - [SvelteKit](https://kit.svelte.dev/)
> - [DaisyUI](https://daisyui.com/)
> - [tailwindcss](https://tailwindcss.com/).

## Usage

You have to options to use this template:

1. Just copy and adapt the files you need.
2. Use this README as a guide to create your own template.

## Getting Started

### Install SveteKit in a Docker Container

First create `Dockerfile` and `docker-compose.yml` files:

The `Dockerfile` should be created inside an `app` directory:

```Dockerfile
# check newest node version: https://hub.docker.com/_/node
FROM node:21-alpine

WORKDIR /app

# install dependencies
COPY package*.json ./
RUN npm install
# copy source code
COPY . .

# start dev server
CMD [ "npm", "run", "dev"]
```

The `docker-compose.yml`:

```yaml
version: "3.8"

services:
  app:
    build:
      context: ./app
    volumes:
      - ./app:/app
    ports:
      - "5173:5173"
    command: npm run dev
```

Now to install SvelteKit in a Docker container run:

```bash
docker compose run app npm init svelte@next
```

Follow the instructions and choose the options fitting your needs.

Now you can install the dependencies:

```bash
docker compose run app npm install
```

Because we created all files as root user inside the container and mapped the files to our development directory, we have to change the owner of the files:

```bash
sudo chown -R $USER:$USER app/
```

Because SvelteKit is running in the Docker container, we have to make a little change to the npm run scripts in `package.json`:

```json
"scripts": {
    "dev": "vite dev --host",
    ...
}
```

### Install Tailwind CSS & DaisyUI

To add Tailwind CSS we have to install some dependencies and initialize it:

```bash
docker compose run --rm app npm install -D tailwindcss postcss autoprefixer
docker compose run --rm app npx tailwindcss init -p
```

After that we can install DaisyUI:

```bash
docker compose run app npm install -D daisyui@latest
```

We have to adjust to parameters in `tailwind.config.js`. With content we add the paths to all files we want to use Tailwind CSS in and as plugins we add DaisyUI:

```js
export default {
  content: ["./src/**/*.{svelte,html,js,ts}"],
  plugins: [require("daisyui")],
};
```

Create a `app.css` file in `src` and add the following content:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

And to import we create a global `+layout.svelte` file in `src/routes`:

```html
<script>
  import "../app.css";
</script>

<slot />
```

Additionally add initial-scale to the meta tag in `src/app.html`:

```html
<meta name="viewport" content="width=device-width", initial-scale=1" />
```

### Additional Libraries

A very useful library for SvelteKit is [Iconfiy](https://iconify.design/docs/icon-components/svelte/). It lets you use icons with ease. To install it run:

```bash
docker compose run app npm install -D @iconify/svelte
```

To use it, search Icon [here](https://icon-sets.iconify.design/) and import it in your component:

```html
<script lang="ts">
  import Icon from "@iconify/svelte";
</script>

<Icon icon="mdi:home" />
```

When working with time [svelte-time](https://www.npmjs.com/package/svelte-time) is handy.

```bash
docker compose run app npm install -D svelte-time
```

To use it, import it in your component:

```html
<script lang="ts">
  import { Time } from "svelte-time";
</script>

<time timestamp="2024-01-01" />
```

## Development

To start the development server run:

```bash
docker compose up
```

## TODOs & Ideas

- [ ] Fix the file creation as root user
- [ ] Add theme change
- [ ] Think about using pnpm
- [ ] Prepare for production
