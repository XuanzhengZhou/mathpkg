---
role: exercise
locale: en
chapter: "4"
section: "D"
exercise_number: 1
of_concept: hausdorff-metric-space-isometry
source_book: gtm027
---

# Exercise D.1 — Hausdorff Metric Space and Isometric Embedding

Let $(X, d)$ be a metric space of finite diameter. Let $\alpha$ be the family of all closed subsets of $X$. For $r > 0$ and $A \in \alpha$, define
$$V_r(A) = \{x \in X : \operatorname{dist}(x, A) < r\},$$
where $\operatorname{dist}(x, A) = \inf\{d(x, a) : a \in A\}$. For $A, B \in \alpha$, define the Hausdorff metric
$$d'(A, B) = \inf\{r > 0 : A \subset V_r(B) \text{ and } B \subset V_r(A)\}.$$

Prove that:

(a) $(\alpha, d')$ is a metric space, and the map $\varphi: X \to \alpha$ defined by $\varphi(x) = \{x\}$ is an isometry of $X$ onto a subspace of $\alpha$.

(b) Characterize the topology of the Hausdorff metric on $\alpha$ in terms of the topology of $X$.
