<script lang="ts">
  import { onMount } from "svelte";
  import Icon from "@iconify/svelte";
  import { themeChange } from "theme-change";

  onMount(() => {
    themeChange(false);
  });
</script>

<label class="swap swap-rotate">
  <!-- this hidden checkbox controls the state -->
  <input
    type="checkbox"
    class="theme-controller"
    data-toggle-theme="dark,light"
  />
  <Icon class="swap-on fill-current w-6 h-auto" icon="ph:sun-bold" />
  <Icon class="swap-off fill-current w-6 h-auto" icon="ph:moon-bold" />
</label>
