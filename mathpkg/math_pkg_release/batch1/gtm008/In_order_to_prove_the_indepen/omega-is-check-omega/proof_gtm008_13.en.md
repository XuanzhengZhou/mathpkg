---
role: proof
locale: en
of_concept: omega-is-check-omega
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The defining formula for $\omega$ in $ZF$ is:
$$\omega = a \leftrightarrow \varphi(a)$$
where $\varphi(a)$ is:
$$0 \in a \land (\forall x \in a)[x + 1 \in a] \land (\forall y)[0 \in y \land (\forall x \in y)[x + 1 \in y] \rightarrow a \subseteq y].$$

We verify that $\check{\omega}$ satisfies $\varphi$ with Boolean value $1$:

- $[\![0 \in \check{\omega}]\!] = 1$ (Example 1 and the definition of $\check{\omega}$).
- $[\![(\forall x \in \check{\omega})[x + 1 \in \check{\omega}]\!] = \prod_{n \in \omega} [\![\check{n} + 1 \in \check{\omega}]\!] = \prod_{n \in \omega} [\![(\widehat{n + 1}) \in \check{\omega}]\!] = 1$ (by Example 2 and the definition of $\check{\omega}$).
- By Example 5, $[\![0 \in y \land (\forall x \in y)[x + 1 \in y] \rightarrow \check{\omega} \subseteq y]\!] = 1$ for any $y \in V^{(B)}$.

Combining these, $[\![\varphi(\check{\omega})]\!] = 1$, and since $\omega$ is the unique set satisfying $\varphi$ in $ZF$ (and $V^{(B)}$ is a model of $ZF$ by Theorem 13.12), we have $[\![\omega = \check{\omega}]\!] = 1$.
