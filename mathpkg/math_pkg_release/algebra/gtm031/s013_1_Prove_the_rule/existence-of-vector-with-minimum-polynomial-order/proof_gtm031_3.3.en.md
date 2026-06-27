---
role: proof
locale: en
of_concept: existence-of-vector-with-minimum-polynomial-order
source_book: gtm031
source_chapter: "The Theory of a Single Linear Transformation"
source_section: "3"
---

*Proof.* Let $(e_1, e_2, \dots, e_n)$ be a basis for $\Re$ over $\Phi$. Then the $e_i$ form a set of generators for $\Re$ relative to $A$, i.e., every vector $x \in \Re$ can be written as $x = \sum_{i=1}^n e_i \phi_i(A)$ for suitable $\phi_i(\lambda) \in \Phi[\lambda]$. Let $\mu_{e_i}(\lambda)$ be the order of $e_i$ and let $\mu(\lambda)$ be the minimum polynomial of $A$. Since each $\mu_{e_i}(\lambda)$ divides $\mu(\lambda)$, the least common multiple $\bar{\mu}(\lambda) = [\mu_{e_1}(\lambda), \dots, \mu_{e_n}(\lambda)]$ divides $\mu(\lambda)$. On the other hand, for any $x = \sum e_i \phi_i(A)$, we have

$$x\bar{\mu}(A) = \sum e_i \phi_i(A)\bar{\mu}(A) = \sum e_i \bar{\mu}(A)\phi_i(A) = 0,$$

since $\bar{\mu}(A)$ is a multiple of each $\mu_{e_i}(\lambda)$ and therefore annihilates each $e_i$. Hence $\bar{\mu}(A) = 0$, which implies $\mu(\lambda) \mid \bar{\mu}(\lambda)$. Thus $\mu(\lambda) = \bar{\mu}(\lambda)$.

Now factor each $\mu_{e_i}(\lambda)$ into prime powers:

$$\mu_{e_i}(\lambda) = \pi_1(\lambda)^{k_{1i}} \pi_2(\lambda)^{k_{2i}} \cdots \pi_s(\lambda)^{k_{si}},$$

where the $\pi_j(\lambda)$ are distinct monic irreducibles and $k_{ji} \geq 0$. Let $k_j = \max_i k_{ji}$. Then

$$\mu(\lambda) = \pi_1(\lambda)^{k_1} \pi_2(\lambda)^{k_2} \cdots \pi_s(\lambda)^{k_s}.$$

For each $j$, choose a vector $f_j$ whose order $\mu_{f_j}(\lambda)$ is divisible by $\pi_j(\lambda)^{k_j}$ (for instance, an $e_i$ for which $k_{ji} = k_j$). Then set $g_j = f_j \nu_j(A)$ where $\nu_j(\lambda) = \mu(\lambda)/\pi_j(\lambda)^{k_j}$, so that the order of $g_j$ is exactly $\pi_j(\lambda)^{k_j}$. The subspaces $\{g_j\}$ are independent because their orders are pairwise coprime. Let $u = g_1 + g_2 + \cdots + g_s$. By the lemma on the order of a sum of vectors with independent cyclic subspaces and pairwise coprime orders, the order of $u$ is the product $\prod \pi_j(\lambda)^{k_j} = \mu(\lambda)$. Thus there exists a vector $u \in \Re$ whose order is the minimum polynomial of $A$. $\square$
