---
role: proof
locale: en
of_concept: isolated-primary-components-are-unique
source_book: gtm028
source_chapter: "IV"
source_section: "§5. Uniqueness theorems"
---

If $x \in \mathfrak{a}'_i$, then $yx \in \mathfrak{a}'_i$ for all $y \in R$. If $x_1, x_2 \in \mathfrak{a}'_i$, there exist $\pi_1, \pi_2 \notin \mathfrak{p}_i$ with $\pi_1 x_1, \pi_2 x_2 \in \mathfrak{a}$. Then $\pi_1\pi_2(x_1 - x_2) \in \mathfrak{a}$ and $\pi_1\pi_2 \notin \mathfrak{p}_i$ (since $\mathfrak{p}_i$ is prime), so $x_1 - x_2 \in \mathfrak{a}'_i$. Thus $\mathfrak{a}'_i$ is an ideal.

If $x \in \mathfrak{a}'_i$, then $x\pi \in \mathfrak{a}$ for some $\pi \notin \mathfrak{p}_i$. Then $x\pi \in \mathfrak{a}_i$ with $\pi \notin \mathfrak{p}_i$, hence $x \in \mathfrak{a}_i$. So $\mathfrak{a}'_i \subset \mathfrak{a}_i$.

Now suppose $\mathfrak{a}_i$ is isolated. If $\mathfrak{a}_i$ is an isolated primary component, then $\mathfrak{p}_i$ is minimal among the associated primes. For any $x \in \mathfrak{a}_i$, we can find an element outside $\mathfrak{p}_i$ that multiplies $x$ into $\bigcap_{j \neq i} \mathfrak{a}_j$, giving $\pi x \in \mathfrak{a}$. Thus $x \in \mathfrak{a}'_i$, proving $\mathfrak{a}'_i = \mathfrak{a}_i$. The third assertion follows from the second and the uniqueness of isolated prime ideals (Theorem 6/7).
