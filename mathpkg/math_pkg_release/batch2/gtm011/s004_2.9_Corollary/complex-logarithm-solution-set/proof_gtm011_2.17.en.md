---
role: proof
locale: en
of_concept: complex-logarithm-solution-set
source_book: gtm011
source_chapter: "2"
source_section: "2.17"
---

Suppose $e^z = w$ with $w \neq 0$ (since $e^z \neq 0$ for any $z$, we cannot solve $e^z = 0$). Write $z = x + iy$ with $x, y \in \mathbb{R}$. Then

$$w = e^z = e^{x+iy} = e^x e^{iy} = e^x (\cos y + i \sin y).$$

Taking absolute values gives $|w| = e^x$, so $x = \log |w|$ where $\log$ denotes the usual real logarithm. The argument of $w$ must satisfy $y = \arg w + 2\pi k$ for some integer $k$, since $e^{i\theta}$ is $2\pi$-periodic. Therefore every solution has the form

$$z = x + iy = \log |w| + i(\arg w + 2\pi k)$$

for some $k \in \mathbb{Z}$. Thus the solution set is exactly $\{ \log |w| + i(\arg w + 2\pi k) : k \in \mathbb{Z} \}$.
