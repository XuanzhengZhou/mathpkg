---
role: proof
locale: en
of_concept: quasi-isomorphism-galois-group-modulo-torsion
source_book: gtm059
source_chapter: "5"
source_section: "§6. The Galois Group as Module over the Iwasawa Algebra"
---

**Proof.** From the structure theorem for finitely generated $\Lambda$-modules (Theorem 3.1), we know that there is a quasi-isomorphism

$$G \sim \Lambda^r \oplus \bigoplus_{i=1}^{t} \Lambda/(f_i^{e_i})$$

where $f_i$ are distinguished irreducible polynomials. In particular, $G/G_{\mathrm{tor}} \sim \Lambda^r$ with $r$ equal to the rank of the free part.

On the other hand, applying Theorem 6.1 to $K_n$ as base field (each $K_n$ satisfies the Leopoldt conjecture by hypothesis, and $K_0$ is totally imaginary so $r_2(K_n) = p^n r_2$), we obtain

$$G/G^{\gamma^{p^n}-1} \cong \mathbb{Z}_p^{r_2(K_n) + 1}.$$

By Theorem 5.2 applied to $K_n$, we know that

$$G/G^{\gamma-1} \cong \mathbb{Z}_p^{r_2+1}$$

where we have used $r_2 = r_2(K_0)$ and the fact that the $\mathbb{Z}_p$-extension contributes one extra copy of $\mathbb{Z}_p$.

From the structure theorem, one sees easily that the rank of the free part $r$ must equal $r_2$: modulo the augmentation ideal $X\Lambda$, the free part $\Lambda^r$ contributes $\mathbb{Z}_p^r$, while each torsion module $\Lambda/(f_i^{e_i})$ contributes a finite group or a $\mathbb{Z}_p$-module of rank equal to the degree of $f_i$ depending on whether $X$ divides $f_i$. Counting $\mathbb{Z}_p$-ranks modulo $X$ forces $r = r_2$ and all $f_i$ to be distinguished polynomials not divisible by $X$.

Thus $G/G_{\mathrm{tor}} \sim \Lambda^{r_2}$. $\square$
