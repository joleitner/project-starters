# SvelteKit Template with DaisyUI & Tailwind CSS

Dockerized SvelteKit template with DaisyUI & Tailwind CSS.

> Further information about frameworks and libraries used:
>
> - [SvelteKit](https://kit.svelte.dev/)
> - [DaisyUI](https://daisyui.com/)
> - [tailwindcss](https://tailwindcss.com/).

## Usage

You have to options to use this template:

1. Just copy and adapt the files you need. (**Recommended**)
2. Use this README as a guide to create your own template.

### Copy & Adapt

I recommend to use the vscode [devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension to open the project in a container.

If you copy the `sveltekit` folder and you open it with vscode the devcontainer extension will ask you if you want to open it in a container. If you choose yes, the container will be build and you can directly start developing. Have fun!

## Getting Started

### Setup devcontainer

I suggest to use the [devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension as it will improve your development experience.
In case you haven't already, install the devcontainer extension inside vscode.
Afterwards just copy over the `.devcontainer` folder with the preconfigured `devcontainer.json` file into your project.

### Install SveteKit in a Docker Container

First create `Dockerfile` and `docker-compose.yml` files:

The `Dockerfile` should be created inside an `app` directory:

```Dockerfile
# check newest node version: https://hub.docker.com/_/node
FROM node:21-alpine

WORKDIR /app

USER node
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
      # - /app/node_modules # exclude node_modules
    ports:
      - "5173:5173"
    command: npm run dev
```

Now we can initialize the SvelteKit project inside inside the container and install the dependencies:

```bash
docker compose run app npm create svelte@latest
docker compose run app npm install
```

Follow the instructions and choose the options fitting your needs.

After the project was initialized we now need to add some missing lines to the `Dockerfile` so that it can start the dev server:

```Dockerfile
# check newest node version: https://hub.docker.com/_/node
FROM node:21-alpine

WORKDIR /app

# install dependencies
COPY package*.json ./
RUN npm install

# copy source code
COPY . .

RUN chown -R node:node /app
USER node

# start dev server
CMD [ "npm", "run", "dev"]
```

Because SvelteKit is running in the Docker container, we have to make a little change to the npm run scripts in `package.json`:

```json
"scripts": {
    "dev": "vite dev --host",
    ...
}
```

Now our preconfiguration for the container is made. We can now start and open the container directly with vscode devcontainer. This builds the container and you should be able to see the SvelteKit welcome page on `localhost:5173`.

All the following steps are done inside the Docker container, opened ideally with the devcontainer extension.

### Install Tailwind CSS & DaisyUI

To add Tailwind CSS we have to install some dependencies and initialize it:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

After that we can install DaisyUI:

```bash
npm install -D daisyui@latest
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

In case you want to use DaisyUI themes you have to add the following lines to `tailwind.config.js`:

```js
  daisyui: {
    themes: ["light", "dark"],
  },
```

### Additional Libraries

#### Iconify

A very useful library for SvelteKit is [Iconfiy](https://iconify.design/docs/icon-components/svelte/). It lets you use icons with ease. To install it run:

```bash
npm install -D @iconify/svelte
```

To use it, search Icon [here](https://icon-sets.iconify.design/) and import it in your component:

```html
<script lang="ts">
  import Icon from "@iconify/svelte";
</script>

<Icon icon="mdi:home" />
```

#### theme-change

A very handy library for changing your themes is [theme-change](https://github.com/saadeghi/theme-change). To install it run:

```bash
npm install theme-change
```

Inside the [ThemeController](./app/src/components/ThemeController.svelte) component you can see an example on how to use it.

#### svelte-time

When working with time [svelte-time](https://www.npmjs.com/package/svelte-time) is handy.

```bash
npm install -D svelte-time
```

To use it, import it in your component:

```html
<script lang="ts">
  import { Time } from "svelte-time";
</script>

<time timestamp="2024-01-01" />
```

### Component folder

Depending on your preference you can create a `components` folder in `src` and add an alias to `svelte.config.js`:

```js
const config = {
  // ...
  kit: {
    // ...
    alias: {
      $components: "./src/components",
    },
  },
};
```

Afterwards you can import your own components like this:

```html
<script lang="ts">
  import Button from "$components/Button.svelte";
</script>
```

## Development

To start the development server run:

```bash
docker compose up
```
