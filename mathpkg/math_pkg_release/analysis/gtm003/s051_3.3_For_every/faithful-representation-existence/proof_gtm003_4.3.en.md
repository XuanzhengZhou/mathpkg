---
role: proof
locale: en
of_concept: faithful-representation-existence
source_book: gtm003
source_chapter: "4"
source_section: "4.3"
---

Since the state space $S(A)$ separates $A$ (by the Lemma preceding 4.2), we "paste" the representations $\pi_{\phi}$ ($\phi \in S(A)$) together. Precisely, let $H$ denote the Hilbert direct sum $\bigoplus_{\phi \in S(A)} H_{\phi}$ (Chapter II, Section 3, Example 5) and define a representation $\pi : A \rightarrow \mathcal{L}(H)$ by $\pi(x) = \bigoplus_{\phi \in S(A)} \pi_{\phi}(x)$, where the operator $\pi(x) \in \mathcal{L}(H)$ acts coordinatewise on the elements $(\eta_{\phi})_{\phi \in S(A)}$ of $H$.

For each $\phi \in S(A)$, one constructs $H_\phi$ as the completion of $A/A_\phi$ with inner product induced by $[x, y]_\phi = \phi(y^*x)$. The representation $\pi_\phi$ on $H_\phi$ is given by left multiplication. The direct sum representation $\pi$ is faithful because if $\pi(x) = 0$, then $\pi_\phi(x) = 0$ for all $\phi$, implying $\phi(x^*x) = 0$ for all states $\phi$. Since $S(A)$ separates points, $x = 0$.
