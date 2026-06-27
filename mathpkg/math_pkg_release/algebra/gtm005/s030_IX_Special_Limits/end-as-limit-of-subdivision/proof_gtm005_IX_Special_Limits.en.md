---
role: proof
locale: en
of_concept: end-as-limit-of-subdivision
source_book: gtm005
source_chapter: "IX"
source_section: "Special Limits"
---

Define the subdivision category $C^{\S}$: objects are symbols $c^{\S}$ (one for each $c \in C$) and $f^{\S}$ (one for each arrow $f$ in $C$, with $f^{\S} \neq (1_c)^{\S}$). For each arrow $f : b \to c$ in $C$, there are two non-identity arrows in $C^{\S}$: $b^{\S} \to f^{\S}$ and $c^{\S} \to f^{\S}$ (plus identity arrows).

Define $S^{\S} : C^{\S} \to X$ on objects by $S^{\S}(c^{\S}) = S(c,c)$ and $S^{\S}(f^{\S}) = S(b,c)$ for $f : b \to c$. On arrows, for $f : b \to c$, the arrow $b^{\S} \to f^{\S}$ maps to $S(b, f) : S(b,b) \to S(b,c)$, and $c^{\S} \to f^{\S}$ maps to $S(f, c) : S(c,c) \to S(b,c)$.

A cone $\tau : x \to S^{\S}$ assigns to each $c^{\S}$ an arrow $\tau_c : x \to S(c,c)$ and to each $f^{\S}$ (for $f : b \to c$) an arrow $\tau_f : x \to S(b,c)$ such that the triangles commute: $S(b,f) \circ \tau_b = \tau_f$ and $S(f,c) \circ \tau_c = \tau_f$. Eliminating $\tau_f$ gives $S(b,f) \circ \tau_b = S(f,c) \circ \tau_c$, which is precisely the dinaturality hexagon condition for a wedge $\tau : x \xrightarrow{\bullet} S$. Thus cones over $S^{\S}$ correspond bijectively to dinatural wedges from $x$ to $S$. Hence a limiting cone for $S^{\S}$ is a universal dinatural wedge, i.e., an end of $S$.
