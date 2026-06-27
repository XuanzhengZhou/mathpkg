---
role: proof
locale: en
of_concept: kaplansky-density-theorem
source_book: gtm003
source_chapter: "VI"
source_section: "7"
---

All topological statements refer to the strong operator topology of $\mathcal{L}(H)$ unless stated otherwise.

**(a)** From a combined application of (6.1), its corollary, and (6.2), the linear projection $x \mapsto \frac{1}{2}(x + x^*)$ mapping $\mathcal{L}(H)$ onto $\mathcal{L}(H)_{sa}$ is continuous for the weak operator topology. Hence, $A_{sa}$ is dense in $M_{sa}$ for that topology. Since $A_{sa}$ is convex, it is also dense in $M_{sa}$ for the strong operator topology by the Hahn-Banach theorem (IV, 3.1), as convex sets have the same closure in both topologies.

**(b)** Let $a \in U_M \cap M_{sa}$. By (a), there exists a filter $\mathfrak{F}$ on $A_{sa}$ converging strongly to $a$. Define $f(t) = \sup(-1, \inf(t, 1))$ for $t \in \mathbb{R}$. The function $f$ is bounded, continuous, and satisfies $|f(t)| \leq 1$ with $f(t) = t$ for $t \in [-1, 1]$. Since $f$ is strongly continuous by Theorem 7.3, the net $f(x_\alpha)$ (for $x_\alpha$ in the filter) lies in $U_A \cap A_{sa}$ and converges strongly to $f(a) = a$, because $\|a\| \leq 1$ implies $f(a) = a$ via the functional calculus.

**(c)** For any $a \in U_M$, use the $2 \times 2$ matrix trick: embed $M$ into $M_2(M) = M \otimes M_2(\mathbb{C}) \subset \mathcal{L}(H \oplus H)$. The element $\begin{pmatrix} 0 & a \\ a^* & 0 \end{pmatrix}$ is self-adjoint with norm $\leq 1$. Apply (b) to approximate it by elements in $U_{M_2(A)} \cap M_2(A)_{sa}$, then project to the $(1,2)$-entry to obtain an approximation of $a$ by elements of $U_A$.

**(d)** If $A$ is unital, let $u \in G_M$. By Lemma 1, $u = \exp(iv)$ for some self-adjoint $v \in M$. By (b), approximate $v$ by a bounded net $(v_\alpha)$ in $U_A \cap A_{sa}$, then $\exp(iv_\alpha) \in G_A$ approximates $u$ by continuity of the functional calculus (Theorem 7.3 applied to $t \mapsto \exp(it)$).
