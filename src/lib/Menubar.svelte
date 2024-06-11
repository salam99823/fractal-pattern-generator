<script lang="ts">
  import { type Menu } from "./Menubar/menu.js";
  let classes = "";
  let id = "";
  let menus: Menu[] = [];
  export { menus, classes as class, id }
</script>

<menu>
  {#each menus as menu}
    <li>{menu}</li>
  {/each}
</menu>

<style>
</style>
