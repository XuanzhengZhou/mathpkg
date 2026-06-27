---
role: proof
locale: en
of_concept: classification-of-collineations-by-segre-symbol
source_book: gtm049
source_chapter: "7"
source_section: "7.6 Classification of Collineations"
---

(i) Suppose the Segre symbols are the same and let the elementary divisors of $f, g$ be $(X - x_i)^{n_{ij}}$, $(X - y_i)^{n_{ij}}$, respectively. Suppose

$$V_f = \bigoplus_{i=1}^{t} K_i, \quad V_g = \bigoplus_{i=1}^{t} L_i,$$

where, for each $i$, $K_i$ is the submodule of $V_f$ consisting of all elements annihilated by some power of $X - x_i$; and $L_i$ similarly for $X - y_i$ in $V_g$. If $f_i, g_i$ are the restrictions of $f, g$ to $K_i, L_i$, respectively, then the Segre symbol of both $f_i$ and $g_i$ is $\{(n_{i1}, \ldots, n_{ik_i})\}$.

Since $f_i$ and $(x_i/y_i)g_i$ have the same elementary divisors, there is a module isomorphism $e_i$ of $K_i$ onto $L_i$. Clearly, $e_i$ must map the invariant configuration of $\mathcal{P}(f_i)$ onto the invariant configuration of $\mathcal{P}((x_i/y_i)g_i) = \mathcal{P}(g_i)$. If $e$ is the result of combining $e_1, \ldots, e_t$, then $e$ is an isomorphism of $V_f$ onto $V_g$.

Now any submodule $M$ of $V_f$ has a direct decomposition

$$M = (M \cap K_1) \oplus \cdots \oplus (M \cap K_t)$$

where $M \cap K_i$ is the set of all elements of $M$ annihilated by some power of $(X - x_i)$. There is a similar decomposition for any submodule of $V_g$. It follows that $e$ maps the invariant configuration of $\mathcal{P}(f)$ onto that of $\mathcal{P}(g)$ and thus $\mathcal{P}(e)$ is the required collineation.

(ii) Conversely, if there exists a collineation mapping the invariant configuration of $\mathcal{P}(f)$ onto that of $\mathcal{P}(g)$, then the corresponding semi-linear isomorphism induces a module isomorphism between $V_f$ and $V_g$ preserving the invariant submodule lattices. This forces the elementary divisors to coincide, hence the Segre symbols are equal.
