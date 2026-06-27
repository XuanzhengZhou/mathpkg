---
role: proof
locale: en
of_concept: coend-as-colimit
source_book: gtm005
source_chapter: "IX"
source_section: "6"
---

Dual to ends, the coend $\int^c S(c, c)$ is defined as a universal cowedge. It can be constructed as a coequalizer:

$$\coprod_{f: b \to c} S(c, b) \rightrightarrows \coprod_a S(a, a) \to \int^a S(a, a).$$

The two parallel maps: for each $f: b \to c$, the first map sends the $(c, b)$-summand to the $c$-summand via $S(1, f): S(c, b) \to S(c, c)$, and the second sends it to the $b$-summand via $S(f, 1): S(c, b) \to S(b, b)$.

A cowedge $S \xrightarrow{\bullet} x$ is a family $\tau_a: S(a, a) \to x$ such that for each $f: b \to c$, $\tau_b \circ S(f, 1) = \tau_c \circ S(1, f)$. The coequalizer condition encodes this dinaturality, and its universal property gives the universal cowedge.
