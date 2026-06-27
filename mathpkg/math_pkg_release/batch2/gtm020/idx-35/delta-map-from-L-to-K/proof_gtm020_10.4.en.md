---
role: proof
locale: en
of_concept: delta-map-from-L-to-K
source_book: gtm020
source_chapter: "10. Relative K-Theory"
source_section: "4"
---

Each difference isomorphism $\alpha: \xi_0 \rightarrow \xi_1$ is equivalent in $L(X, A)$ to $\alpha \oplus 1: \xi_0 \oplus \zeta \rightarrow \xi_1 \oplus \zeta$. If $\zeta$ has the property that $\xi_1 \oplus \zeta$ is isomorphic to $\theta^m$, then
$$\Delta([\alpha: \xi_0 \rightarrow \xi_1]) = \{(\xi_0 \oplus \zeta)/(\alpha \oplus 1)\} - m$$
proves that $\Delta$ is uniquely defined.

To prove that this relation can serve as a definition of $\Delta$, consider $[\alpha: \xi \rightarrow \theta^m] = [\beta: \eta \rightarrow \theta^n]$. There exist vector bundles $\zeta_1$ and $\zeta_2$ with $\alpha \oplus 1: \xi \oplus \zeta_1 \rightarrow \theta^m \oplus \zeta_1$ isomorphic to $\beta \oplus 1: \eta \oplus \zeta_2 \rightarrow \theta^n \oplus \zeta_2$. Since $\zeta_1$ and $\zeta_2$ are $s$-equivalent, there exists a vector bundle $\zeta$ with $\zeta_1 \oplus \zeta$ isomorphic to $\theta^p$, $\zeta_2 \oplus \zeta$ isomorphic to $\theta^q$, and $m + p = n + q = k$. Then $\alpha \oplus 1: \xi \oplus \theta^p \rightarrow \theta^k$ and $\beta \oplus 1: \eta \oplus \theta^q \rightarrow \theta^k$ are isomorphic, and in $K(X, A)$ we have:
$$\{\xi/\alpha\} - m = \{(\xi \oplus \theta^p)/(\alpha \oplus 1)\} - k = \{(\eta \oplus \theta^q)/(\beta \oplus 1)\} - k = \{\eta/\beta\} - n$$

Thus $\Delta$ is well-defined.
