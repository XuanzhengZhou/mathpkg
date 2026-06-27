---
role: proof
locale: en
of_concept: approximation-of-simple-function-by-l-functions
source_book: gtm018
source_chapter: "55"
source_section: "55. Classes of Continuous Functions"
---

Let $g = \sum_{i=1}^{n} \alpha_i \chi_{C_i}$, where the $C_i$ are disjoint compact Baire sets. (If the $C_i$ are not disjoint, we may first rewrite $g$ in terms of a disjoint partition by considering all Boolean combinations of the $C_i$, which remain compact Baire sets.)

Since $\{C_1, \ldots, C_n\}$ is a finite disjoint class of compact sets, there exists a finite disjoint class $\{U_1, \ldots, U_n\}$ of bounded open Baire sets such that $C_i \subset U_i$ for $i = 1, \ldots, n$. By the regularity of the Baire measure $\mu_0$, we may (and do) assume, without loss of generality, that

$$\mu_0(U_i) \leq \mu_0(C_i) + \frac{\varepsilon}{nc}, \quad i = 1, \ldots, n,$$

where $c > 0$ is a number such that $|g(x)| \leq c$ for every $x \in X$ (for instance, $c = \max_i |\alpha_i|$).

For each $i = 1, \ldots, n$, the compact set $C_i$ and the closed set $X - U_i$ are disjoint. By Urysohn's lemma (more precisely, by the existence of functions in $\mathcal{L}$ separating compact sets from closed sets, cf. §50), there exists a function $h_i \in \mathcal{L}$ such that

$$h_i(x) = 1 \text{ for } x \in C_i, \quad h_i(x) = 0 \text{ for } x \in X - U_i, \quad \text{and} \quad 0 \leq h_i(x) \leq 1 \text{ for all } x.$$

Define $h = \sum_{i=1}^{n} \alpha_i h_i$. Since each $h_i \in \mathcal{L}$, we have $h \in \mathcal{L}$. Now estimate:

$$\int |g - h| \, d\mu_0 = \int \left| \sum_{i=1}^{n} \alpha_i (\chi_{C_i} - h_i) \right| d\mu_0.$$

Since the $U_i$ are disjoint and $\chi_{C_i} - h_i$ vanishes outside $U_i$, the supports of the summands are disjoint, so

$$\int |g - h| \, d\mu_0 \leq \sum_{i=1}^{n} |\alpha_i| \int |\chi_{C_i} - h_i| \, d\mu_0.$$

On $C_i$, we have $h_i = 1 = \chi_{C_i}$, so $|\chi_{C_i} - h_i| = 0$. On $U_i - C_i$, we have $\chi_{C_i} = 0$ and $0 \leq h_i \leq 1$, so $|\chi_{C_i} - h_i| = |h_i| \leq 1$. Hence

$$\int |\chi_{C_i} - h_i| \, d\mu_0 \leq \mu_0(U_i - C_i) = \mu_0(U_i) - \mu_0(C_i) \leq \frac{\varepsilon}{nc}.$$

Therefore,

$$\int |g - h| \, d\mu_0 \leq \sum_{i=1}^{n} |\alpha_i| \cdot \frac{\varepsilon}{nc} \leq \sum_{i=1}^{n} c \cdot \frac{\varepsilon}{nc} = \varepsilon.$$

This completes the proof.
