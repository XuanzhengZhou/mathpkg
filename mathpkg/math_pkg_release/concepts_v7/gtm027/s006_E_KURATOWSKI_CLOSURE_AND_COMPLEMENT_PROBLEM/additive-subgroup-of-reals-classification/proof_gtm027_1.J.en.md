---
role: proof
locale: en
of_concept: additive-subgroup-of-reals-classification
source_book: gtm027
source_chapter: "1"
source_section: "J"
---

# Proof of Classification of Additive Subgroups of the Reals

**Theorem.** An additive subgroup $G$ of $\mathbb{R}$ which contains more than one member is either dense in $\mathbb{R}$ or has a smallest positive element.

*Proof.* Let $G \subseteq \mathbb{R}$ be an additive subgroup with $G \neq \{0\}$. Define
$$G^+ = \{x \in G : x > 0\}.$$
Since $G \neq \{0\}$, there exists $g \in G \setminus \{0\}$. If $g > 0$, then $g \in G^+$; if $g < 0$, then $-g \in G^+$. Thus $G^+ \neq \emptyset$.

Let $a = \inf G^+$. Note $a \geq 0$.

**Case 1:** $a > 0$. We claim $a \in G^+$. Suppose not. Then by definition of infimum, there exist elements of $G^+$ arbitrarily close to $a$. Pick $x, y \in G^+$ with $a < x < y < 2a$. Then $y - x \in G$ (since $G$ is a group) and $0 < y - x < a$. But $y - x > 0$ implies $y - x \in G^+$, contradicting the definition of $a$ as $\inf G^+$. Hence $a \in G^+$, and $a$ is the smallest positive element of $G$. In this case $G = a\mathbb{Z} = \{na : n \in \mathbb{Z}\}$, a discrete subgroup.

**Case 2:** $a = 0$. We claim $G$ is dense in $\mathbb{R}$. Let $x \in \mathbb{R}$ and $\varepsilon > 0$. Since $\inf G^+ = 0$, there exists $g \in G^+$ with $0 < g < \varepsilon$. Consider the integer multiples $ng$ for $n \in \mathbb{Z}$. These form an arithmetic progression with step size $g < \varepsilon$, so there exists $n \in \mathbb{Z}$ such that $|ng - x| < g < \varepsilon$. Since $ng \in G$, this proves $G$ is dense in $\mathbb{R}$.

**Corollary.** The set of rational numbers $\mathbb{Q}$ is dense in $\mathbb{R}$, since $\mathbb{Q}$ is an additive subgroup with $\inf \mathbb{Q}^+ = 0$. $\square$
