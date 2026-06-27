---
role: proof
locale: en
of_concept: morita-duality-submodule-correspondence
source_book: gtm013
source_chapter: "7"
source_section: "24. Morita Dualities"
---

Since $\sigma_M$ is an isomorphism, we have for $L \leq M^*$

$$l_{M^{**}}(L) = \{ \sigma_M(x) \mid \sigma_M(x)(h) = 0 \text{ for all } h \in L \}$$
$$= \{ \sigma_M(x) \mid h(x) = 0 \text{ for all } h \in L \}$$
$$= \sigma_M(l_M(L))$$

and hence

$$r_{M^*} (l_{M^{**}}(L)) = \{ f \in M^* \mid \sigma_M(y)(f) = 0 \text{ for all } y \in l_M(L) \}$$
$$= r_{M^*} (l_M(L)).$$

Thus the second assertion of (1) follows from the first of (2) and, by symmetry, we have the second of (2). Now (3) and (4) follow from (1) and (2) and (24.3).
