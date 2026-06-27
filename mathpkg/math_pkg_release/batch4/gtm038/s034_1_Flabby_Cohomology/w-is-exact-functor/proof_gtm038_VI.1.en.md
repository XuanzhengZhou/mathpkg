---
role: proof
locale: en
of_concept: w-is-exact-functor
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---

Let $\mathcal{S}_1 \xrightarrow{\psi} \mathcal{S} \xrightarrow{\varphi} \mathcal{S}_2$ be exact.

(a) From the functoriality, $W\varphi \circ W\psi = W(\varphi \circ \psi) = W(0) = 0$, so $\text{Im}(W\psi) \subset \ker(W\varphi)$.

(b) Let $\sigma \in W(\mathcal{S})_x$ and $W\varphi(\sigma) = \mathbf{O}_x$. Then there exists a neighborhood $U(x) \subset X$ and an $s \in \hat{\Gamma}(U, \mathcal{S})$ with $r s(x) = \sigma$, therefore $W\varphi \circ r s(x) = \mathbf{O}_x$.

Hence there exists a neighborhood $V(x) \subset U$ with $\mathbf{O} = W\varphi \circ r s \mid_V = r(\varphi \circ s) \mid_V$; therefore $(\varphi \circ s) \mid_V = \mathbf{O}$.

Since the original sequence is exact, we can construct an $s_1 \in \hat{\Gamma}(V, \mathcal{S}_1)$ with $\psi \circ s_1 = s \mid_V$ pointwise (choosing preimages at each stalk, which is possible without continuity constraints for generalized sections). Then
$$W\psi \circ r s_1 = r(\psi \circ s_1) = r s \mid_V,$$
and therefore $W\psi(r s_1(x)) = \sigma$. Thus $\ker(W\varphi) \subset \text{Im}(W\psi)$.

Together (a) and (b) establish exactness of $W(\mathcal{S}_1) \to W(\mathcal{S}) \to W(\mathcal{S}_2)$.
