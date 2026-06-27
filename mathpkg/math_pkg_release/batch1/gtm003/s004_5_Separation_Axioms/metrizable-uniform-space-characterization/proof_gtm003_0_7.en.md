---
role: proof
locale: en
of_concept: metrizable-uniform-space-characterization
source_book: gtm003
source_chapter: "0"
source_section: "7"
---

The text states the theorem without proof. Standard proof sketch: If a metric $d$ generates the uniformity, the sets $W_n = \{(x,y) : d(x,y) < n^{-1}\}$ form a countable base, and the uniformity is separated because $d(x,y) = 0 \iff x = y$. Conversely, given a countable base $\{V_n\}$ of the separated uniformity, one constructs a sequence of symmetric vicinities $U_n$ with $U_{n+1} \circ U_{n+1} \subset U_n \subset V_n$. Then define a pseudometric via $f(x,y) = \inf\{2^{-k} : (x,y) \in U_k\}$, which is a genuine metric because the uniformity is separated. This metric generates the original uniformity.
