---
role: proof
locale: en
of_concept: lemma-10-13
source_book: gtm055
source_chapter: "10"
source_section: "Section 11_Section_11"
---

Proof. That $\mu^*$ agrees with $\rho$ on open sets follows at once from Lemma 10.10. Let $U$ and $V$ be open sets, and let $\varepsilon$ be any positive number. Let $f$ be any continuous function on $X$ such that $0 \leq f \leq \chi_U$ and $\varphi_0(f) > \rho(U) - \varepsilon$, and let $K = \{x \in X : f(x) \geq \varepsilon\}$.

$\varepsilon$ is a positive number, then by the definition of $\mu^*$ there exists a sequence $\{V_n\}_{n=1}^{\infty}$ of open sets in $X$ such that

$$A \subset \bigcup_{n=1}^{\infty} V_n \quad \text{and} \quad \sum_{n=1}^{\infty} \rho(V_n) < \mu^*(A) + \varepsilon.$$

By the countable subadditivity of $\mu^*$ we have

$$\mu^*(A \cap U) \leq \sum_{n=1}^{\infty} \mu^*(V_n \cap U) \quad \text{and} \quad \mu^*(A \setminus U) \leq \sum_{n=1}^{\infty} \mu^*(V_n \setminus U).$$

But then, by Lemma 10.13 and (2), we obtain the inequality

$$\mu^*(A \cap U) + \mu^*(A \setminus U) \leq \mu^*(A) + \varepsilon,$$

and since $\varepsilon$ is arbitrary, this implies that $U$ is measurable with respect to $\mu^*$. From this it follows, of course, that the $\sigma$-ring of sets measurable with respect to $\mu^*$ contains the $\sigma$-ring $B$ of Borel sets in $X$ (see Problem 8C), and hence that $\mu = \mu^*$ | $B$ is a Borel measure on $X$ with the property that $\mu(U) = \rho(U)$ for every open set $U$. Since Lemma 10.11 clearly shows that the measure $\mu$ is regular, and since the uniqueness of $\mu$ was settled in Proposition 10.8, the proof will be complete if we verify (1) for the measure $\mu$.

To do this, we note first that if $f$ is a continuous function on $X$ and $V$ is an open set in $X$ such that $f \geq \chi_V$, then $\varphi(f) \geq \varphi(g)$ for every continuous function $g$ on $X$ such that $0 \leq g \leq \chi_V$, and therefore $\varphi
