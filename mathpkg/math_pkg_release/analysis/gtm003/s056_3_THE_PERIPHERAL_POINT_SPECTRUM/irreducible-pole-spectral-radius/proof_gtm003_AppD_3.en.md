---
role: proof
locale: en
of_concept: irreducible-pole-spectral-radius
source_book: gtm003
source_chapter: "Appendix D"
source_section: "3. The Peripheral Point Spectrum"
---

**Proof of (3.2).** Let $p$ denote the leading coefficient of the principal part of the resolvent at $\lambda = r$ and let $q$ be the residue at $r$. Then $p$ is positive (cf. proof of (2.4), Corollary), and $p = q(u - re)^{k-1}$, where $k$ is the order of the pole; moreover, $q$ and its adjoint $q'$ are projections such that $q(E)$, $q'(E')$ are the null spaces of $(re - u)^k$, $(re' - u')^k$, respectively.

**(ii):** Since $C$ and $C'$ are total subsets of $E$ and $E'$, respectively, there exist eigenvectors (pertaining to $r$) of $u$ in $C$, and of $u'$ in $C'$. Let $x_0, x'_0$ be any such eigenvectors. From $uR(\lambda, u)x_0 = \frac{r}{\lambda - r} x_0$ we conclude that $x_0$ is quasi-interior to $C$, because $u$ is irreducible. Similarly, $\langle x, u'R(\lambda, u')x'_0 \rangle = \frac{r}{\lambda - r} \langle x, x'_0 \rangle$ for all $x \in E$, and since $u$ is irreducible we obtain $\langle x, x'_0 \rangle > 0$ for all $x \in C$, $x \neq 0$; i.e., $x'_0$ is a strictly positive linear form.

**(i):** If $r = 0$, then $uR(\lambda, u)x_0 = 0$ for all $\lambda > 0$, contradicting the irreducibility of $u$ (which requires $uR(\lambda, u)x_0$ to be quasi-interior). Thus $r > 0$. If $k > 1$ were the order of the pole, then $p = q(u - re)^{k-1} \neq 0$ and $p(u - re) = q(u - re)^k = 0$. The subspace $p(E)$ is contained in the eigenspace $N(r)$ of $u$ for $r$, hence $p(E) \subset N(r)$. But $p$ is positive and $p \neq 0$, so there exists $x \in C$ with $p(x) \in C \cap N(r)$, $p(x) \neq 0$. Then $uR(\lambda, u)p(x) = \frac{r}{\lambda - r} p(x)$, showing $p(x)$ is quasi-interior to $C$. On the other hand, $p(x) = q((u - re)^{k-1}x)$ and the positivity of $q$ together with $k > 1$ implies that $p(x)$ lies in a null space of higher order, contradicting that it belongs to $N(r)$ unless $k = 1$. Hence $k = 1$ and $r$ is a simple pole.

**(iii):** The projection $p = q$ maps $E$ onto $N(r)$. Since $p(C) \subset C \cap N(r)$, the restriction of $C$ to $p(E)$ is a proper cone. By (ii), every non-zero element of $p(C)$ is quasi-interior to $p(C)$ in $p(E)$. In case (a), $C$ has interior points, hence so does $p(C)$ in $p(E)$. Since $p(C)$ is a closed proper cone in $p(E)$, it follows that $p(E)$ has dimension $1$ and hence $d(r) = 1$. If (b) $d(r)$ is finite, then every quasi-interior point of $p(C)$ in $p(E)$ is interior to $p(C)$ (cf. the lemma preceding (V, 4.1)) and the conclusion is the same as before.

There remains to show that $d(r) = 1$ if $E$ is a Banach lattice. If $x$ is any eigenvector of $u$ pertaining to $r$, then from $rx = u(x)$ it follows that $r|x| = |u(x)| \leq u(|x|)$. If $x'_0 \in C'$ is an eigenvector of $u'$ for $r$, we obtain
$$r \langle |x|, x'_0 \rangle \leq \langle u(|x|), x'_0 \rangle = r \langle |x|, x'_0 \rangle,$$
and this implies that $r|x| = u(|x|)$, since $r > 0$ and $x'_0$ is a strictly positive linear form by (ii). Now $x = x^+ - x^-$ and $|x| = x^+ + x^-$; hence both $x^+$, $x^-$ are positive elements of the eigenspace $N(r)$ of $u$ pertaining to $r$. Since they are lattice disjoint and the lattice operations are continuous in $E$, both cannot be quasi-interior points of $C$; thus either $x^+ = 0$ or else $x^- = 0$. Therefore, if $x$ is an eigenvector of $u$ for $r$, we have either $x \in C$ or $x \in -C$. Hence this eigenspace is totally ordered; since this order is also Archimedean, it follows that $d(r) = 1$ (Chapter V, Exercise 2).
