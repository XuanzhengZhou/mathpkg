---
role: proof
locale: en
of_concept: structure-of-lubin-tate-torsion-module
source_book: gtm059
source_chapter: "8"
source_section: "2. Formal p-adic Multiplication"
---

(i) Let $x \in A_n$ be a generator (a primitive $\pi^n$-torsion point, i.e., an element with $[\pi^{n-1}](x) \neq 0$). The map $a \mapsto [a]_f(x)$ gives an $\mathfrak{o}$-module homomorphism $\mathfrak{o} \to A_n$ with kernel $\pi^n\mathfrak{o}$. Since $A_n$ has $q^n$ elements and the map is surjective (the orbit of $x$ under $\mathfrak{o}$ fills $A_n$), we obtain an isomorphism $\mathfrak{o}/\pi^n\mathfrak{o} \cong A_n$. Hence $A_n$ is free of rank $1$ over $\mathfrak{o}/\pi^n\mathfrak{o}$.

For the cardinality: since $[\pi]_f(X) \equiv X^q \pmod{\pi}$, the degree of $[\pi^n]_f$ as a power series is $q^n$, so the equation $[\pi^n]_f(x) = 0$ has $q^n$ solutions in $\overline{\mathfrak{m}}$. By induction, there exist $q^n - q^{n-1}$ primitive $\pi^n$-torsion points.

(ii) The action of $G = \operatorname{Gal}(K(A_n)/K)$ on $A_n$ commutes with the $\mathfrak{o}$-action, giving a representation $\chi: G \to \operatorname{Aut}_{\mathfrak{o}}(A_n) \cong (\mathfrak{o}/\pi^n\mathfrak{o})^*$. The extension is totally ramified because the ramification index equals the degree (both are $q^{n-1}(q-1)$). The map is surjective by counting: the order of $G$ is $[K(A_n):K] = q^{n-1}(q-1) = |(\mathfrak{o}/\pi^n\mathfrak{o})^*|$, and $\chi$ is injective since a Galois automorphism fixing $A_n$ pointwise fixes the generating set of $K(A_n)$.

(iii) The degree follows from the cardinality of $(\mathfrak{o}/\pi^n\mathfrak{o})^*$, which is $q^{n-1}(q-1)$. Since the extension is totally ramified of this degree, $K(A_n)/K$ is a totally ramified abelian extension.
