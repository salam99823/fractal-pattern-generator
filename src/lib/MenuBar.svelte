<script lang="ts">
  import { Menubar } from "bits-ui";

  type Menu = {
    trigger: string;
    contents: (Content | SubMenu)[];
    trigger_class?: string | undefined | null;
    contents_class?: string | undefined | null;
  };

  type SubMenu = {
    type: "SubMenu";
    trigger: string;
    contents: Content[];
    trigger_class?: string | undefined | null;
    contents_class?: string | undefined | null;
  };

  type Content = {
    type: "Label" | "Item" | "Separator" | "Arrow";
    label: string;
    onClick?: () => void;
    class?: string | undefined | null;
    href?: string | undefined | null;
  };

  let menus: Menu[] = [
    {
      trigger: "Файл",
      contents_class: "menubar-content",
      trigger_class: "menubar-trigger",
      contents: [
        {
          label: "Новый файл",
          type: "Item",
          onClick: () => {
            console.log("new file");
          },
        },
        {
          label: "Открыть файл",
          type: "Item",
          onClick: () => {
            console.log("open file");
          },
        },
        {
          trigger: "Открыть последние",
          type: "SubMenu",
          contents: [],
        },
        {
          type: "Separator",
          label: "",
          class: "menubar-separator",
        },
      ],
    },
    {
      trigger: "Настройки",
      contents_class: "menubar-content",
      trigger_class: "menubar-trigger",
      contents: [
        {
          label: "Новый файл",
          type: "Item",
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
    },
    {
      trigger: "Справка",
      contents_class: "menubar-content",
      trigger_class: "menubar-trigger",
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
    },
  ];
</script>

<Menubar.Root class="menubar-root">
  {#each menus as menu}
    <Menubar.Menu>
      <Menubar.Trigger class={menu.trigger_class}>
        {menu.trigger}
      </Menubar.Trigger>
      <Menubar.Content align="start" class={menu.contents_class}>
        {#each menu.contents as item}
          {#if item.type === "Separator"}
            <Menubar.Separator class={item.class} on:click={item.onClick}
              >{item.label}
            </Menubar.Separator>
          {:else if item.type === "Arrow"}
            <Menubar.Arrow class={item.class} on:click={item.onClick}>
              {item.label}
            </Menubar.Arrow>
          {:else if item.type === "SubMenu"}
            <Menubar.Sub>
              <Menubar.SubTrigger class={item.trigger_class}>
                {item.trigger}
              </Menubar.SubTrigger>
              <Menubar.SubContent align="start" class={item.contents_class}>
                {#each item.contents as subitem}
                  {#if subitem.type === "Separator"}
                    <Menubar.Separator
                      class={subitem.class}
                      on:click={subitem.onClick}
                      >{subitem.label}
                    </Menubar.Separator>
                  {:else if subitem.type === "Arrow"}
                    <Menubar.Arrow
                      class={subitem.class}
                      on:click={subitem.onClick}
                    >
                      {subitem.label}
                    </Menubar.Arrow>
                  {:else if subitem.type === "Item"}
                    <Menubar.Item
                      class={subitem.class}
                      on:click={subitem.onClick}
                    >
                      {subitem.label}
                    </Menubar.Item>
                  {:else if subitem.type === "Label"}
                    <Menubar.Label
                      class={subitem.class}
                      on:click={subitem.onClick}
                    >
                      {subitem.label}
                    </Menubar.Label>
                  {/if}
                {/each}
              </Menubar.SubContent>
            </Menubar.Sub>
          {:else if item.type === "Item"}
            <Menubar.Item
              class={item.class}
              on:click={item.onClick}
              href={item.href}
              target="_blank"
              >{item.label}
            </Menubar.Item>
          {:else if item.type === "Label"}
            <Menubar.Label class={item.class} on:click={item.onClick}
              >{item.label}
            </Menubar.Label>
          {/if}
        {/each}
      </Menubar.Content>
    </Menubar.Menu>
  {/each}
</Menubar.Root>
