<script lang="ts">
  import {} from "pug"
</script>

<div class="menubar">
  <div class="menubar-conteiner">Файл</div>
  <div class="menubar-conteiner">Вид</div>
  <div class="menubar-conteiner">Справка</div>
</div>

<style>
  .menubar {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
  }

  .menubar-conteiner {
    display: flex;
    padding: 3px;
    border-radius: 0%;
    cursor: default;
    font-size: small;
  }
</style>
