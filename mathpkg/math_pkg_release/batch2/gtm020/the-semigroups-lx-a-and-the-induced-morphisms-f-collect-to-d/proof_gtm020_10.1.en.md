---
locale: en
of_concept: the-semigroups-lx-a-and-the-induced-morphisms-f-collect-to-d
role: proof
source_book: gtm020
source_chapter: 10. Relative K-Theory
source_section: '1'
---

For the first statement, each difference isomorphism $\alpha: \xi_0 \rightarrow \xi_1$ is equivalent in $L(X, A)$ to $\alpha \oplus 1: \xi_0 \oplus \zeta \rightarrow \xi_1 \oplus \zeta$. If $\zeta$ has the property that $\xi_1 \oplus \zeta$ and $\theta^m$ are isomorphic, the property $\Delta([\alpha: \xi_0 \rightarrow \xi_1]) = \{(\xi_0 \oplus \zeta)/(\alpha \oplus 1)\} - m$ proves that $\Delta$ is uniquely defined. To prove that this relation can serve as a definition of $\Delta$, we consider $[\alpha: \xi \rightarrow \theta^m] = [\beta: \eta \rightarrow \theta^n]$. There exist vector bundles $\zeta_1$ and $\zeta_2$ with $\alpha \oplus 1: \xi \oplus \zeta_1 \rightarrow \theta^m \oplus \zeta_1$ isomorphic to $\beta \oplus 1: \eta \oplus \zeta_2 \rightarrow \theta^n \oplus \zeta_2$. Since $\zeta_1$ and $\zeta_2$ are $s$-equivalent, there exists a vector bundle $\zeta$ with $\zeta_1 \oplus \zeta$ isomorphic to $\theta^p$, $\zeta_2 \oplus \zeta$ isomorphic to $\theta^q$, and $m + p = n + q = k$. Then $\alpha \oplus 1: \xi \oplus \theta^p \rightarrow \theta^k$ and $\beta \oplus 1: \eta \oplus \theta^q \rightarrow \theta^k$ are isomorphic, and in $K(X, A)$ we have $\{\xi/\alpha\} - m = \{(\xi \oplus \theta^p)/(\alpha \oplus 1)\} - k = \{(\eta \oplus \theta^q)/(\beta \oplus 1)\} - k = \{\eta/\beta\

riemannian metric on $\xi_0$ and $\xi_1$ defined fibrewise, then in $L(X, A)$ we have $[\alpha: \xi_0 \rightarrow \xi_1] = -[\beta: \xi_1 \rightarrow \xi_0]$.

Proof. The result is true for $A = \phi$ or $A =$ point by a direct inspection. In general, we use the natural isomorphism $L(X/A, *) \rightarrow L(X, A)$ given by the commutative diagram of isomorphisms.

$$\begin{array}{ccc}
L(X/A, *) & \xrightarrow{\Delta} & K(X/A, *) \\
\downarrow & & \downarrow \\
L(X, A) & \xrightarrow{\Delta} & K(X, A)
\end{array}$$

6. Products in $L(X, A)$

We make use of the following lemma on vector spaces which is a special case of the Künneth formula.
