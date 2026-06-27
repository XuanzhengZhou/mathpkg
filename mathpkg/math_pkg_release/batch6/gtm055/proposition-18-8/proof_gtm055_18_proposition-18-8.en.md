---
role: proof
locale: en
of_concept: proposition-18-8
source_book: gtm055
source_chapter: "18"
source_section: "Section 19_Section_19"
---

Proof. According to Problem 1D it suffices to verify that if $f \in A$, then $|f| \in A$ also. To establish the latter assertion observe that if we set $q_n(t) = p_n(1 - t)$, where $\{p_n(t)\}$ is a sequence of real polynomials converging uniformly to $\sqrt{1 - t}$ on the interval $[0, 1]$, then the sequence $\{q_n(t)\}$ converges uniformly to the function $\sqrt{t}$ on $[0, 1]$. In particular, if $a_n = q_n(0)$, then $a_n \to 0$. Hence if $r_n(t) = q_n(t) - a_n$, then the sequence of polynomials $\{r_n(t)\}$ also converges uniformly to $\sqrt{t}$ on $[0, 1]$, and each $r_n$ has zero constant term. Note that $r_n \circ f \in A$ whenever $f \in A$ by virtue of the fact that $r_n(0) = 0$.

Suppose now that $f$ is a nonzero element of $A$. Set $g(x) = \left(f(x) / \|f\|_\infty\right)^2$ for all $x$ in $X$, and observe that $g$ belongs to $A$ and that the sequence $\{r_n \circ g\}$ does so too. But this latter sequence converges uniformly on $X$ to the limit $\sqrt{g} = |f| / \|f\|_\infty$, whence it follows at once that $|f|$ belongs to $A$.
