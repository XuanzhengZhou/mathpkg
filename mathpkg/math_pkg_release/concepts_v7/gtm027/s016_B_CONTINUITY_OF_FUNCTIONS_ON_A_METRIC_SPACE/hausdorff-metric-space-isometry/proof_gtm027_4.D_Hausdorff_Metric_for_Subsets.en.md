---
role: proof
locale: en
of_concept: hausdorff-metric-space-isometry
source_book: gtm027
source_chapter: "4"
source_section: "D. Hausdorff Metric for Subsets"
---

# Proof of Hausdorff Metric Space and Isometric Embedding

Let $(X, d)$ be a metric space of finite diameter, and let $\alpha$ be the family of all closed subsets of $X$. For $r > 0$ and $A \in \alpha$, define
$$V_r(A) = \{x \in X : \mathrm{dist}(x, A) < r\},$$
where $\mathrm{dist}(x, A) = \inf\{d(x, a) : a \in A\}$.

For $A, B \in \alpha$, define
$$d'(A, B) = \inf\{r > 0 : A \subset V_r(B) \text{ and } B \subset V_r(A)\}.$$

## (a) $(\alpha, d')$ is a metric space

**Non-negativity**: $d'(A, B) \geq 0$ by definition (infimum of positive numbers extended by zero convention).

**Identity**: $d'(A, A) = 0$, since for any $r > 0$, $A \subset V_r(A)$, so the infimum is 0.

Conversely, if $d'(A, B) = 0$, then for every $\varepsilon > 0$, $A \subset V_\varepsilon(B)$ and $B \subset V_\varepsilon(A)$. Thus for each $a \in A$, $\mathrm{dist}(a, B) < \varepsilon$ for all $\varepsilon > 0$, so $\mathrm{dist}(a, B) = 0$, which implies $a \in \overline{B} = B$ (since $B$ is closed). Hence $A \subset B$. Symmetrically $B \subset A$, so $A = B$.

**Symmetry**: $d'(A, B) = d'(B, A)$ is immediate from the symmetric definition.

**Triangle inequality**: Let $A, B, C \in \alpha$. For any $\varepsilon > 0$, choose $r$ such that $d'(A, B) < r < d'(A, B) + \varepsilon$ and $s$ such that $d'(B, C) < s < d'(B, C) + \varepsilon$.

Then $A \subset V_r(B)$ and $B \subset V_s(C)$. For any $a \in A$, there exists $b \in B$ with $d(a, b) < r$, and for this $b$, there exists $c \in C$ with $d(b, c) < s$. By the triangle inequality in $(X, d)$, $d(a, c) \leq d(a, b) + d(b, c) < r + s$. Thus $\mathrm{dist}(a, C) < r + s$, so $A \subset V_{r+s}(C)$. Symmetrically $C \subset V_{r+s}(A)$.

Hence $d'(A, C) \leq r + s < d'(A, B) + d'(B, C) + 2\varepsilon$. Since $\varepsilon > 0$ was arbitrary, $d'(A, C) \leq d'(A, B) + d'(B, C)$.

## Isometric embedding

Define $\varphi: X \to \alpha$ by $\varphi(x) = \{x\}$. For $x, y \in X$,
$$d'(\{x\}, \{y\}) = \inf\{r > 0 : \{x\} \subset V_r(\{y\}) \text{ and } \{y\} \subset V_r(\{x\})\}.$$
The condition $\{x\} \subset V_r(\{y\})$ means $\mathrm{dist}(x, \{y\}) < r$, i.e., $d(x, y) < r$. Similarly $\{y\} \subset V_r(\{x\})$ means $d(y, x) < r$. Thus
$$d'(\{x\}, \{y\}) = \inf\{r > 0 : d(x, y) < r\} = d(x, y).$$
Therefore $\varphi$ is an isometry of $X$ onto the subspace $\{\{x\} : x \in X\}$ of $\alpha$.
