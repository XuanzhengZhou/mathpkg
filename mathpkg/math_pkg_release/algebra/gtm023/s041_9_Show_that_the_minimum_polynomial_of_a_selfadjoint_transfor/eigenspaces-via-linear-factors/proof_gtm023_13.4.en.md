---
role: proof
locale: en
of_concept: eigenspaces-via-linear-factors
source_book: gtm023
source_chapter: "13"
source_section: "13.4"
---
Suppose $\mu = f_1^{k_1} \cdots f_r^{k_r}$ is the decomposition of the minimum polynomial of $\varphi$ into irreducible factors, and let $E = E_1 \oplus \cdots \oplus E_r$ be the corresponding primary decomposition, where $E_i = K(f_i^{k_i})$. If $\lambda$ is an eigenvalue of $\varphi$, then there exists a nonzero vector $x$ such that $\varphi(x) = \lambda x$, i.e., $(\varphi - \lambda \iota)(x) = 0$. Hence $x \in K(t - \lambda)$, and so $t - \lambda$ divides $\mu$ (by the property of the minimum polynomial). Since the $f_i$ are the irreducible factors of $\mu$, we must have $f_i = t - \lambda$ for some $i$. Conversely, if $f_i = t - \lambda$ is linear, then $K(f_i) \subset K(f_i^{k_i}) = E_i$. For any $x \in K(f_i)$, we have $f_i(\varphi)x = (\varphi - \lambda \iota)x = 0$, so $\varphi(x) = \lambda x$. Thus $K(f_i)$ is contained in the $\lambda$-eigenspace. Moreover, every eigenvector belongs to some $K(f_i)$ where $f_i$ is linear. Therefore the eigenspaces are exactly the spaces $K(f_i)$ for those $f_i$ in the decomposition which are linear.
