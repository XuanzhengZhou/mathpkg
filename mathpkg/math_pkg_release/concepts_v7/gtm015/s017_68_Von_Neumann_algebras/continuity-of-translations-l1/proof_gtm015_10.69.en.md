---
role: proof
locale: en
of_concept: continuity-of-translations-l1
source_book: gtm015
source_chapter: "10"
source_section: "69"
---

# Proof of Continuity of translations in L^1(G)

Proof. If $u \in L^1(G)$, we are to show that the mappings $s \mapsto u_s$ and $s \mapsto u^s$ are continuous from $G$ to $L^1(G)$. We prove the result for left translations; the case of right translations is similar.

Let $u = [f]$ with $f \in \mathcal{L}^1(G)$. Given $\varepsilon > 0$, choose a continuous function $g$ with compact support such that $\|f - g\|_1 < \varepsilon/3$ (this is possible because $\mathcal{K}(G)$ is dense in $L^1(G)$, cf. 39.9). Since $g$ has compact support and is continuous, it is uniformly continuous; thus there exists a neighborhood $V$ of $e$ such that for all $s \in V$,

$$\sup_{t \in G} |g(s^{-1}t) - g(t)| < \frac{\varepsilon}{3 \, \mu(\operatorname{supp} g \cup s \operatorname{supp} g)}$$

where $\mu$ denotes Haar measure. It follows that $\|g_s - g\|_1 < \varepsilon/3$ for all $s \in V$.

Now for any $s \in V$,

$$\|f_s - f\|_1 \leq \|f_s - g_s\|_1 + \|g_s - g\|_1 + \|g - f\|_1 = 2\|f - g\|_1 + \|g_s - g\|_1 < \varepsilon,$$

where we used $\|f_s - g_s\|_1 = \|f - g\|_1$ (left invariance of Haar measure). Thus $s \mapsto u_s$ is continuous at $e$, hence everywhere by the group structure.
