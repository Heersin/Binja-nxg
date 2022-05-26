# Binja-nxg
Generate networkx graphs / call chains for analysis

## Expect Feature
- Generate networkx graphs
- Store Graphs
- Display Graphs In BinaryNinja
- Provide Simple Operations (has path/find path ... )

## Plugin Menu
- Binja-nxg
  - GenGraphs : Generate Graphs in Manager
  - GraphManager : List/Delete/Set/Refresh/Draw/Info Graph/etc..
  - GraphOperation : has_path ...
  - Recipes : quick script to extract info directly

## Project Structure
- Binja-nxg : project main directory
  - features/ : 
    - recipes code
    - ui/ : binayrninja ui utlis
    - src/ : implements for headless binja
      - analysis implementation based on `graphs`
      - graphs/ : generate graphs (and add to cache)

## Other