---
role: proof
locale: en
of_concept: characterization-of-hyperplane
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Equivalent Characterizations of Hyperplanes

Let $E$ be a vector space over $\mathbb{K}$. The following conditions on a subset $H$ of $E$ are equivalent:

**(a)** $H$ is a maximal proper linear variety (i.e., $H$ is a proper linear variety and if $V$ is a linear variety with $H \subset V$, then $V = H$ or $V = E$);

**(b)** $H = z + M$, where $z \in E$ and $M$ is a maximal linear subspace of $E$;

**(c)** $H = \{x \in E : f(x) = \lambda\}$ for some nonzero linear form $f$ on $E$ and some scalar $\lambda \in \mathbb{K}$.

*Proof.*

**(a) $\Rightarrow$ (b):** Say $H = x + M$, where $M$ is a linear subspace. Since $H$ is a proper subset of $E$, so is $M$. Suppose $N$ is a linear subspace such that $M \subset N$; it is to be shown that $N = M$ or $N = E$. Since $x + N$ is a linear variety and $x + N \supset x + M = H$, it follows from the maximality of $H$ that $x + N = E$ or $x + N = x + M$, that is, $N = E$ or $N = M$.

**(b) $\Rightarrow$ (c):** Assume $H = z + M$, where $M$ is a maximal linear subspace. By Theorem 21.3, there exists a nonzero linear form $f$ with null space $M$. Set $\lambda = f(z)$. Then

$$\{x \in E : f(x) = \lambda\} = \{x \in E : f(x) = f(z)\} = \{x \in E : f(x - z) = 0\}$$
$$= \{x \in E : x - z \in M\} = M + z = H.$$

**(c) $\Rightarrow$ (a):** Suppose $H = \{x \in E : f(x) = \lambda\}$, where $f$ is a nonzero linear form and $\lambda \in \mathbb{K}$. Let $M$ be the null space of $f$ and choose any $z \in H$. Then $H = z + M$ by an argument similar to that in the preceding paragraph (since $f(z) = \lambda$ and $f(x) = \lambda \iff f(x - z) = 0$). Since $M$ is a maximal linear subspace by Theorem 21.3, it follows that $H$ is a maximal proper linear variety (any variety containing $z + M$ would correspond to a subspace containing $M$, which must be $M$ or $E$).

**Uniqueness.** Finally, suppose $H = \{x \in E : f(x) = \lambda\} = \{x \in E : g(x) = \mu\}$, where $\lambda, \mu \in \mathbb{K}$ and $f, g$ are nonzero linear forms. Choose $u \in H$ and let $M$ be the null space of $f$; as noted above, $H = u + M$. Similarly, if $N$ is the null space of $g$, then $H = u + N$. By Lemma 21.5, $M = N$ and $u - u = 0 \in M = N$. Thus $f$ and $g$ have the same null space, so by the uniqueness statement in Theorem 21.3, $g = \rho f$ for some nonzero $\rho \in \mathbb{K}$, and $\mu = g(u) = \rho f(u) = \rho \lambda$.
