---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The taboo visit notation ${}^k n_j(\omega)$ counts visits to state $j$ that occur before the first visit to state $k$, effectively treating $k$ as a forbidden (taboo) state. The shifted version ${}^k \bar{n}_j$ starts counting after time $0$. These quantities give rise to the taboo matrices ${}^k N$ and ${}^k \bar{N}$, which collect the expected taboo visit counts. A notable edge case is that ${}^j n_j(\omega) = 0$ (no visits counted before the first visit), while ${}^j \bar{n}_j(\omega) = 1$ if the chain starts at $j$.
