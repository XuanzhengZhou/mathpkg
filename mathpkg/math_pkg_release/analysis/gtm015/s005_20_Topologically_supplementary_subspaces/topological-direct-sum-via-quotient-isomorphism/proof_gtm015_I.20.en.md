---
role: proof
locale: en
of_concept: topological-direct-sum-via-quotient-isomorphism
source_book: gtm015
source_chapter: "I. Topological Vector Spaces"
source_section: "20. Topologically supplementary subspaces"
---

# Proof of Topological Direct Sum via Quotient Isomorphism

Let $E$ be a TVS and let $M, N$ be supplementary linear subspaces of $E$. Let $\pi: E \to E/M$ be the canonical quotient mapping and let $\pi_0 = \pi|_N: N \to E/M$ be its restriction to $N$.

By Proposition (20.8), $\pi_0$ is a vector space isomorphism and is continuous (as the composition of the continuous inclusion $N \hookrightarrow E$ with the continuous quotient map $\pi$).

**Theorem.** $E$ is the topological direct sum of $M$ and $N$ if and only if $\pi_0$ is bicontinuous (i.e., a TVS isomorphism).

*Proof.* Let $p: E \to E$ be the projector onto $N$ along $M$, defined by $p(y + z) = z$ for $y \in M$, $z \in N$.

($\Rightarrow$) Suppose $E$ is the topological direct sum of $M$ and $N$. Then by Theorem (20.3), the projector $p$ is continuous. We claim that the inverse of $\pi_0$ is given by

$$\pi_0^{-1}(x + M) = p(x) \quad \text{for any representative } x \text{ of the coset } x + M.$$

Indeed, if $x + M = z + M$ for $z \in N$ (the unique $N$-representative guaranteed by $E = M \oplus N$), then $x - z \in M$, and writing the unique decomposition $x = (x - z) + z$ with $x - z \in M$, $z \in N$, we have $p(x) = z = \pi_0^{-1}(x + M)$. Now $\pi_0^{-1}$ can be expressed as the composition

$$E/M \xrightarrow{\sigma} E \xrightarrow{p} N,$$

where $\sigma: E/M \to E$ is any (not necessarily continuous) linear section of the quotient map (e.g., choosing the unique $N$-representative). To verify continuity of $\pi_0^{-1}$, let $W$ be an open set in $N$. Then $W$ is of the form $U \cap N$ for some open $U \subseteq E$. Since $p$ is continuous, $p^{-1}(U \cap N)$ is open in $E$. Because $\pi$ is an open map (quotient maps in TVS are open), we have that the set $\{x + M : p(x) \in U \cap N\}$ is open in $E/M$. But this set is precisely $(\pi_0^{-1})^{-1}(U \cap N)$. Hence $\pi_0^{-1}$ is continuous, and $\pi_0$ is bicontinuous.

($\Leftarrow$) Suppose $\pi_0: N \to E/M$ is bicontinuous. Let $\psi = \pi_0^{-1}: E/M \to N$ be its continuous inverse. Define $q: E \to N$ by $q = \psi \circ \pi$, i.e., $q(x) = \psi(x + M)$. Since both $\pi: E \to E/M$ and $\psi: E/M \to N$ are continuous, $q$ is continuous.

Now for any $x \in E$, write its unique decomposition $x = y + z$ with $y \in M$, $z \in N$. Then $x + M = z + M$, so $q(x) = \psi(z + M) = z$. Thus $q$ is precisely the projector onto $N$ along $M$. By Theorem (20.3), condition (c), the continuity of $q$ (the projection onto $N$) implies that $E$ is the topological direct sum of $M$ and $N$. $\square$
