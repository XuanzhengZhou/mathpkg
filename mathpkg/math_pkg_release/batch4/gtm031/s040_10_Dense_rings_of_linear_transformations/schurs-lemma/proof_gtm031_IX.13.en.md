---
role: proof
locale: en
of_concept: schurs-lemma
source_book: gtm031
source_chapter: "IX"
source_section: "13"
---
Let $B$ be any non-zero element in $\mathfrak{B}$. First, consider the image group $\mathfrak{R}B$. For any $A \in \mathfrak{A}$, we have $(\mathfrak{R}B)A = \mathfrak{R}(BA) = \mathfrak{R}(AB) = (\mathfrak{R}A)B \subseteq \mathfrak{R}B$, so $\mathfrak{R}B$ is invariant under $\mathfrak{A}$. Since $B \neq 0$, we have $\mathfrak{R}B \neq 0$, and by the irreducibility of $\mathfrak{A}$, this forces $\mathfrak{R}B = \mathfrak{R}$. Thus $B$ is surjective.

Next, let $\mathfrak{K}$ be the kernel of $B$. For any $A \in \mathfrak{A}$ and $x \in \mathfrak{K}$, we have $(xA)B = x(AB) = x(BA) = (xB)A = 0A = 0$, so $xA \in \mathfrak{K}$. Thus $\mathfrak{K}$ is an $\mathfrak{A}$-invariant subgroup. Since $B \neq 0$, we have $\mathfrak{K} \neq \mathfrak{R}$, so by irreducibility $\mathfrak{K} = 0$. Thus $B$ is injective.

We have shown that every non-zero $B \in \mathfrak{B}$ is a bijective endomorphism, hence an automorphism of $\mathfrak{R}$. The inverse $B^{-1}$ commutes with every $A \in \mathfrak{A}$ because $AB^{-1} = B^{-1}(BA)B^{-1} = B^{-1}(AB)B^{-1} = B^{-1}A$. Therefore $B^{-1} \in \mathfrak{B}$, proving that $\mathfrak{B}$ is a division ring.
