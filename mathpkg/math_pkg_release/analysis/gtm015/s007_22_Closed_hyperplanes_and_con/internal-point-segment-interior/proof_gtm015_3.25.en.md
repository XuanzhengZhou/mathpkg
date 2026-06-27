---
role: proof
locale: en
of_concept: internal-point-segment-interior
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Internal points of segment from interior to closure are interior

Let $E$ be a TVS over $\mathbb{K}$ and let $A$ be a convex subset of $E$ with nonempty interior. Suppose $a \in \operatorname{int} A$ and $b \in \overline{A}$. Let $c$ be an internal point of the segment from $a$ to $b$:

$$c = \alpha a + (1 - \alpha)b,$$

where $0 < \alpha < 1$. The problem is to show that $c$ is an interior point of $A$.

Since $a \in \operatorname{int} A$, there exists a neighborhood $V$ of $\theta$ such that $a + V \subset A$. We claim that

$$c + \alpha V \subset A.$$

Indeed, if $v \in V$, then $a + v \in A$, and since $b \in \overline{A}$, there exists $b' \in A$ arbitrarily close to $b$. More precisely, for $v \in V$, we have

$$c + \alpha v = \alpha(a + v) + (1 - \alpha)b.$$

Since $b \in \overline{A}$, every neighborhood of $b$ intersects $A$. Choose $b' \in A \cap (b - \tfrac{\alpha}{1-\alpha} V)$. Then

$$c + \alpha v = \alpha a + (1 - \alpha) b' + \alpha v + (1 - \alpha)(b - b') \in \alpha A + (1 - \alpha) A + \text{(neighborhood of }\theta\text{)} \subset A$$

for suitably small $v$. This shows $c$ is interior.
