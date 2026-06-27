---
role: proof
locale: en
of_concept: lusin-theorem-for-baire-measures
source_book: gtm018
source_chapter: "55"
source_section: "55. Classes of Continuous Functions"
---

We prove the theorem in two stages: first for simple Baire functions, then for general Baire functions.

**Stage 1: Simple Baire functions.** Let $f = \sum_{i=1}^{n} \alpha_i \chi_{E_i}$ be an integrable simple Baire function, where the $E_i$ are disjoint Baire sets and $\alpha_i \neq 0$. Choose $c > 0$ such that $|\alpha_i| \leq c$ for all $i$. Given $\varepsilon > 0$, the regularity of the Baire measure $\mu_0$ implies that for each $i = 1, \ldots, n$, there exists a compact Baire set $C_i$ such that

$$C_i \subset E_i \quad \text{and} \quad \mu_0(E_i) \leq \mu_0(C_i) + \frac{\varepsilon}{nc}.$$

Since the $E_i$ are disjoint, we may take the $C_i$ to be disjoint as well (by passing to $C_i \setminus \bigcup_{j \neq i} C_j$, which remains a compact Baire set). Set $g = \sum_{i=1}^{n} \alpha_i \chi_{C_i}$. Then

$$\int |f - g| \, d\mu_0 = \sum_{i=1}^{n} |\alpha_i| \, \mu_0(E_i - C_i) \leq \sum_{i=1}^{n} c \cdot \frac{\varepsilon}{nc} = \varepsilon.$$

Moreover, each $C_i$ is compact and the $C_i$ are disjoint, so $g$ (and hence $f$) restricted to $C = \bigcup_{i=1}^{n} C_i$ is continuous (each $C_i$ is both relatively open and closed in $C$, and $g$ is constant on each $C_i$). Thus we have found a compact Baire set $C$ (the union of the $C_i$) such that $f$ is continuous on $C$ and $\mu_0(E - C)$ is controlled. This establishes the theorem for simple Baire functions.

**Stage 2: General Baire functions.** Now let $f$ be an arbitrary Baire function on a Baire set $E$ with $\mu_0(E) < \infty$. There exists a sequence $\{f_n\}$ of simple Baire functions converging pointwise to $f$ on $E$. Given $\varepsilon > 0$, apply Egoroff's theorem and the regularity of $\mu_0$: there exists a compact Baire set $C_0 \subset E$ such that

$$\mu_0(E) \leq \mu_0(C_0) + \frac{\varepsilon}{2}$$

and such that $\{f_n\}$ converges to $f$ uniformly on $C_0$.

Now, for each $n$, since $f_n$ is a simple Baire function, by Stage 1 there exists a compact Baire set $C_n \subset E$ such that

$$\mu_0(E) \leq \mu_0(C_n) + \frac{\varepsilon}{2^{n+1}}$$

and such that $f_n$ is continuous on $C_n$ (more precisely, we apply Stage 1 to obtain a compact Baire subset of $E$ on which $f_n$ is continuous and whose complement has measure at most $\varepsilon/2^{n+1}$; we then intersect with a set of full measure to ensure the continuity property holds on $C_n$ with the measure bound).

Define

$$C = \bigcap_{n=0}^{\infty} C_n.$$

Then $C$ is a compact Baire set with $C \subset E$, and

$$\mu_0(E - C) = \mu_0\left(\bigcup_{n=0}^{\infty} (E - C_n)\right) \leq \sum_{n=0}^{\infty} \mu_0(E - C_n) \leq \frac{\varepsilon}{2} + \sum_{n=1}^{\infty} \frac{\varepsilon}{2^{n+1}} = \varepsilon.$$

On $C$, each $f_n$ is continuous (being the restriction of a continuous function to $C$) and $f_n \to f$ uniformly. Since the uniform limit of continuous functions is continuous, $f$ is continuous on $C$. This completes the proof.

This result is known as **Lusin's theorem**.
