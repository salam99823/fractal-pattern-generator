<script lang="ts">
  import { type Menu } from "./Menubar/types.js";
  let classes = "";
  let id = "";
  let menus: Menu[] = [];
  export { menus, classes as class, id };
</script>

<menu>
  {#each menus as menu}
    <li>{menu.name}</li>
  {/each}
</menu>

<style>
  menu {
    padding: 0px;
  }
  li {
    list-style: none;
  }
</style>
