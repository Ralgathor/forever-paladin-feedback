# Notes for edits to this repository

## Talent tree layout (proposed trees)

Each tree has 7 rows and 4 columns. When a proposal adds, removes or moves a talent, place the talents of each changed row with these rules:

1. Fill the row from column 1.
2. A row with only two slots is centered: columns 2 and 3.
3. A prerequisite arrow counts as a slot. A vertical arrow takes its column in each row that it goes through. The talents at the two ends of an arrow stay in the same column.
4. A row with one talent and no arrow (a capstone) uses column 2.

Set the column in the `PROPOSED` patch of `calculator/index.html` (`col`). Use `pid:null` for a move that only changes the column. Then list the talents of the row in column order in the layout table of the tree (`proposals/holy.md`, `protection.md`, `retribution.md`) and in the Claude Doc tab.

The beta trees follow the Wowhead layout. Do not change them.

## Calculator versions

- `calculator/index.html` is the current version. Its proposed build codes start with `v2p`.
- `calculator/v1/index.html` is frozen. Do not edit it.
- A column move does not change the build codes. A change to the talent list or the talent order of a tree does. Then freeze the current page as a new version first.
