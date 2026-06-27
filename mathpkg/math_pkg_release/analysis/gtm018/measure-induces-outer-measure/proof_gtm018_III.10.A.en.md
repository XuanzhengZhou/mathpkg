---
role: proof
locale: en
of_concept: measure-induces-outer-measure
source_book: gtm018
source_chapter: "III"
source_section: "10"
---

If $E \in \mathbf{R}$, then $E \subset E \cup 0 \cup 0 \cup \cdots$ and therefore $\mu^*(E) \leq \mu(E) + \mu(0) + \mu(0) + \cdots = \mu(E)$. On the other hand if $E \in \mathbf{R}$, $E_n \in \mathbf{R}$, $n = 1, 2, \cdots$, and $E \subset \bigcup_{n=1}^{\infty} E_n$, then, by 9.B, $\mu(E) \leq \sum_{n=1}^{\infty} \mu(E_n)$, so that $\mu(E) \leq \mu^*(E)$. Hence $\mu^*(E) = \mu(E)$ for $E$ in $\mathbf{R}$, i.e. $\mu^*$ is an extension of $\mu$.

To prove that $\mu^*$ is an outer measure on $\mathbf{H}(\mathbf{R})$, we first note that $\mu^*$ is clearly non negative and monotone. To prove countable subadditivity, let $\{E_i\}$ be a sequence of sets in $\mathbf{H}(\mathbf{R})$ with union $E$. Given $\epsilon > 0$, choose for each $i$ a sequence $\{E_{ij}\}$ of sets in $\mathbf{R}$ such that

$$E_i \subset \bigcup_{j=1}^{\infty} E_{ij} \quad \text{and} \quad \sum_{j=1}^{\infty} \mu(E_{ij}) \leq \mu^*(E_i) + \frac{\epsilon}{2^i}.$$

(The possibility of such a choice follows from the definition of $\mu^*(E_i)$.) Then, since the sets $E_{ij}$ form a countable class of sets in $\mathbf{R}$ which covers $E$,

$$\mu^*(E) \leq \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} \mu(E_{ij}) \leq \sum_{i=1}^{\infty} \mu^*(E_i) + \epsilon.$$

The arbitrariness of $\epsilon$ implies that

$$\mu^*(E) \leq \sum_{i=1}^{\infty} \mu^*(E_i).$$

Suppose, finally, that $\mu$ is $\sigma$-finite and let $E$ be any set in $\mathbf{H}(\mathbf{R})$. Then, by the definition of $\mathbf{H}(\mathbf{R})$, there exists a sequence $\{E_i\}$ of sets in $\mathbf{R}$ such that $E \subset \bigcup_{i=1}^{\infty} E_i$. Since $\mu$ is $\sigma$-finite, there exists, for each $i = 1, 2, \cdots$, a sequence $\{E_{ij}\}$ of sets in $\mathbf{R}$ such that

$$E_i \subset \bigcup_{j=1}^{\infty} E_{ij} \text{ and } \mu(E_{ij}) < \infty.$$

Consequently

$$E \subset \bigcup_{i=1}^{\infty} \bigcup_{j=1}^{\infty} E_{ij} \text{ and } \mu^*(E_{ij}) = \mu(E_{ij}) < \infty.$$
