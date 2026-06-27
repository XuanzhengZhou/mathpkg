---
role: proof
locale: en
of_concept: infinite-cyclic-group-isomorphism
source_book: gtm030
source_chapter: "1"
source_section: "11"
---

Consider the mapping $\phi: I_+ \to \mathfrak{Z}$ defined by $\phi(n) = a^n$. Using the extended exponent laws, we have:
$$\phi(m+n) = a^{m+n} = a^m a^n = \phi(m)\phi(n).$$
Thus $\phi$ is a homomorphism. If $\phi$ is 1-1, then it is an injective homomorphism. Since the image $\phi(I_+)$ consists of all integral powers $a^n$, and $[a]$ is precisely the set of all such powers, $\phi$ is surjective onto $\mathfrak{Z}$. Hence $\phi$ is an isomorphism of $I_+$ onto $\mathfrak{Z}$.

If $\mathfrak{Z}$ is infinite, then the powers $a^n$ must all be distinct (otherwise $\mathfrak{Z}$ would be finite), so $\phi$ is 1-1 and thus an isomorphism.
