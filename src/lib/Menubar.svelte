<script lang="ts">
  import { type Menu } from "./Menubar/types.js";
  let menus: Menu[] = [];
  export { menus };
</script>

<menu>
  {#each menus as {name, children}}
    <li>
      <button
        on:click={() => {
          console.log("hello");
        }}>{name}</button
      >
      <menu class="submenu">
        {#each children as submenu}
          <li>{submenu.name}</li>
        {/each}
      </menu>
    </li>
  {/each}
</menu>

<style>
  menu {
    height: 24px;
    padding: 0px;
  }
  li {
    display: inline-block;
    list-style-type: none;
    padding: 2px 4px;
  }
  .submenu {
    visibility: visible;
    position: relative;
  }
</style>
