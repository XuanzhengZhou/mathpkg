---
role: proof
locale: en
of_concept: perturbed-stone-weierstrass-polynomial-sequence
source_book: gtm035
source_chapter: "14"
source_section: "14.1"
---
# Proof of Polynomial Sequence for Perturbed Stone-Weierstrass

Let $S$ be a closed semidisk contained in the closed right half-plane $\{\operatorname{Re} w \geq 0\}$. For each integer $n \geq 1$, we construct a polynomial $P_n$ such that the sequence $\{P_n\}$ satisfies the approximation properties required in Lemma 14.2.

**Construction.** Consider the function $w \mapsto 1/(w + 1/n)$ on $S$. Since $\operatorname{Re}(w + 1/n) > 0$ on $S$, this function is holomorphic on a neighborhood of $S$. By Runge's approximation theorem (or Mergelyan's theorem, since $S$ is compact with connected complement), there exists a polynomial $P_n$ in $w$ such that
$$
\left| P_n(w) - \frac{1}{w + \frac{1}{n}} \right| < \frac{1}{n}, \quad \forall w \in S.
$$

**Verification for Lemma 14.2.** For any $w \in S \setminus \{0\}$,
$$
|w P_n(w)|
= |w| \left| P_n(w) - \frac{1}{w + \frac{1}{n}} + \frac{1}{w + \frac{1}{n}} \right|
\leq |w| \left| P_n(w) - \frac{1}{w + \frac{1}{n}} \right| + \left| \frac{w}{w + \frac{1}{n}} \right|.
$$

The first term is bounded by $|w|/n \leq r_0/n$ where $r_0$ is the radius of the semidisk $S$. The second term satisfies $\left|\frac{w}{w + 1/n}\right| < 1$ since $|w| < |w + 1/n|$ for $\operatorname{Re} w > 0$ (this follows from $\operatorname{Re}(1/n) = 1/n > 0$, which adds to the real part of the denominator).

Thus $|w P_n(w)| \leq r_0 + 1 = C$, which is the uniform estimate used in Lemma 14.2.

Moreover, for fixed $w \in S \setminus \{0\}$,
$$
\lim_{n \to \infty} P_n(w) = \lim_{n \to \infty} \frac{1}{w + 1/n} = \frac{1}{w},
$$
since $P_n$ uniformly approximates $1/(w + 1/n)$ on $S$ with error at most $1/n$.

Hence the polynomials $P_n$ satisfy both conditions needed for the proof of Lemma 14.2 and ultimately for the perturbation theorems that follow.

$\square$
