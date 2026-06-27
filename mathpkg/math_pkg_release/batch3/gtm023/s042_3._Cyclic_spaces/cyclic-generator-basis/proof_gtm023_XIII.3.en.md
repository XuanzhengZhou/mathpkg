---
role: proof
locale: en
of_concept: cyclic-generator-basis
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

Let $l$ be the largest integer such that the vectors
$$a, \varphi(a), \ldots, \varphi^{l-1}(a)$$
are linearly independent. Then these vectors generate $E$. In fact, every vector $x \in E$ can be written in the form $x = f(\varphi)a$ where $f = \sum_{v=0}^{k} \alpha_v t^v$ is a polynomial. It follows that
$$x = \sum_{v=0}^{k} \alpha_v \varphi^v(a) = \sum_{j=0}^{l-1} \mu_j \varphi^j(a).$$

Thus the vectors $a, \varphi(a), \ldots, \varphi^{l-1}(a)$ form a basis of $E$. Now Proposition II implies that $l = m$.
