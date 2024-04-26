<script lang="ts">
    import { Menubar } from "bits-ui";

    type Menu = {
        trigger: string;
        contents: (Content | SubMenu)[];
        trigger_class?: string | undefined | null;
        contents_class?: string | undefined | null;
    };

    type SubMenu = {
        icon?: string | undefined | null;
        type: "SubMenu";
        trigger: string;
        contents: Content[];
        icon_class?: string | undefined | null;
        trigger_class?: string | undefined | null;
        contents_class?: string | undefined | null;
    };

    type Content = {
        icon?: string | undefined | null;
        type: "Label" | "Item" | "Separator" | "Arrow";
        label: string;
        onClick?: () => void;
        icon_class?: string | undefined | null;
        class?: string | undefined | null;
        href?: string | undefined | null;
    };

    let menus: Menu[] = [
        {
            trigger: "Файл",
            contents_class: "file-content menubar-content",
            trigger_class: "file-trigger menubar-trigger",
            contents: [
                {
                    icon: "/tauri.svg",
                    icon_class: "new-file-btn",
                    label: "Новый файл",
                    type: "Item",
                    onClick: () => {
                        console.log("new file");
                    },
                    class: "menubar-item",
                },
                {
                    label: "Открыть файл",
                    type: "Item",
                    onClick: () => {
                        console.log("open file");
                    },
                    class: "menubar-item",
                },
                {
                    trigger: "Открыть последние",
                    type: "SubMenu",
                    contents: [],
                    trigger_class: "menubar-subtrigger",
                },
                {
                    type: "Separator",
                    label: "",
                    class: "menubar-separator",
                },
                {
                    type: "Item",
                    label: "Сохранить",
                    onClick: () => {
                        console.log("save");
                    },
                    class: "menubar-item",
                },
                {
                    type: "Item",
                    label: "Сохранить как",
                    onClick: () => {
                        console.log("save as");
                    },
                    class: "menubar-item",
                },
                {
                    type: "Item",
                    label: "Сохранить изображение",
                    onClick: () => {
                        console.log("save image");
                    },
                    class: "menubar-item",
                },
                {
                    type: "Separator",
                    label: "",
                    class: "menubar-separator",
                },
                {
                    type: "Item",
                    label: "Выход",
                    onClick: () => {
                        console.log("exit");
                    },
                    class: "menubar-item",
                },
            ],
        },
        {
            trigger: "Настройки",
            contents_class: "settings-content menubar-content",
            trigger_class: "settings-trigger menubar-trigger",
            contents: [
                {
                    type: "Item",
                    label: "Параметры",
                    onClick: () => {
                        console.log("settings");
                    },
                    class: "menubar-item",
                },
                {
                    type: "Item",
                    label: "Сочетания клавиш",
                    onClick: () => {
                        console.log("keyboard shortcuts");
                    },
                    class: "menubar-item",
                },
            ],
        },
        {
            trigger: "Справка",
            contents_class: "about-content menubar-content",
            trigger_class: "about-trigger menubar-trigger",
            contents: [
                {
                    type: "Item",
                    label: "О программе",
                    onClick: () => {
                        console.log("about");
                    },
                    class: "menubar-item",
                },
                {
                    type: "Item",
                    label: "Справка",
                    onClick: () => {
                        console.log("help");
                    },
                    class: "menubar-item",
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
            <Menubar.Content
                align="start"
                class={menu.contents_class}
            >
                {#each menu.contents as item}
                    {#if item.type === "Separator"}
                        <Menubar.Separator
                            class={item.class}
                            on:click={item.onClick}
                            >{item.label}
                        </Menubar.Separator>
                    {:else if item.type === "Arrow"}
                        <Menubar.Arrow
                            class={item.class}
                            on:click={item.onClick}
                        >
                            {item.label}
                        </Menubar.Arrow>
                    {:else if item.type === "SubMenu"}
                        <Menubar.Sub>
                            <Menubar.SubTrigger class={item.trigger_class}>
                                {#if item.icon}
                                    <img
                                        src={item.icon}
                                        alt="icon"
                                        class={item.icon_class}
                                    />{/if}{item.trigger}
                            </Menubar.SubTrigger>
                            <Menubar.SubContent
                                align="start"
                                class={item.contents_class}
                            >
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
                                            >{#if subitem.icon}
                                                <img
                                                    src={subitem.icon}
                                                    alt="icon"
                                                    class={subitem.icon_class}
                                                />{/if}{subitem.label}
                                        </Menubar.Item>
                                    {:else if subitem.type === "Label"}
                                        <Menubar.Label
                                            class={subitem.class}
                                            on:click={subitem.onClick}
                                            >{#if item.icon}
                                                <img
                                                    src={subitem.icon}
                                                    alt="icon"
                                                    class={subitem.icon_class}
                                                />{/if}{subitem.label}
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
                            >{#if item.icon}
                                <img
                                    src={item.icon}
                                    alt="icon"
                                    class={item.icon_class}
                                />{/if}{item.label}
                        </Menubar.Item>
                    {:else if item.type === "Label"}
                        <Menubar.Label
                            class={item.class}
                            on:click={item.onClick}
                            >{#if item.icon}
                                <img
                                    src={item.icon}
                                    alt="icon"
                                    class={item.class}
                                />{/if}{item.label}
                        </Menubar.Label>
                    {/if}
                {/each}
            </Menubar.Content>
        </Menubar.Menu>
    {/each}
</Menubar.Root>
