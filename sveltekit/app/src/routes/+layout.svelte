<script lang="ts">
  import "../app.css";
  import Navbar from "$components/Navbar.svelte";
</script>

<Navbar />

<main class="container max-w-5xl mx-auto mt-8 mb-20 px-3">
  <slot />
</main>
