---
role: proof
locale: en
of_concept: theorem-macaulays-theorem
source_book: gtm029
source_chapter: "VII"
source_section: "8"
---

Upon replacing $G_1, \cdots, G_n$ by suitable powers, we may assume that the forms $F_1, \cdots, F_n$ have like degree $d$. We have just proved the existence of a finite set of monomials $\omega_j(X)$ which is a basis of $R$ over $S = A[[F_1, \cdots, F_n]]$ (or $A[F_1, \cdots, F_n]$). Furthermore, we have seen that every form $u(X)$ in $R$ may be written as

(4) $$u(X) = \sum_j \varphi_j(F)\omega_j(X)$$

where $\varphi_j$ is a form such that $d \cdot \partial(\varphi_j) + \partial(\omega_j) = \partial(u)$. Now, if $v(X)$ is any element of $R$, we apply (4) to each monomial $u(X)$ which occurs in $v(X)$, and by addition of terms we find a relation of the form

(4') $$v(X) = \sum_j \psi_j(F)\omega_j(X),$$

where the $\psi_j(F)$ are power series in $F_1, F_2, \cdots, F_n$ (or polynomials in $F_1, F_2, \cdots, F_n$), and where

(5) $$d \cdot o(\psi_j) \geq o(v) - o(\omega_j)$ in the power series case,

with equality for at least one value of $j$;

(5') $$d \cdot \partial(\psi_j) \leq \partial(v) - \partial(\omega_j)$ in the polynomial case,

again with equality for at least one value of $j$.

We prove that $\{\omega_j(X)\}$ is also a basis of $R$ over $T$, and thus will prove Theorem 28. For every $v(X)$ in $R$, we consider the difference $v(X) - \sum_j \psi_j(G)\omega_j(X)$, where $v

Furthermore the inequalities $d \cdot o(\chi_{js}) \geq s - o(\omega_j)$ show that the sequences $\{\psi_{j,s}\}$ are Cauchy sequences in the power series ring in $n$ variables. Let $\mu_j$ be the limit of $\{\psi_{j,s}\}$. By passage to the limit we obviously have $v(X) = \sum_j \mu_j(G) \omega_j(X)$, and this proves our assertion in the power series case.

In the polynomial case we proceed by induction on the degree $s$ of $v(X)$. The case $s=0$ is straightforward, if care has been taken to include the monomial 1 among the $\omega_j(X)$'s. As above, we write $v(X) = \sum_j \psi_j(F) \omega_j(X)$, and consider the differences $v'(X) = v(X) - \sum_j \psi_j(G) \omega_j(X)$. Since the replacement of the $F_i$'s by the $G_i$'s leaves the highest degree form of $\sum_j \psi_j(F) \omega_j(X)$ unchanged, we have $\partial(v') < \partial(v)$, and our induction hypothesis shows that $v'(X) = \sum_j \chi_j(G) \omega_j(X)$ with suitable polynomials $\chi_j$. Therefore $v(X)$ is also a linear combination of the monomials $\omega_j(X)$, with coefficients in $A[G_1, \cdots, G_n]$.

Q.E.D
