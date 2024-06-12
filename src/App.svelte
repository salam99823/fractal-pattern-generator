<script lang="ts">
  import { type Menu } from "./lib/Menubar/types.js";
  import Menubar from "./lib/Menubar.svelte";
  import Canvas from "./lib/Canvas.svelte";
  let menus: Menu[] = [
    {
      name: "1",
      children: [],
    },
  ];
</script>

<main>
  <Menubar {menus} />
  <Canvas />
  pass
</main>

<style>
</style>
