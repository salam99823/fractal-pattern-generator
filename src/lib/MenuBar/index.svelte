<script lang="ts">
  import MenuBarButton from "./MenuBarButton.svelte";
</script>

<div class="menubar">
  <MenuBarButton text="Файл" actions={["1", "2"]}/>
  <MenuBarButton text="Настройки" actions={["1", "2"]}/>
  <MenuBarButton text="Вид" actions={["1", "2"]}/>
  <MenuBarButton text="Справка" actions={["1", "2"]}/>
</div>

<style>
  .menubar {
    display: flex;
    flex-direction: row;
    justify-content: flex-start space-around;
    align-items: center;
    width: 100%;
    margin: 0;
    padding: 0;
    background-color: #ffffff;
  }

  @media (prefers-color-scheme: dark) {
    .menubar {
      background-color: #0f0f0f98;
      color: #ffffff;
    }
  }
</style>
