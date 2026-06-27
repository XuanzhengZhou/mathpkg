---
role: proof
locale: en
of_concept: seminorm-continuity-equivalence
source_book: gtm015
source_chapter: "3"
source_section: "37"
---

# Proof of Equivalent conditions for continuity of one seminorm relative to another

Let $E$ be a vector space over $\mathbb{K}$ and let $p, q$ be seminorms on $E$. The following conditions are equivalent:

**(a)** $p$ is continuous for $\tau_q$;

**(b)** $\tau_p \subset \tau_q$;

**(c)** there exists a constant $M > 0$ such that $p(x) \leq M q(x)$ for all $x \in E$.

*Proof.* Since $\tau_q$ is a compatible topology, (a) and (b) are equivalent by part (4) of (37.5).

**(a) $\Rightarrow$ (c):** Since $p$ is continuous at $\theta$ for $\tau_q$, the set $\{x : p(x) \leq 1\}$ is a $\tau_q$-neighborhood of $\theta$, hence contains some $\tau_q$-basic neighborhood $\{x : q(x) \leq \varepsilon\}$. Thus $q(x) \leq \varepsilon$ implies $p(x) \leq 1$. For arbitrary $x \neq \theta$ with $q(x) > 0$, set $y = \varepsilon x / q(x)$; then $q(y) = \varepsilon$, so $p(y) \leq 1$, i.e., $p(x) \leq (1/\varepsilon) q(x)$. Taking $M = 1/\varepsilon$ yields (c).

**(c) $\Rightarrow$ (a):** For any $\varepsilon > 0$, if $q(x) \leq \varepsilon/M$ then $p(x) \leq M q(x) \leq \varepsilon$, so $\{x : q(x) \leq \varepsilon/M\} \subset \{x : p(x) \leq \varepsilon\}$. Thus $\{x : p(x) \leq \varepsilon\}$ is a $\tau_q$-neighborhood of $\theta$, proving $p$ is $\tau_q$-continuous at $\theta$ and hence everywhere.
