<script lang="ts"></script>

<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>hello</Menubar.Trigger>
    <Menubar.Content class="z-50 w-full max-w-[220px] rounded-xl border border-muted bg-background px-1 py-1.5 shadow-popover !ring-0 !ring-transparent">
      <Menubar.Item>
        <Menubar.Trigger>hello</Menubar.Trigger>
      </Menubar.Item>
      <Menubar.Item>New Window</Menubar.Item>
      <Menubar.Item>New Incognito Window</Menubar.Item>
      <Menubar.Separator />
      <Menubar.Sub>
        <Menubar.SubTrigger>Share</Menubar.SubTrigger>
        <Menubar.SubContent>
          <Menubar.Item>Email link</Menubar.Item>
          <Menubar.Item>Messages</Menubar.Item>
          <Menubar.Item>Notes</Menubar.Item>
        </Menubar.SubContent>
      </Menubar.Sub>
      <Menubar.Separator />
      <Menubar.Item>Print...</Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>hello</Menubar.Trigger>
    <Menubar.Content>i</Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
