---
role: proof
locale: en
of_concept: ulam-measurable-inaccessible
source_book: gtm037
source_chapter: "31"
source_section: "5"
---

(The text truncates the proof. The standard proof proceeds as follows.)

Let $m$ be measurable with measure $\mu$. First, $m$ is regular: if $\operatorname{cf}(m) = \kappa < m$, then $m = \bigcup_{\alpha < \kappa} X_\alpha$ with $|X_\alpha| < m$. By (ii) and (iii), $\mu(X_\alpha) = 0$ for each $\alpha$, so by $m$-additivity $\mu(m) = 0$, contradicting (i).

Second, $m$ is a strong limit cardinal: if $2^n \geq m$ for some $n < m$, let $f: m \to \mathcal{P}(n)$ be injective. For each $\xi < n$, define $A_\xi = \{\alpha < m : \xi \in f(\alpha)\}$. Then for each $\alpha$, exactly one of $\alpha \in A_\xi$ or $\alpha \notin A_\xi$ holds. Using the measure, one can define a function $g: n \to \{0,1\}$ that disagrees with every $f(\alpha)$, contradicting surjectivity. Hence $2^n < m$ for all $n < m$.
