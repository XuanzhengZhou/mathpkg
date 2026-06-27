---
role: proof
locale: en
of_concept: projective-plane-non-orientable
source_book: gtm051
source_chapter: "5"
source_section: "5.5"
---

Consider the antipodal map $i: S^2 \to S^2$ which maps $x \mapsto -x$. In terms of the atlas for $S^2$ defined in (5.5.3, 1),

$$u_+ \circ i \circ u^{-1}(\xi, \eta) = (-\xi, -\eta); \quad (\xi, \eta) \neq (0, 0).$$

It follows that this map reverses orientation. Now assume that $P^2$ possesses an oriented atlas $(u_\alpha, P_\alpha^2)_{\alpha \in A}$. Recall that $\varphi: S^2 \to P^2$ is the map $x \mapsto \{x, -x\}$. The sets $\varphi^{-1}P_\alpha^2$ can be divided into sets $S_\alpha^2 \cup iS_\alpha^2$ in such a way that $\varphi: S_\alpha^2 \to P^2$ and $\varphi: iS_\alpha^2 \to P^2$ are diffeomorphisms. Thus

$$(u_\alpha \circ \varphi, S_\alpha^2)_{\alpha \in A} \cup (u_\alpha \circ \varphi, iS_\alpha^2)_{\alpha \in A}$$

is an orientable atlas for $S^2$. But $i: S_\alpha^2 \to iS_\alpha^2$ has the coordinate representation $\mathrm{id}: u_\alpha(P_\alpha^2) \to u_\alpha(P_\alpha^2)$. This is a contradiction since $i$ is orientation reversing, but $\mathrm{id}: u_\alpha(P_\alpha^2) \to u_\alpha(P_\alpha^2)$ is not.
