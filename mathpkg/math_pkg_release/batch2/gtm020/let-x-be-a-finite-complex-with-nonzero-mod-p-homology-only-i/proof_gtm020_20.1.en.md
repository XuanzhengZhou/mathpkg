---
locale: en
of_concept: let-x-be-a-finite-complex-with-nonzero-mod-p-homology-only-i
role: proof
source_book: gtm020
source_chapter: 20. General Theory of Characteristic Classes
source_section: '1'
---

By taking a skeleton $Y$ of $X$ we have a finite cell complex with $H^n(Y, F_2) = F_2x$, $H^{2n}(Y, F_2) = F_2x^2$, and other cohomology groups equal to zero mod 2. By (6.2) it follows that $n = 2, 4$, or 8. We have only to show $n = 8$ is impossible.

Let $x$ denote a generator of $H^8(X, Z_{(2)})$ over $Z_{(2)}$. Then $x^2$ and $x^3$ are generators of $H^{16}(X, Z_{(2)})$ and $H^{24}(X, Z_{(2)})$ over $Z_{(2)}$ respectively. Now $\tilde{K}(X) \otimes Z_{(2)}$ has a basis $y_1, y_2, y_3$ over $Z_{(2)}$ such that

$$ch(y_1) = x + ax^2 + bx^3, \quad ch(y_2) = x^2 + cx^3, \quad ch(y_3) = x^3.$$

Since $ch(y_1^2) = (x + ax^2 + bx^3)^2 = x^2 + 2ax^3$ and $ch(y_2) = x^2 + cx^3$, it follows that $ch(y_1^2 - y_2) = (2a - c)x^3$ and $2a - c \in Z_{(2)}$ because $y_1^2 - y_2 \in \tilde{K}(X) \otimes Z_{(2)}$.

Applying $ch$ to the relation $\psi^2(y_1) - y_1^2 = 2(a_1y_1 + a_2y_2 + a_3y_3)$, we derive the relation

$$(2^4x + 2^8ax^2 + 2^{12}bx^3) - (x^2 + 2ax^3)$$

$$= 2a_1(x + ax^2 +

spheres. In (4.9) with (5.2) and (5.5) we showed that the mod $p$ Hopf invariant was nontrivial in the cases described above. This proves the theorem.

In chap. 15, §4 a more elementary derivation of the above theorem is given.

6.5 Remark. Of the four $H$-spaces $S^0, S^1, S^3$, and $S^7$ we saw in (4.9) that the first three $S^0, S^1$, and $S^3$ have classifying spaces $P_\infty(R), P_\infty(C)$, and $P_\infty(H)$ respectively. By (6.3) the $H$-space $S^7$ has no classifying space, and in fact more is true, any $H$-space structure on $S^7$ is not homotopy associative. If an $H$-space $G$ is homotopy associative, then $B_3(C)$, the third step in the classifying space construction, exists. For $G = S^7$ this has a cell decomposition $B_3(S^7) = S^8 \cup e^{16} \cup e^{24}$ with the third power $H^8(B_3(S^7)) \rightarrow H^{24}(B_3(S^7))$ non-zero. In (6.3) we showed that such a space cannot exist.

6.6 Remark. In (4.10) we remarked that each odd sphere $S_{(p)}^{2n-1}$ localized at $p$ admits an $H$-space structure. By (1)(6.2) we see that if $S_{(p)}^{2n-1}$ has a classifying space, then $n$ divides $p-1$. D. Sullivan proved that if $n$ divides $p-1$, then the localized space $S_{(p)}^{2n-1}$ has a classifying space. He considered the space $K(Z_p, 2)$ where $Z_p$ is the $p$-adic integers and the subgroup $\Gamma$ of $Z_p^*$ (the $p$-adic units) of order $n
