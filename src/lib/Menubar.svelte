<script lang="ts">
  import { type Menu } from "./Menubar/types.js";
  let menus: Menu[] = [];
  export { menus };
</script>

<div class="menu-bar">
  {#each menus as { name }}
    <button
      on:click={() => {
        console.log("hello");
      }}
      class="menu-btn">{name}</button
    >
  {/each}
</div>

<style>
  .menu-bar {
    height: 24px;
  }
  .menu-btn {
    display: inline-block;
    padding: 2px 4px;
  }
</style>
