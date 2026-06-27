---
role: proof
locale: en
of_concept: characteristic-equation-eigenvalue
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§6. The characteristic polynomial"
---

Assume that $a$ is an eigenvector of $\varphi$ with eigenvalue $\lambda$. Then $\varphi a = \lambda a$ with $a \neq 0$. Rewrite as $(\varphi - \lambda \iota)a = 0$. Since $a \neq 0$, the linear transformation $\varphi - \lambda \iota$ has a non-trivial kernel, hence it is not injective and therefore not regular. Consequently, $\det(\varphi - \lambda \iota) = 0$.

Conversely, suppose $\lambda$ satisfies $\det(\varphi - \lambda \iota) = 0$. Then $\varphi - \lambda \iota$ is not regular, so its kernel is non-trivial. Pick $a \neq 0$ in $\ker(\varphi - \lambda \iota)$. Then $(\varphi - \lambda \iota)a = 0$, i.e., $\varphi a = \lambda a$, so $a$ is an eigenvector with eigenvalue $\lambda$.
