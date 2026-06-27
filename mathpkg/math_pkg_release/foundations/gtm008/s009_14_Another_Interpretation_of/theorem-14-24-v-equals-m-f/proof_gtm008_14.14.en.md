---
role: proof
locale: en
of_concept: theorem-14-24-v-equals-m-f
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

$V = M[F]$ can be written as a formula $(\forall x)\varphi(M(x), F)$ where $\varphi$ is a formula of $\mathcal{L}_0$.

Suppose $[[V = M[F]]] \neq 1$ in $\mathbf{V}^{(B)}$. Then there exists an $N$ (a countable transitive model of a sufficiently large fragment of ZF) such that in $(V^{(B)})^N$,
$$b = [[V = M[F_N]]] \neq 1.$$

By the same reasoning as in Corollary 14.23, there exists an $N$-complete homomorphism $h: |\mathbf{B}| \to |2|$ such that $h(b) = 0$. Let $G = h(F_N)$. Then in $N[G]$,
$$N[G] \models \neg(\forall x)\varphi(M(x), G),$$
which means that $V \neq N[G]$ in $N[G]$. But since $M(x)$ is interpreted as $x \in N$ in $N[G]$, and $N[G]$ is a model of ZF, $V = N[G]$ is true in $N[G]$ (by the definition of $N[G]$ as the generic extension). This is a contradiction.

Therefore $[[V = M[F]]] = 1$ in $\mathbf{V}^{(B)}$.
