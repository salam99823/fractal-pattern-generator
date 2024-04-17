<script lang="ts">
  function hello() {
    document.getElementsByClassName("hello")[0].innerHTML =
      "<p>Hello World!</p>";
  }
</script>

<div class="menubar">
  <button class="menubar-button">Файл</button>
  <button class="menubar-button">Вид</button>
  <button class="menubar-button" on:click={hello}>Справка</button>
  <p class="hello"></p>
</div>

<style>
  .menubar {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    margin: 0;
    padding: 0;
  }

  .menubar-button {
    display: flex;
    padding: 4px;
    border-radius: 0;
    font-size: small;
  }
</style>
