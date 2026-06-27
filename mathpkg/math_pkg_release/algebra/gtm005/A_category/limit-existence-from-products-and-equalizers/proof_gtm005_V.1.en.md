---
role: proof
locale: en
of_concept: limit-existence-from-products-and-equalizers
source_book: gtm005
source_chapter: "V"
source_section: "1. Creation of Limits"
---

By assumption, the products $\prod_i F_i$ and $\prod_u F_{\operatorname{cod}u}$ exist, where the second product is taken over all arrows $u$ of $J$, with the $u$-th factor being $F_{\operatorname{cod}u}$. Let $p_i: \prod_i F_i \to F_i$ and $q_u: \prod_u F_{\operatorname{cod}u} \to F_{\operatorname{cod}u}$ be the product projections.

Define two morphisms $f, g: \prod_i F_i \to \prod_u F_{\operatorname{cod}u}$ by specifying their components: for each arrow $u: j \to k$ in $J$, set $q_u \circ f = p_k$ and $q_u \circ g = F_u \circ p_j$. Since $\prod_u F_{\operatorname{cod}u}$ is a product, these uniquely determine $f$ and $g$.

By hypothesis, there exists an equalizer $e: d \to \prod_i F_i$ of $f$ and $g$. Set $\mu_i = p_i \circ e : d \to F_i$ for each $i \in \operatorname{obj}(J)$. Since $e$ equalizes $f$ and $g$, for each arrow $u: j \to k$ we have $q_u \circ f \circ e = q_u \circ g \circ e$, i.e., $p_k \circ e = F_u \circ p_j \circ e$, so $F_u \circ \mu_j = \mu_k$. Thus $\mu: \Delta d \to F$ is a cone.

If $\tau: \Delta c \to F$ is any other cone, its components $\tau_i: c \to F_i$ induce a unique map $h: c \to \prod_i F_i$ with $p_i \circ h = \tau_i$. Since $\tau$ is a cone, $F_u \circ \tau_j = \tau_k$ for all $u$, which implies $f \circ h = g \circ h$. By the universal property of the equalizer, $h$ factors uniquely as $h = e \circ h'$ for some $h': c \to d$. Then $\mu_i \circ h' = p_i \circ e \circ h' = p_i \circ h = \tau_i$, so $\mu \circ \Delta h' = \tau$. Uniqueness of $h'$ follows from the fact that $e$ is monic. Hence $\mu$ is a limiting cone.
