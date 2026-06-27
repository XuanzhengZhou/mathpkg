---
role: exercise
locale: en
chapter: "II"
section: "7"
exercise_number: 6
---

**The Riemann-Roch Problem.** Let $X$ be a nonsingular projective variety over an algebraically closed field, and let $D$ be a divisor on $X$. For any $n > 0$ we consider the complete linear system $|nD|$. Then the Riemann-Roch problem is to determine $|nD|$ as a function of $n$, and, in particular, its behavior for large $n$. If $\mathcal{L}$ is the corresponding invertible sheaf, then $\dim|nD| = \dim \Gamma(X, \mathcal{L}^n) - 1$, so an equivalent problem is to determine $\dim \Gamma(X, \mathcal{L}^n)$ as a function of $n$.

(a) Show that if $D$ is very ample, and if $X \hookrightarrow \mathbf{P}_k^N$ is the corresponding embedding in projective space, then for all $n$ sufficiently large, $\dim|nD| = P_X(n) - 1$, where $P_X$ is the Hilbert polynomial of $X$ (I, \S 7). Thus in this case $\dim|nD|$ is a polynomial function of $n$, for $n$ large.

(b) If $D$ corresponds to a torsion element of $\operatorname{Pic} X$, of order $r$, then $\dim|nD| = 0$ if $r \nmid n$, and the function is periodic of period $r$ otherwise. In this case the function is periodic of period $r$.

It follows from the general Riemann-Roch theorem that $\dim|nD|$ is a polynomial function for $n$ large, whenever $D$ is an ample divisor. See (IV, 1.3.2), (V, 1.6), and Appendix A. In the case of algebraic surfaces, Zariski has shown for any effective divisor $D$, that there is a finite set of polynomials $P_1, \ldots, P_r$, such that for all $n$ sufficiently large, $\dim|nD| = P_{i(n)}(n)$, where $i(n) \in \{1, 2, \ldots, r\}$ is a function of $n$.
