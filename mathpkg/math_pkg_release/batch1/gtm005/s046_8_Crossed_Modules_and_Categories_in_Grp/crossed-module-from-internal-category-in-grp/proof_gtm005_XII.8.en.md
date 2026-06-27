---
role: proof
locale: en
of_concept: crossed-module-from-internal-category-in-grp
source_book: gtm005
source_chapter: "XII"
source_section: "8"
---

From the data of an internal category in $\mathbf{Grp}$ — namely groups $C_0, C_1$ and homomorphisms $d_0, d_1 : C_1 \to C_0$, $i : C_0 \to C_1$ with $d_0 i = 1 = d_1 i$ and $[\ker d_0, \ker d_1] = 1$ — we construct the crossed module as follows.

Set $H = \ker d_0$ and $P = C_0$. Define $\alpha : H \to P$ to be the restriction $d_1|_{\ker d_0}$ of $d_1$ to the kernel of $d_0$. This is a group homomorphism.

Consider the sequence

$$1 \longrightarrow \ker d_0 \longrightarrow C_1 \xrightarrow{d_0} C_0 \longrightarrow 1.$$

The map $i : C_0 \to C_1$ provides a splitting of $d_0$ (since $d_0 i = 1$), which shows that $d_0$ is surjective, hence the sequence is exact. This short exact sequence determines an action of $P = C_0$ on $H = \ker d_0$ in the standard way: for $p \in P$, choose a lift $\tilde{p} \in C_1$ with $d_0(\tilde{p}) = p$ (for instance, $\tilde{p} = i(p)$), and define the action by conjugation:

$$h^p = \tilde{p} \, h \, \tilde{p}^{-1}.$$

One must verify that this satisfies the crossed module axioms. For $h, k \in H$ and $p, q \in P$:

- $h^1 = h$ since the lift of the identity is the identity.
- $(h^p)^q = h^{pq}$ by the standard properties of the conjugation action from a short exact sequence.
- $(hk)^p = h^p k^p$ because conjugation is a group automorphism.
- $\alpha(h^p) = p(\alpha h)p^{-1}$: this follows from $d_1(\tilde{p} h \tilde{p}^{-1}) = d_1(\tilde{p}) d_1(h) d_1(\tilde{p})^{-1}$ and the fact that $d_1(i(p)) = p$, so $d_1(\tilde{p})$ is conjugate to $p$ in $C_0$; with the commutator condition $[\ker d_0, \ker d_1] = 1$, one deduces the required identity.

Thus $(H, P, \alpha)$ is a crossed module.
