<script lang="ts">
  import ThemeController from "$components/ThemeController.svelte";

  let title = "SvelteKit App";
</script>

<nav class="navbar bg-base-100 px-4">
  <div>
    <a class="btn btn-ghost text-xl mr-16" href="/">{title}</a>
  </div>
  <div>
    <a class="btn btn-ghost" href="/">Page 1</a>
  </div>
  <div>
    <a class="btn btn-ghost" href="/">Page 2</a>
  </div>
  <div class="flex-1" />
  <div class="flex-none mx-3">
    <ThemeController />
  </div>
  <div class="flex-none mx-3">
    <div class="avatar placeholder">
      <div class="bg-neutral text-neutral-content rounded-full w-10">
        <span>JL</span>
      </div>
    </div>
  </div>
</nav>
