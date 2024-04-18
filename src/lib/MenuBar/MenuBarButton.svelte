<script lang="ts">
  export let text: string = "";
  export let actions: string[] = [];
  let actionsopen: boolean = false;
  function openactions() {
    actionsopen = !actionsopen;
  }
</script>

<div class="menubar-btn-block">
  <button type="button" class="menubar-btn" on:click={openactions}
    >{text}</button
  >
  <menu class="actions" class:show={actionsopen}>
    {#each actions as action}
      <li><button type="button" class="menubar-btn">{action}</button></li>
    {/each}
  </menu>
</div>

<style>
  .menubar-btn {
    padding: 4px;
    border-radius: 0;
    font-size: small;
  }
  .actions {
    display: none;
    padding: 0;
    flex-direction: column;
    justify-content: space-around;
  }
  .actions *.menubar-btn {
    display: flex;
    position: static;
  }
  .show {
    display: contents;
  }
  .menubar-btn-block {
    overflow: visible;
    display: block;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
</style>
