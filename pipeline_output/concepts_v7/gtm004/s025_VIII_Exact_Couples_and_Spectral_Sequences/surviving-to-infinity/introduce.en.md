---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The concept of an element "surviving to infinity" captures the intuition of a class in a spectral sequence that persists through all stages without being killed by any differential. Formally, $x \in E_n$ survives to infinity if it lies in the kernel of every subsequent differential $d_r$ ($r \geq n$) and is never in the image of any $d_r$. Such elements represent non-zero classes in the limit term $E_\infty$. In computational practice, one tracks which elements survive at each page $E_2, E_3, \ldots$; those that never become boundaries are the permanent cycles constituting $E_\infty$.
