---
role: proof
locale: en
of_concept: dgamma2-plus-dgamma1-surjective
source_book: gtm014
source_chapter: "V"
source_section: "5. Local Transverse Stability"
---

Let $v$ be in $T_{\sigma}\mathcal{D}_{\sigma}$ and let $c(t)$ be a curve representing $v$ in $\mathcal{D}_{\sigma}$. Using the local parametrization $T$ of $J^{k}(X,Y)$ (from Proposition 5.1), we can write $c(t) = T(a(t))$ for some curve $a(t) = (p(t), q(t), \tau(t))$ in $U \times V \times \mathring{\mathcal{O}}_{\sigma}$, where $U$ and $V$ are coordinate neighborhoods of the source and target of $\sigma$. Concretely,
\[
c(t) = j^{k}(T_{q(t)}) \cdot \tau(t) \cdot j^{k}(T_{p(t)}^{-1}),
\]
where $T_{a}$ denotes the translation by $a$ in the local coordinates. Thus it suffices to show that $\tau(t)$ can be expressed as
\[
\tau(t) = j^{k}(h(t)) \cdot \sigma \cdot j^{k}(g(t)^{-1})
\]
for smooth curves $g(t)$ in $\operatorname{Diff}(X)_{p}$ and $h(t)$ in $\operatorname{Diff}(Y)_{q}$ with $g(0) = \operatorname{id}_{X}$ and $h(0) = \operatorname{id}_{Y}$, for then taking derivatives at $t = 0$ yields $v = (d\gamma_{2})(\xi) + (d\gamma_{1})(\eta)$ where $\xi = \left.\frac{d}{dt}g(t)\right|_{t=0}$ and $\eta = \left.\frac{d}{dt}h(t)\right|_{t=0}$.

Now $\tau(t)$ is a curve in $\mathring{\mathcal{O}}_{\sigma}$, the orbit of $\sigma$ under the connected component $\mathring{\mathcal{G}} = \mathring{\mathcal{G}}^{k}(X)_{p} \times \mathring{\mathcal{G}}^{k}(Y)_{q}$ of the jet group. Since $\mathring{\mathcal{G}}$ is a Lie group (it is open in the space of $k$-jets of diffeomorphisms), there exists a smooth curve $(\tilde{g}(t), \tilde{h}(t))$ in $\mathring{\mathcal{G}}^{k}(X)_{p} \times \mathring{\mathcal{G}}^{k}(Y)_{q}$ such that
\[
\tilde{h}(t) \cdot \sigma \cdot \tilde{g}(t)^{-1} = \tau(t).
\]

In local coordinates, elements of $\mathring{\mathcal{G}}^{k}(X)_{p}$ are $k$-jets of polynomial mappings of degree $\leq k$ on $\mathbf{R}^{n}$ which are diffeomorphisms on a neighborhood of $0$. Let $g(t)$ be the unique polynomial of degree $\leq k$ such that $j^{k}g(t) = \tilde{g}(t)$, and define $h(t)$ similarly. Since $\det(dg_{0})_{p} > 0$ and $\det(dh_{0})_{q} > 0$, we may apply Proposition 5.5 to extend these polynomial mappings to globally defined diffeomorphisms $g_{t}$ on $X$ and $h_{t}$ on $Y$. This yields the desired curves of diffeomorphisms, completing the proof.
