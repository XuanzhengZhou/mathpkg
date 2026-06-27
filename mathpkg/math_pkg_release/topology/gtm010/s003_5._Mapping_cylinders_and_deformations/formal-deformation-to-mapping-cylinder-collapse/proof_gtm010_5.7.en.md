---
role: proof
locale: en
of_concept: formal-deformation-to-mapping-cylinder-collapse
source_book: gtm010
source_chapter: "5"
source_section: "5"
---

First, show that for each $i$, $M_{g_i} \searrow \text{dom } g_i = K_i$. If $K_i \nearrow K_{i+1}$, then $M_{g_i} = (K_i \times I) \cup_{g_i} K_{i+1} \searrow (K_i \times I) \searrow (K_i \times 0) \equiv K_i$. If $K_i \searrow K_{i+1}$, then by (5.4), $M_{g_i} \searrow M_{g_i|_{K_{i+1}}} \cup K_i = (K_{i+1} \times I) \cup (K_i \times 0) \searrow K_i \times 0 \equiv K_i$.

Now apply (5.6) repeatedly: $M_g \wedge M_{g_0} \cup M_{g_1 \circ \dots \circ g_{q-1}}$ rel $K_0$, then $M_{g_1 \circ \dots \circ g_{q-1}} \wedge M_{g_1} \cup M_{g_2 \circ \dots \circ g_{q-1}}$, and so on. By induction, $M_g \wedge M_{g_0} \cup M_{g_1} \cup \dots \cup M_{g_{q-1}}$ rel $K_0$.
