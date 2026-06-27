---
role: proof
locale: en
of_concept: open-mapping-theorem
source_book: gtm015
source_chapter: "V"
source_section: "48"
---

# Proof of the Open Mapping Theorem

Let $T: E \to F$ be a surjective continuous linear mapping, where $E$ and $F$ are metrizable, complete TVS. $E$ and $F$ may be metrized with additively invariant metrics, relative to which they are complete metric spaces (7.9).

The proof proceeds in two steps.

**Step 1 (Key Lemma, 48.2).** If $W$ is any neighborhood of $\theta$ in $E$, then $\overline{T(W)}$ is a neighborhood of $\theta$ in $F$.

*Proof of Step 1.* Let $V$ be a neighborhood of $\theta$ in $E$. Choose a balanced neighborhood $W$ of $\theta$ such that $W + W \subset V$ and fix $\lambda$ with $|\lambda| > 1$. Then $E = \bigcup_{n=1}^{\infty} \lambda^n W$ (since for any $x$, $\mu x \in W$ for some $\mu$, and choosing $n$ with $|\lambda^{-n}\mu^{-1}| \leq 1$ gives $\lambda^{-n}x \in W$, so $x \in \lambda^n W$ by balancedness). Surjectivity and linearity of $T$ give $F = \bigcup_{1}^{\infty} \lambda^n T(W)$. Since $F$ is a Baire space (46.6), $\overline{\lambda^m T(W)}$ has nonempty interior for some $m$, hence $\overline{T(W)}$ has nonempty interior. Let $A = \operatorname{int}(\overline{T(W)})$. By symmetry, $-A = A$, so $\theta \in A + A \subset \overline{T(W)} + \overline{T(W)} \subset \overline{T(W+W)} \subset \overline{T(V)}$. Since $A+A$ is open, $\overline{T(V)}$ is a neighborhood of $\theta$.

**Step 2 (Successive Approximations Lemma, 48.3).** For each $r > 0$ there exists $\rho > 0$ such that $B_\rho(Tx) \subset \overline{T(B_r(x))}$ for all $x \in E$. Moreover, for any $a > r$, $B_\rho(Tx) \subset T(B_a(x))$ for all $x \in E$.

*Proof of Step 2.* The hypothesis $B_\rho(Tx) \subset \overline{T(B_r(x))}$ follows from Step 1 applied to the ball $B_r(\theta)$ (using translation invariance). The second claim is the successive approximations argument (48.3(i)): write $a = \sum r_n$ with $r_n > 0$, $r_1 = r$, construct a sequence $x_n$ with $x_n \in B_{r_n}(x_{n-1})$ and $d(Tx_n, y) \to 0$, then the limit $x = \lim x_n$ satisfies $Tx = y$ and $d(x_0, x) \leq \sum r_n = a$.

**Conclusion.** By Step 2(ii), $T$ is an open mapping: for any open $U \subset E$ and $x \in U$, choose $r$ with $B_r(x) \subset U$; Step 2 produces $\rho$ with $B_\rho(Tx) \subset T(B_r(x)) \subset T(U)$, showing $T(U)$ is open. $\square$
