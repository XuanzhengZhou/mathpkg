---
role: proof
locale: en
of_concept: pullback-of-transition-functions
source_book: gtm020
source_chapter: "5"
source_section: "4"
---

By 4(4.2) and 4(6.3), the morphism $f^*(h_i): \theta(f^{-1}(V_i)) \rightarrow f^*(\eta)|f^{-1}(V_i)$ is an isomorphism given by $f^*(h_i)(b_1, y) = (b_1, h_i(f(b_1), y))$.

If $h_i(b, g_{i,j}(b)y) = h_j(b, y)$ for $b \in V_i \cap V_j$, then evaluating at $f(b_1)$ for $b_1 \in f^{-1}(V_i \cap V_j) = f^{-1}(V_i) \cap f^{-1}(V_j)$ gives
$$f^*(h_i)(b_1, g_{i,j}(f(b_1))y) = (b_1, h_i(f(b_1), g_{i,j}(f(b_1))y)) = (b_1, h_j(f(b_1), y)) = f^*(h_j)(b_1, y).$$

Hence $\{g_{i,j} \circ f\}$ is the set of transition functions for $f^*(\eta)$.
