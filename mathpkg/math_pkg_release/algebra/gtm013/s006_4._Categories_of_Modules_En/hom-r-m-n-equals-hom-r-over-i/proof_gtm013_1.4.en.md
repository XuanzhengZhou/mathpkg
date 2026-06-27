---
role: proof
locale: en
of_concept: hom-r-m-n-equals-hom-r-over-i
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

If $I$ is an ideal of $R$ annihilating both $M$ and $N$, then for $r \in R$ and $x \in M$, the scalar product $rx$ depends only on the coset $r + I$: if $r - r' \in I$, then $(r - r')x = 0$, so $rx = r'x$. Hence the $R$-module structure induces a well-defined $R/I$-module structure by $(r+I)x = rx$. The same holds for $N$.

Now if $f \in \operatorname{Hom}_R(M,N)$, then $f((r+I)x) = f(rx) = rf(x) = (r+I)f(x)$, so $f$ is an $R/I$-homomorphism. Conversely, if $f \in \operatorname{Hom}_{R/I}(M,N)$, then $f(rx) = f((r+I)x) = (r+I)f(x) = rf(x)$, so $f \in \operatorname{Hom}_R(M,N)$. Thus the two Hom sets are equal.
