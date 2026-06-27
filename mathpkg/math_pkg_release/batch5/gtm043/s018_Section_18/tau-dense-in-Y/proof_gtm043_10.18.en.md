---
role: proof
locale: en
of_concept: extension-of-mapping-into-compact-space
source_book: gtm043
source_chapter: "10"
source_section: "18"
---

**Proof of Theorem 10.7.**

It is enough to give the details for $C$. For any $g \in C(Y)$, the function $g \circ \varphi$ belongs to $C(X)$, and hence has an extension to a function $(g \circ \varphi)_0$ in $C(T)$. The mapping $g \rightarrow (g \circ \varphi)_0$ is a homomorphism $t$ of $C(Y)$ into $C(T)$, and it carries $1$ to $1$. By Theorem 10.6, since $Y$ is realcompact, there exists a unique continuous mapping $\overline{\varphi}: T \rightarrow Y$ such that $t = \overline{\varphi}'$, i.e., $(g \circ \varphi)_0 = g \circ \overline{\varphi}$ for all $g \in C(Y)$. For $x \in X$, we have $(g \circ \varphi)_0(x) = g(\varphi x)$, so $g(\overline{\varphi} x) = g(\varphi x)$ for all $g \in C(Y)$. By complete regularity, $\overline{\varphi} x = \varphi x$, so $\overline{\varphi}$ extends $\varphi$. The proof for $C^*$ is analogous, using the compactness of $Y$ in place of realcompactness.
