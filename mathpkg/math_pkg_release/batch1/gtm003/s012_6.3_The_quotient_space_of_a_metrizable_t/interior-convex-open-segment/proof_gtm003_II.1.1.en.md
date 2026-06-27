---
role: proof
locale: en
of_concept: interior-convex-open-segment
source_book: gtm003
source_chapter: "II"
source_section: "1.1"
---

Let $\lambda$, $0 < \lambda < 1$, be fixed; we have to show that $\lambda x + (1 - \lambda) y \in \mathring{A}$. By a translation if necessary we can arrange that $\lambda x + (1 - \lambda) y = 0$. Now $y = \alpha x$ where $\alpha < 0$. Since $w \rightarrow \alpha w$ is a homeomorphism of $L$ by (I, 1.1) and $x \in \mathring{A}$, $y \in \overline{A}$, there exists a $z \in \mathring{A}$ such that $\alpha z \in A$. Let $\mu = \alpha / (\alpha - 1)$; then $0 < \mu < 1$ and $\mu z + (1 - \mu) \alpha z = 0$. Hence

$$U = \{ \mu w + (1 - \mu) \alpha z : w \in \mathring{A} \}$$

is a neighborhood of $0$ since $w \rightarrow \mu w + (1 - \mu) \alpha z$ is a homeomorphism of $L$ mapping $z \in \mathring{A}$ onto $0$. But $w \in \mathring{A}$ and $\alpha z \in A$ imply $U \subset A$, since $A$ is convex; hence $0 \in \mathring{A}$.
