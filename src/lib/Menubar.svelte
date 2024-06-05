<script lang="ts">
  import { Menu } from "./Menubar/menu.ts";
  let classes = "";
  let id = "";
  let menus: Menu[] = [];
  export { menus, classes as class, id }
</script>

<menu>
  {#each menus as menu}
    
  {/each}
</menu>

<style>
</style>
