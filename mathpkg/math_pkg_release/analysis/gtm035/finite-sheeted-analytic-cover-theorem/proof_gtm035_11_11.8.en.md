---
role: proof
locale: en
of_concept: finite-sheeted-analytic-cover-theorem
source_book: gtm035
source_chapter: "11"
source_section: "11.8"
---
# Proof of Finite-Sheeted Analytic Cover Theorem

**Theorem 11.8.** Let $(A, X, \Omega, f)$ be a maximum modulus algebra and let $E \subset \Omega$ be a set of positive logarithmic capacity such that $\# f^{-1}(\lambda) \leq n$ for all $\lambda \in E$. Then

(i) $\# f^{-1}(\lambda) \leq n$ for every $\lambda \in \Omega$;

(ii) there exists a discrete subset $\Lambda$ of $\Omega$ such that $f^{-1}(\Omega \setminus \Lambda)$ admits the structure of a Riemann surface on which every function in $A$ is analytic.

*Proof of (i).* Fix a function $g \in A$. By hypothesis, if $\lambda \in E$, $\# f^{-1}(\lambda) \leq n$; so $\# g(f^{-1}(\lambda)) \leq n$ and hence $d_{n+1}(g(f^{-1}(\lambda))) = 0$. We define

$$\psi(\lambda) = \log d_{n+1}(g(f^{-1}(\lambda)))$$

for $\lambda \in \Omega$. Then $\psi(\lambda) = -\infty$ on $E$. By Theorem 11.7, $\psi$ is subharmonic on $\Omega$. By the theory of subharmonic functions (see Appendix), since the exceptional set $E$ has positive logarithmic capacity, a subharmonic function that equals $-\infty$ on a set of positive capacity must be identically $-\infty$. Hence $\psi \equiv -\infty$, and therefore $d_{n+1}(g(f^{-1}(\lambda))) = 0$ for all $\lambda \in \Omega$.

Now fix $\lambda_0 \in \Omega$. Suppose that $\# f^{-1}(\lambda_0) \geq n + 1$. Because $A$ separates the points of $X$, we may choose $g \in A$ such that the set $g(f^{-1}(\lambda_0))$ contains at least $n + 1$ distinct points. Hence $d_{n+1}(g(f^{-1}(\lambda_0))) \neq 0$, contradicting the previous paragraph. Thus $\# f^{-1}(\lambda) \leq n$ for every $\lambda \in \Omega$, proving assertion (i).

*Proof of (ii).* Define $\Omega_n = \{\lambda \in \Omega : \# f^{-1}(\lambda) = n\}$. We may assume $\Omega_n$ is nonempty (otherwise the statement is vacuous or follows from a similar argument with smaller $n$). Fix $p \in f^{-1}(\Omega_n)$ and let $\lambda_0 = f(p)$. We shall construct a neighborhood of $p$ in $X$ such that $f$ maps this neighborhood one-to-one onto a disk in $\Omega$ centered at $\lambda_0$.

Let $\Delta$ be a small closed disk centered at $\lambda_0$ with $\Delta \subset \Omega$. Using the local maximum modulus principle and the separation properties of $A$, one can find disjoint components $X_1, \ldots, X_n$ of $f^{-1}(\Delta)$ such that each contains exactly one point of $f^{-1}(\lambda_0)$. Standard arguments using the maximum modulus algebra property show that each $X_j$ is mapped by $f$ onto $\Delta$, and $f|_{X_j}$ is one-to-one onto $\operatorname{int}(\Delta)$ (by Corollary 11.3 applied to each sheet).

This provides local coordinates making $f^{-1}(\Omega_n)$ a Riemann surface. Moreover, the functions in $A$, when restricted to each local sheet, are analytic functions of the local coordinate $f$ (again by Corollary 11.3).

It remains to identify the exceptional set $\Lambda = \Omega \setminus \Omega_n$. Fix $g \in A$ that separates the points on generic fibers (i.e., $g$ takes distinct values on distinct points of $f^{-1}(\lambda)$ for $\lambda$ in a dense open set). Consider the discriminant function defined locally: for $\lambda$ in a region where $f^{-1}(\lambda)$ consists of $n$ points $p_1(\lambda), \ldots, p_n(\lambda)$ (given locally as the roots of a monic polynomial equation), set

$$D(\lambda) = \prod_{1 \leq i < j \leq n} (g(p_i(\lambda)) - g(p_j(\lambda)))^2.$$

The function $D$ is single-valued and analytic on $\Omega_n$. Moreover, one can show that $D$ extends continuously to $\Omega$ and vanishes on $\partial \Omega_n = \Omega \setminus \Omega_n$. Specifically, if $\lambda_k \to b$ with $\lambda_k \in \Omega_n$ and $b \in \Omega_s$ for some $s < n$, then as $k \to \infty$, two or more points in the fiber $f^{-1}(\lambda_k)$ must approach the same point in $f^{-1}(b)$, forcing $D(\lambda_k) \to 0$.

Thus $D$ is continuous on $\Omega$ and analytic on $\Omega_n$, vanishing on $\partial \Omega_n$. By Rado's theorem (Theorem 10.9), $D$ is analytic on all of $\Omega$. Hence the zero set $\Lambda = \{\lambda : D(\lambda) = 0\}$ is a discrete subset of $\Omega$, and $\Lambda = \Omega \setminus \Omega_n$. This proves assertion (ii). $\square$
