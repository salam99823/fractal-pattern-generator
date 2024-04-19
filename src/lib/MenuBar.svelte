<script lang="ts">
  // noinspection ES6UnusedImports
  import { Menubar } from "bits-ui";

  type Menu = {
    trigger: string;
    contents:
      | (
          | {
              type: "Label" | "Item";
              label: string;
              onClick?: () => void;
              class?: string;
            }
          | SubMenu
          | "Separator"
          | "Arrow"
        )[]
      | string;
    trigger_class?: string;
  };

  type SubMenu = {
    type: "SubMenu";
    trigger: string;
    contents:
      | (
          | {
              type: "Label" | "Item";
              label: string;
              onClick?: () => void;
              class?: string;
            }
          | "Separator"
          | "Arrow"
        )[]
      | string;
    trigger_class?: string;
  };

  let menus: Menu[] = [
    {
      trigger: "Файл",
      contents: [
        {
          type: "Item",
          label: "Новый файл",
          onClick: () => {
            console.log("new file");
          },
        },
        {
          type: "Item",
          label: "Открыть",
          onClick: () => {
            console.log("open");
          },
        },
      ],
      trigger_class: "",
    },
  ];
</script>

<Menubar.Root>
  {#each menus as menu}
    <Menubar.Menu>
      <Menubar.Trigger class="menubar-trigger {menu.trigger_class || ''}">
        {menu.trigger}
      </Menubar.Trigger>
      <Menubar.Content>
        {#if typeof menu.contents === "string"}
          <Menubar.Item>
            {menu.contents}
          </Menubar.Item>
        {:else}
          {#each menu.contents as item}
            {#if item === "Separator"}
              <Menubar.Separator />
            {:else if item === "Arrow"}
              <Menubar.Arrow />
            {:else if item.type === "SubMenu"}
              <Menubar.Sub>
                <Menubar.SubTrigger
                  class="menubar-trigger {item.trigger_class || ''}"
                >
                  {item.trigger}
                </Menubar.SubTrigger>
                <Menubar.SubContent>
                  {#if typeof item.contents === "string"}
                    <Menubar.Item>
                      {item.contents}
                    </Menubar.Item>
                  {:else}
                    {#each item.contents as subitem}
                      {#if subitem === "Separator"}
                        <Menubar.Separator />
                      {:else if subitem === "Arrow"}
                        <Menubar.Arrow />
                      {:else if subitem.type === "Item"}
                        <Menubar.Item
                          class="menubar-item {subitem.class || ''}"
                          on:click={subitem.onClick}
                        >
                          {subitem.label}
                        </Menubar.Item>
                      {:else if subitem.type === "Label"}
                        <Menubar.Label
                          class="menubar-label {subitem.class || ''}"
                          on:click={subitem.onClick}
                        >
                          {subitem.label}
                        </Menubar.Label>
                      {/if}
                    {/each}
                  {/if}
                </Menubar.SubContent>
              </Menubar.Sub>
            {:else if item.type === "Item"}
              <Menubar.Item
                class="menubar-item {item.class || ''}"
                on:click={item.onClick}>{item.label}</Menubar.Item
              >
            {:else if item.type === "Label"}
              <Menubar.Label
                class="menubar-label {item.class || ''}"
                on:click={item.onClick}>{item.label}</Menubar.Label
              >
            {/if}
          {/each}
        {/if}
      </Menubar.Content>
    </Menubar.Menu>
  {/each}
</Menubar.Root>
