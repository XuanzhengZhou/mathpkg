---
role: proof
locale: en
of_concept: cone-bijection-for-kan-extensions
source_book: gtm005
source_chapter: "X"
source_section: "5. Kan Extensions as Coends"
---

A cone $\tau: a \to TQ$ assigns to each $f: c \to Km$ an arrow $\tau(f, m): a \to Tm$ subject to the cone conditions: for each $h: m \to m'$, $\tau(Kh \circ f, m') = Th \circ \tau(f, m)$. A natural transformation $\beta: C(c, K-) \to A(a, T-)$ assigns to each $m \in M$ and each $f: c \to Km$ an arrow $\beta_m f: a \to Tm$, subject to the naturality condition: for each $h: m' \to m$, $\beta_{m'}(Kh \circ f) = Th \circ \beta_m f$. The assignments $\tau \mapsto \beta$ with $\beta_m f = \tau(f, m)$ and $\beta \mapsto \tau$ with $\tau(f, m) = \beta_m f$ are clearly mutually inverse, establishing the bijection.
