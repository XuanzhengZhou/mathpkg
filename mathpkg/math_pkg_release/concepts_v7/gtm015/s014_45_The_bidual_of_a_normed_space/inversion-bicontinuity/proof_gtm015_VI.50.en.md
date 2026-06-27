---
role: proof
locale: en
of_concept: inversion-bicontinuity
source_book: gtm015
source_chapter: "VI"
source_section: "50"
---

# Proof that Inversion is Bicontinuous in a Banach Algebra

Let $A$ be a Banach algebra with unity, $U$ the group of invertible elements. The mapping $j: U \to U$, $j(x) = x^{-1}$ is to be shown bicontinuous.

Since $j$ is involutory ($j(j(x)) = (x^{-1})^{-1} = x$), it suffices to prove that $j$ is continuous at each point of $U$. Let $x \in U$ and let $(x_n)$ be a sequence in $U$ with $\|x_n - x\| \to 0$. We must show $\|x_n^{-1} - x^{-1}\| \to 0$.

First, note that since $\|x_n - x\| \to 0$, the sequence $(x_n)$ is bounded. Also, for sufficiently large $n$, $\|x_n - x\| < \|x^{-1}\|^{-1}$, so by (50.5), $x_n$ lies in the open ball centered at $x$ of radius $\|x^{-1}\|^{-1}$, which is contained in $U$.

Write
$$x_n^{-1} - x^{-1} = x_n^{-1}(x - x_n)x^{-1}.$$

Then
$$\|x_n^{-1} - x^{-1}\| \leq \|x_n^{-1}\|\|x - x_n\|\|x^{-1}\|.$$

It remains to show that $\|x_n^{-1}\|$ is bounded as $n \to \infty$. Since $x_n \to x$, we have $x_n x^{-1} \to 1$. For $n$ large enough, $\|1 - x_n x^{-1}\| < 1/2$, so by (50.2), $x_n x^{-1}$ is invertible with $\|(x_n x^{-1})^{-1}\| \leq \frac{1}{1 - 1/2} = 2$. But $(x_n x^{-1})^{-1} = x x_n^{-1}$, so $\|x_n^{-1}\| \leq \|x x_n^{-1}\|\|x^{-1}\| \leq 2\|x^{-1}\|$. Thus $\|x_n^{-1}\|$ is uniformly bounded.

Therefore $\|x_n^{-1} - x^{-1}\| \leq C \|x_n - x\| \to 0$, proving continuity of $j$. Since $j^{-1} = j$, the map is a homeomorphism, and $U$ is a topological group. $\square$
