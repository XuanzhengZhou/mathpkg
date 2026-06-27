---
role: proof
locale: en
of_concept: theorem-2-2-globalization
source_book: gtm033
source_chapter: "3"
source_section: "2. Transversality"
---

# Proof of Theorem 2.2: Globalization Theorem for Rich Mapping Classes

**Theorem 2.2 (Globalization Theorem).** Let $\mathcal{X}$ be a rich $C^r$ mapping class on $(M,N)$, $0 \leqslant r \leqslant \infty$. For every closed set $L \subset M$:

(a) $\mathcal{X}_L(M,N)$ is dense and open in $C^r_S(M,N)$;

(b) $\mathcal{X}_L(M,N)$ is weakly dense and open if $L$ is compact.

*Proof.* We prove (a); the proof of (b) is similar. Let $\{K_i\}_{i \in \Lambda}$ be a locally finite covering of $L$ by compact sets, each contained in a coordinate domain of $M$. For each $i$, choose open sets $E \subset M$, $V_j \subset N$ such that $K_i \subset E$, $E$ and $V_j$ are subsets of elements of the covers $\mathcal{U}, \mathcal{V}$ (from the richness condition), and $f(K_i) \subset V_j$. The richness hypothesis ensures that $\mathcal{X}_{K_i}(E, V_j)$ is dense and open in $C^r_W(E, V_j)$.

To simplify notation, identify $V_j$ with an open subset of a halfspace via $\psi_j$, so that vector operations make sense on elements of $V_j$.

If $g \in C^r_W(E, V_j)$ is sufficiently close to $f|E$, the following map $\Gamma(g) = h \in C^r(M,N)$ is well-defined:

$$h(x) = \begin{cases} f(x) + \lambda(x)[g(x) - f(x)] & \text{if } x \in E \\ f(x) & \text{if } x \in M - E. \end{cases}$$

Here $\lambda: M \to [0,1]$ is a $C^r$ bump function equal to $1$ on a neighborhood of $K_i$ and with compact support in $E$. Moreover, as $g$ tends to $f|E$ in the weak topology, $h \to f$ in the strong topology. Since $\mathcal{X}_{K_i}(E, V_j)$ is dense, we can choose $g \in \mathcal{X}_{K_i}(E, V_j)$ so close to $f|E$ that $h \in \mathcal{N}$ (a given strong neighborhood of $f$). Since $h = g$ near $K_i$, it follows from the localization axiom that $h \in \mathcal{X}_{K_i}(M,N)$.

This shows that for all $i \in \Lambda$, the set $\mathcal{X}_{K_i}(M,N)$ is dense in $C^r_S(M,N)$; and we already know it is open (by the localization axiom and richness). It follows from the Baire category theorem (applied to the complete metric space structure on $C^r_S$) that $\bigcap_i \mathcal{X}_{K_i}(M,N)$ is strongly dense; since this intersection contains $\mathcal{X}_L(M,N)$ (by the localization axiom again), the latter is therefore strongly dense.

The openness of $\mathcal{X}_L(M,N)$ follows similarly from the localization axiom: for any $f \in \mathcal{X}_L(M,N)$, cover $L$ by finitely many $K_i$, and the openness of each $\mathcal{X}_{K_i}(M,N)$ near $f$ (via the richness condition) implies $\mathcal{X}_L(M,N)$ contains a strong neighborhood of $f$.

QED
