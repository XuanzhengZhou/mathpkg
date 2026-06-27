---
role: proof
locale: en
of_concept: complex-approximation-cohomology
source_book: gtm052
source_chapter: "III"
source_section: "12"
---

First we fix our notation. For any complex $N^\bullet$, let

$$Z^n(N^\bullet) = \ker(d^n: N^n \to N^{n+1})$$

and

$$B^n(N^\bullet) = \operatorname{im}(d^{n-1}: N^{n-1} \to N^n).$$

Thus we have $h^n(N^\bullet) = Z^n(N^\bullet) / B^n(N^\bullet)$.

We construct $L^\bullet$ by descending induction on the degree. Since $C^\bullet$ is bounded above, we may assume $C^n = 0$ for $n$ sufficiently large. Set $L^n = 0$ for all large $n$, and define the map $g^n: L^n \to C^n$ to be zero there.

Now suppose we have constructed $L^i$ and maps $g^i: L^i \to C^i$ for all $i > n$, compatible with the differentials. We wish to construct $L^n$ and $g^n$ so that the induced map $h^{n+1}(L^\bullet) \to h^{n+1}(C^\bullet)$ is an isomorphism and the map $Z^n(L^\bullet) \to h^n(C^\bullet)$ is surjective.

Consider the commutative diagram with exact rows coming from the definitions of $L^\bullet$ and $C^\bullet$ up to degree $n+1$. Let

$$K = \ker(Z^{n+1}(L^\bullet) \to h^{n+1}(C^\bullet)).$$

By hypothesis, $h^{n+1}(C^\bullet)$ is finitely generated. Choose a finitely generated free $A$-module $F$ and a map $F \to Z^{n+1}(C^\bullet)$ whose image generates the kernel of the map $Z^{n+1}(L^\bullet)/B^{n+1}(L^\bullet) \to h^{n+1}(C^\bullet)$.

Also choose a finitely generated free $A$-module $G$ mapping onto the kernel of $Z^n(L^\bullet) \to h^n(C^\bullet)$. Set $L^n = F \oplus G$, define the differential $d^n: L^n \to L^{n+1}$ to be the composition $F \to Z^{n+1}(C^\bullet) \to C^{n+1}$ (lifted to $L^{n+1}$ via the isomorphism $h^{n+1}(L^\bullet) \cong h^{n+1}(C^\bullet)$ on the $F$ summand, and zero on the $G$ summand), and define $g^n: L^n \to C^n$ using the commutative diagram.

One checks easily that $g$ commutes with $d$, that $h^{n+1}(L^\bullet) \to h^{n+1}(C^\bullet)$ is an isomorphism, and that $Z^n(L^\bullet) \to h^n(C^\bullet)$ is surjective. So inductively, we construct the complex $L^\bullet$ required.

Now suppose that each $C^i$ is a flat $A$-module. We prove, by descending induction on $i$, that

$$h^i(L^\bullet \otimes M) \to h^i(C^\bullet \otimes M)$$

is an isomorphism for all $A$-modules $M$. For $i \gg 0$, both $L^i$ and $C^i$ are $0$, so both sides are $0$. So suppose this is true for $i + 1$. It is sufficient to prove the result for finitely generated $A$-modules, because any $A$-module is a direct limit of finitely generated ones, and both $\otimes$ and $h^i$ commute with direct limits.

Given $M$ finitely generated, write it as a quotient of a free finitely generated $A$-module $E$, and let $R$ be the kernel:

$$0 \to R \to E \to M \to 0.$$

Since each $C^i$ is flat by hypothesis, and each $L^i$ is flat because it is free, we obtain an exact, commutative diagram of complexes

$$\begin{CD}
0 @>>> L^\bullet \otimes R @>>> L^\bullet \otimes E @>>> L^\bullet \otimes M @>>> 0 \\
@VVV @VVV @VVV \\
0 @>>> C^\bullet \otimes R @>>> C^\bullet \otimes E @>>> C^\bullet \otimes M @>>> 0
\end{CD}$$

Taking the associated long exact cohomology sequences and using the induction hypothesis (the maps $h^i(L^\bullet \otimes N) \to h^i(C^\bullet \otimes N)$ are isomorphisms for $N = R, E$ and all $i$, and for $N = M$ for $i > n$), the five-lemma implies the isomorphism for $i = n$ and $N = M$ as well.
