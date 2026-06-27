---
role: proof
locale: en
of_concept: ostrowskis-theorem
source_book: gtm058
source_chapter: "I"
source_section: "2"
---

Let $\|\cdot\|$ be a nontrivial norm on $\mathbb{Q}$. Either $\|n\| \leq 1$ for all integers $, or there exists $ with $\|n_0\| > 1$.

Case 1: $\|n\| \leq 1$ for all integers $. The norm is non-Archimedean. Since nontrivial, there is $ with $\|n\| < 1$, so some prime $ has $\|p\| < 1$. Let $\mathcal{P} = \{q \text{ prime} : \|q\| < 1\}$. If , q_2 \in \mathcal{P}$ distinct, then $\gcd(q_1^M, q_2^N)=1$ so ^M + nq_2^N = 1$, giving  \leq \|q_1\|^M + \|q_2\|^N$, contradiction for large ,N$. So only one $ has $\|p\| < 1$. For other primes $, $\|q\|=1$. By prime factorization, $\|a\| = \|p\|^{\operatorname{ord}_p a}$. Let $\rho = \|p\|$; then $\|x\| = \rho^{\operatorname{ord}_p x}$ for all  \in \mathbb{Q}^\times$, equivalent to $|\cdot|_p$.

Case 2: $\exists n_0, \|n_0\| > 1$. Let $\alpha = \log_{n_0}\|n_0\| > 0$. Express $ in base $:  = a_0 + a_1 n_0 + \cdots + a_s n_0^s$ with /tmp/write_gtm058.sh \leq a_i < n_0$. Then $\|n\| \leq Cn^\alpha$. Apply to ^N$, take hBth root, let  \to \infty$ to get $\|n\| \leq n^\alpha$. Reverse inequality from $\|n_0^{s+1}\| \geq \|n\| - \|n_0^{s+1}-n\|$ gives $\|n\| \geq n^\alpha$. Hence $\|n\| = n^\alpha = |n|_\infty^\alpha$ for all $, so $\|\cdot\|$ is equivalent to $|\cdot|_\infty$.
