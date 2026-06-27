---
role: proof
locale: en
of_concept: one-dimensional-hausdorff-tvs-isomorphism
source_book: gtm003
source_chapter: "1"
source_section: "3.1"
---

It follows from $(LT)_2$ that $\lambda \mapsto \lambda x_0$ is continuous; moreover, this mapping is an algebraic isomorphism of $K$ onto $L$. Its inverse is the mapping $x \mapsto f(x)$ where $f$ is the unique linear form on $L$ satisfying $f(x_0) = 1$. Since $L$ is Hausdorff, the kernel of $f$ is $\{0\}$, hence $f$ is a bijection. To show $f$ is continuous, let $U$ be a neighborhood of $0$ in $K$. Since scalar multiplication is continuous, there exists a circled neighborhood $V$ of $0$ in $L$ such that $\lambda \in V$ implies $|\lambda| < \varepsilon$; then $f(V) \subset U$. Thus $f$ is continuous at $0$, hence everywhere. Therefore $\lambda \mapsto \lambda x_0$ is a homeomorphism and a linear bijection, i.e., an isomorphism of t.v.s. Every isomorphism $\phi: K_0 \to L$ satisfies $\phi(\lambda) = \lambda \phi(1)$, so setting $x_0 = \phi(1)$ shows every isomorphism is of the form $\lambda \mapsto \lambda x_0$.
