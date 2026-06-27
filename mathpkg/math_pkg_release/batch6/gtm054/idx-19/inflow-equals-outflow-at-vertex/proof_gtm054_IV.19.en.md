---
role: proof
locale: en
of_concept: inflow-equals-outflow-at-vertex
source_book: gtm054
source_chapter: "IV"
source_section: "19"
---

By definition, the value of the flow $h$ at vertex $x$ is

$$h(x) = \sum_{y \in V \setminus \{x\}} h(y, x).$$

This is the total inflow at $x$. By property B2, the flow conservation law, the inflow at any vertex equals the outflow at that vertex. Hence

$$h(x) = \sum_{y \in V \setminus \{x\}} h(x, y).$$

This identity is used in the vertex-capacitated formulation of network flows to express the flow through a vertex in terms of both incoming and outgoing edges.
