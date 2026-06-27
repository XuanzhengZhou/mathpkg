---
role: proof
locale: en
of_concept: lemma-completion
source_book: gtm029
source_chapter: "VIII"
source_section: "12"
---

We have to prove that every minimal prime ideal $\mathfrak{p}(\neq(0))$ of $A$ is principal.‡ For this it is sufficient to prove that $\hat{A}\mathfrak{p}$ is principal, for, if we have $\hat{A}\mathfrak{p} = \hat{A}a' (a' \in \hat{A})$ and if $\{b_1, \cdots, b_n\}$ denotes a basis of $\mathfrak{p}$, we have $b_i = a'b'_i (b'_i \in \hat{A})$ and $a' = \sum_i c'_i b_i (c'_i \in \hat{A})$; thus $a' = \left( \sum_i c'_i b'_i \right) a'$, whence $1 = \sum_i c'_i b'_i$ since $\hat{A}$ is a domain; then, since $\hat{A}$ is a local ring, at least one of the terms $c'_i b'_i$, say $c'_1 b'_1$, is invertible, whence $b'_1$ is invertible; since $b_1 = a'b'_1$, we have $\hat{A}\mathfrak{p} = \hat{A}a' = \hat{A}b_1$. Hence we have $\mathfrak{p} = \hat{A}\mathfrak{p} \cap A = \hat{A}b_1 \cap A = Ab_1$ (§2, Theorem 5

valuation ring (Vol. I, Ch. V, § 6, corollary to Theorem 14). Hence $\mathfrak{p}A_S = \mathfrak{p}A_\nu$ is a principal ideal, and, since $\mathfrak{p}\hat{A}_S = \mathfrak{p}A_S\hat{A}_S$, $\mathfrak{p}\hat{A}_S$ is also a principal ideal. Thus, since $\hat{A}_S$ is integrally closed, all the associated prime ideals of $\mathfrak{p}\hat{A}_S$ have height 1 (Vol. I, Ch. V, § 6, Theorem 14). This proves lemma 2 and Theorem 30.

REMARK. Lemma 2 reduces the problem of unique factorization in arbitrary (i.e., not necessarily equicharacteristic) regular local rings to the case of complete regular local rings. The unique factorization property holds also in an arbitrary complete regular local ring $A$ of dimension 1 or 2: it is obvious in dimension 1 since $A$ is then a discrete valuation ring; in dimension 2 one uses an analogue of Hensel's lemma for homogeneous polynomials in two variables.† It may also be proved that, if the unique factorization property holds for regular local rings of dimension three, then it holds in any regular local ring. (This has been proved by O. Zariski in unpublished notes, in 1947; subsequently this has been proved by M. Nagata ["A general theory of algebraic geometry over Dedekind domains, II"] (§ 5, Proposition 11), Amer. J. of Mathematics, v. 80, 1958]. Using these facts and methods of cohomological algebra, M. Auslander and D. A. Buchsbaum have recently proved the unique factorization theorem in any regular local ring in their paper, "Unique factorization in regular local rings", PNAS, v. 45 (1959), pp. 733–734. We present their proof in Appendix 7, reducing the cohomological prerequisites to the knowledge of the properties of chains of syzygies given in VII,

(D) The local ring $A$ is a domain, and there exists an element $d \neq 0$ in $A$ such that, if $\hat{A}$ denotes the completion of $A$ and $(\hat{A})'$ the integral closure of $\hat{A}$ in its total quotient ring, then $d(\hat{A})' \subset \hat{A}$.

In the first part of this section we shall derive some consequences of hypothesis (D). In the second part we shall show that the local rings of algebraic geometry satisfy hypothesis (D), thus proving that the consequences of (D) hold true for these local rings.

We shall say that a local ring $A$ is analytically unramified if its completion $\hat{A}$ has no nilpotent elements (other than 0).
