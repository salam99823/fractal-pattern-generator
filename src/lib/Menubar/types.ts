type BaseMenu = {
  name: string,
  icon?: string,
  shortcut?: string,
}
type MenuItem = BaseMenu & {
  action: () => void,
}
export type Menu = BaseMenu & {
  children: Array<Menu | MenuItem>,
}
