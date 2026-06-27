---
role: proof
locale: en
of_concept: runges-theorem
source_book: gtm011
source_chapter: "VIII"
source_section: "1.7"
---

The proof, due to S. Grabiner (Amer. Math. Monthly, 83 (1976), 807-808), reformulates the problem in a functional-analytic setting. On the space $C(K, \mathbb{C})$ of continuous functions on $K$, define the metric
$$\rho(f, g) = \sup \{ |f(z) - g(z)| : z \in K \},$$
which makes $C(K, \mathbb{C})$ a complete metric space where $\rho(f_n, f) \to 0$ iff $f_n \to f$ uniformly on $K$. Runge's Theorem then asserts: if $f$ is analytic on a neighborhood of $K$, then $f$ belongs to the $\rho$-closure of rational functions with poles in $E$.

Define $B(E)$ as the set of all functions $f \in C(K, \mathbb{C})$ that are uniform limits on $K$ of rational functions with poles in $E$. $B(E)$ is a closed subalgebra of $C(K, \mathbb{C})$ containing the constant functions. The goal is to show that every function analytic on a neighborhood of $K$ lies in $B(E)$.

The key lemma (Lemma 1.10) shows that for any $a \in \mathbb{C} - K$, the function $(z-a)^{-1} \in B(E)$. The proof of Lemma 1.10 proceeds by:

1. Defining $V = \{a \in \mathbb{C} : (z-a)^{-1} \in B(E)\}$ and showing $E \subset V \subset \mathbb{C} - K$.

2. Proving $V$ is open: If $a \in V$ and $|b-a| < d(a, K)$, then for all $z \in K$,
$$(z-b)^{-1} = (z-a)^{-1} \left[ 1 - \frac{b-a}{z-a} \right]^{-1} = (z-a)^{-1} \sum_{n=0}^{\infty} \left( \frac{b-a}{z-a} \right)^n,$$
where the geometric series converges uniformly on $K$ by the Weierstrass M-test (since $|b-a|/|z-a| < 1$). The partial sums are rational functions with poles in $V \subset E$-pole set, and since $B(E)$ is a closed algebra, the limit $(z-b)^{-1} \in B(E)$. Hence $b \in V$.

3. Showing $V$ is also closed in $\mathbb{C} - K$, which forces $V = \mathbb{C} - K$. Thus $(z-a)^{-1} \in B(E)$ for every $a$ outside $K$.

With Lemma 1.10 established, one applies the Cauchy integral formula (Proposition 1.1) to represent $f(z)$ for $z \in K$ as a finite sum of integrals over line segments $\gamma_k \subset G - K$. Each such integral is approximated by Riemann sums (Lemma 1.5), yielding rational functions with poles on the $\gamma_k$, which lie in $\mathbb{C} - K$ and therefore in $E$ after suitable adjustment. The closed algebra property of $B(E)$ then implies $f \in B(E)$, completing the proof.
