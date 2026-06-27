---
role: proof
locale: en
of_concept: banach-steinhaus-theorem
source_book: gtm015
source_chapter: "V"
source_section: "47"
---

# Proof of the Banach-Steinhaus Theorem

Let $E$ be a Banach space, $F$ a normed space, and let $(T_n)$ be a sequence of continuous linear mappings from $E$ to $F$. Assume that $\lim_{n \to \infty} T_n x = T x$ exists for every $x \in E$. In view of (43.1), it will suffice to show that $T$ is linear and continuous.

**Linearity.** For $x_1, x_2 \in E$,
$$T(x_1 + x_2) = \lim_{n \to \infty} T_n(x_1 + x_2) = \lim_{n \to \infty} (T_n x_1 + T_n x_2) = \lim_{n \to \infty} T_n x_1 + \lim_{n \to \infty} T_n x_2 = T x_1 + T x_2.$$
Similarly $T(\lambda x) = \lambda T(x)$. Thus $T$ is linear.

**Continuity.** Since $T_n x$ converges for each $x$, the sequence $(T_n x)$ is bounded for each $x \in E$. By the Uniform Boundedness Principle (47.1), the family $(T_n)$ is uniformly bounded: there exists $C > 0$ such that $\|T_n\| \leq C$ for all $n$. Then for any $x \in E$,
$$\|T x\| = \lim_{n \to \infty} \|T_n x\| \leq \liminf_{n \to \infty} \|T_n\| \|x\| \leq C \|x\|,$$
so $T$ is continuous with $\|T\| \leq C$. $\square$
