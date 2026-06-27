---
role: proof
locale: en
of_concept: injectivity-lemma-immersions
source_book: gtm033
source_chapter: "2. Function Spaces"
source_section: "2.1"
---

# Proof of Local Injectivity Lemma for Immersions

**Lemma.** Let $f: U \to \mathbb{R}^m$ be a $C^1$ immersion, where $U \subset \mathbb{R}^n$ is an open set. Let $W \subset U$ be an open set with compact closure $\bar{W} \subset U$. Then there exists $\varepsilon > 0$ such that any $C^1$ map $g: U \to \mathbb{R}^m$ satisfying

$$\|Dg(x) - Df(x)\| < \varepsilon \quad \text{and} \quad |g(x) - f(x)| < \varepsilon$$

for all $x \in W$ is injective on $W$.

*Proof.* Suppose the lemma is false. Then there exists a sequence $g_n \in C^1(U, \mathbb{R}^m)$ such that

$$\|Dg_n(x) - Df(x)\| \to 0$$

and

$$|g_n(x) - f(x)| \to 0$$

uniformly on $W$, while for each $n$ there exist distinct points $a_n, b_n$ in $W$ with $g_n(a_n) = g_n(b_n)$. By compactness of $\bar{W}$ we may assume $a_n \to a \in U$, $b_n \to b \in U$ as $n \to \infty$. Then $f(a) = f(b)$ by the uniform convergence of $g_n$ to $f$, so $a = b$ since $f$ is an immersion (hence locally injective).

Choosing subsequences if necessary we may assume that the sequence of unit vectors

$$v_n = \frac{a_n - b_n}{|a_n - b_n|}$$

converges to a unit vector $v \in S^{n-1}$. By uniformity of Taylor expansion we have

$$\frac{|g_n(a_n) - g_n(b_n) - Df(b_n)(a_n - b_n)|}{|a_n - b_n|} \to 0.$$

Since $g_n(a_n) = g_n(b_n)$, this implies $Df(b_n)v_n \to 0$. But this sequence also converges to $Df(b)v$, which therefore is $0$. This contradicts the assumption that $f$ is an immersion (i.e., $Df(b)$ is injective, so $Df(b)v = 0$ implies $v = 0$, contradicting $|v| = 1$).

$\square$

**Remark.** This lemma is crucial for the proof of Theorem 1.4 (openness of embeddings in the strong topology), as it provides local injectivity for maps sufficiently close to an immersion in the $C^1$ sense.
