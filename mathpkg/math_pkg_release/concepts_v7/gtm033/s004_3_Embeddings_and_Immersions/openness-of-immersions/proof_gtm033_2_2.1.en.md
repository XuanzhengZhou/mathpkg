---
role: proof
locale: en
of_concept: openness-of-immersions
source_book: gtm033
source_chapter: "2. Function Spaces"
source_section: "2.1"
---

# Proof of Openness of Immersions in the Strong Topology (Theorem 1.1)

**Theorem 1.1.** The set $\operatorname{Imm}^r(M,N)$ of $C^r$ immersions is open in $C^r_S(M,N)$, $r \geqslant 1$.

*Proof.* Since

$$\operatorname{Imm}^r(M,N) = \operatorname{Imm}^1(M,N) \cap C^r(M,N)$$

it suffices to prove this for $r = 1$. If $f: M \rightarrow N$ is a $C^1$ immersion one can choose a neighborhood $\mathcal{N}^1(f; \Phi, \Psi, K, \varepsilon)$ as follows. Let $\Psi^0 = \{\psi_\beta, V_\beta\}_{\beta \in B}$ be any atlas for $N$. Pick an atlas $\Phi = \{\varphi_i, U_i\}_{i \in \Lambda}$ for $M$ so that each $U_i$ has compact closure, and for each $i \in \Lambda$ there exists $\beta(i) \in B$ such that $f(U_i) \subset V_{\beta(i)}$. Put $V_{\beta(i)} = V_i$, $\psi_{\beta(i)} = \psi_i$, and $\Psi = \{\psi_i, V_i\}_{i \in \Lambda}$. Let $K = \{K_i\}_{i \in \Lambda}$ be a compact cover of $M$ with $K_i \subset U_i$. Choose $\varepsilon_i > 0$ such that any map whose local representation has derivatives within $\varepsilon_i$ of those of $f$ on $K_i$ is also an immersion on $K_i$. Such $\varepsilon_i$ exist because the condition of being an immersion (i.e., having injective derivative) is an open condition in the space of first derivatives. Setting $\varepsilon = \{\varepsilon_i\}_{i \in \Lambda}$ gives the required neighborhood $\mathcal{N}^1(f; \Phi, \Psi, K, \varepsilon)$. Any $g$ in this neighborhood has the property that each $g|U_i$ is an immersion, hence $g$ is an immersion on all of $M$.

$\square$

**Remark.** The key point is that the immersion condition $T_x f$ injective is an open condition on the 1-jet of $f$. Since the strong topology provides uniform control over compact sets via the cover $\{K_i\}$, we can ensure that every $g$ sufficiently close to $f$ in the strong topology remains an immersion.
