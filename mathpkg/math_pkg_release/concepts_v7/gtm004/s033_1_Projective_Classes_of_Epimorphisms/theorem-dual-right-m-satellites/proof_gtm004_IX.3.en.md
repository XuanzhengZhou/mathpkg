---
role: proof
locale: en
of_concept: theorem-dual-right-m-satellites
source_book: gtm004
source_chapter: "IX"
source_section: "3. Satellites"
---

# Proof of Right $\mathcal{M}$-Satellite Equals Right $\mathcal{M}$-Derived Functor

**Theorem 3.5.** If $H : \mathfrak{A} \to \mathfrak{B}$ is a left $\mathcal{M}$-exact functor, where $\mathcal{M}$ is an injective class of monomorphisms in $\mathfrak{A}$, then the $\mathcal{M}$-connected sequence of functors $\{R^j_{\mathcal{M}} H\}$ is the right $\mathcal{M}$-satellite of $H$, i.e., $R^j_{\mathcal{M}} H = S^j_{\mathcal{M}} H$ (with $R^j_{\mathcal{M}} H = 0$ for $j < 0$).

**Proof.** This theorem is the precise dual of Theorem 3.2. We outline the dualization:

1. Replace the abelian category $\mathfrak{A}$ by its opposite $\mathfrak{A}^{\text{op}}$, under which epimorphisms become monomorphisms and the projective class $\mathfrak{E}$ becomes an injective class $\mathcal{M}$.

2. A left $\mathcal{M}$-exact functor $H : \mathfrak{A} \to \mathfrak{B}$ corresponds to a right exact functor $H^{\text{op}} : \mathfrak{A}^{\text{op}} \to \mathfrak{B}^{\text{op}}$.

3. The right $\mathcal{M}$-derived functors $R^j_{\mathcal{M}} H$ are defined using $\mathcal{M}$-injective resolutions (the dual of $\mathcal{E}$-projective resolutions). That is, for an $\mathcal{M}$-injective resolution $A \to I^*$, we set $R^j_{\mathcal{M}} H(A) = H^j(H(I^*))$.

4. An $\mathcal{M}$-connected sequence of functors has connecting homomorphisms $\omega^j : T^j(A'') \to T^{j+1}(A')$ (note the degree shift upward, dual to the downward shift $\omega_j : T_j(A'') \to T_{j-1}(A')$ in the left satellite case).

5. The inductive construction of $\varphi^j$ proceeds by taking an $\mathcal{M}$-injective copresentation $0 \to A \to I \to C \to 0$, using that $\omega^j : R^j_{\mathcal{M}} H(C) \to R^{j+1}_{\mathcal{M}} H(A)$ is epic (since $R^{j+1}_{\mathcal{M}} H(I) = 0$ for $\mathcal{M}$-injective $I$), and defining $\varphi^{j+1}$ by the dual diagram chase.

The theorem follows from the duality principle: every statement about left satellites and projective classes dualizes to a statement about right satellites and injective classes.
