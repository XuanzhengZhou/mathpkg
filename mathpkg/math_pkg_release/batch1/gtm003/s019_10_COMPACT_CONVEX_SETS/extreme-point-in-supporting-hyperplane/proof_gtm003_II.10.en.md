---
role: proof
locale: en
of_concept: extreme-point-in-supporting-hyperplane
source_book: gtm003
source_chapter: "II"
source_section: "10"
---

Let $H$ be a closed real hyperplane supporting $C$ and denote by $\mathfrak{M}$ the family of all closed real linear manifolds contained in $H$ and supporting $C$. $\mathfrak{M}$ is inductively ordered under downward inclusion $\supset$; for, if $\{M_\alpha : \alpha \in A\}$ is a totally ordered subfamily, then $M = \bigcap_\alpha M_\alpha$ will be its lower bound in $\mathfrak{M}$, provided that $M \cap C \neq \emptyset$. But the family $\{M_\alpha \cap C : \alpha \in A\}$, again totally ordered under $\supset$, is a filter base consisting of closed subsets of $C$; since $C$ is compact, it follows that $M \cap C = (\bigcap_\alpha M_\alpha) \cap C = \bigcap_\alpha (M_\alpha \cap C)$ is not empty. Hence by Zorn's lemma, there exists a minimal element $M_0 \in \mathfrak{M}$. If $M_0 = \{x_0\}$, then $x_0$ is an extreme point of $C$ contained in $H$; the assumption $\dim M_0 \geq 1$ leads to a contradiction by considering a proper closed linear submanifold of $M_0$ that still supports $C$, contradicting the minimality of $M_0$. Therefore $\dim M_0 = 0$ and $M_0$ consists of a single extreme point.
