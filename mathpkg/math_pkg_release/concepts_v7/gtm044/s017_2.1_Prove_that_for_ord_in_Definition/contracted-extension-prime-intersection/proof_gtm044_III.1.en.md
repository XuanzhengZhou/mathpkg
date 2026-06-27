---
role: proof
locale: en
of_concept: contracted-extension-prime-intersection
source_book: gtm044
source_chapter: "III"
source_section: "1"
---

# Proof of Contracted Extension is Intersection of Contained Prime Ideals

**Theorem 3.14.** For each ideal $a \in \mathcal{J}(R)$, $a^{ec}$ is the intersection of those prime ideals which contain $a$ and which are contained in $\mathfrak{p}$. (The intersection of an empty set of prime ideals is defined to be $R$.) Thus if $a \subset R = R_V$ defines the subvariety $X$ of $V$ (and $\mathfrak{p}$ defines $W$), then $a^{ec}$ defines $X_{(W)}$---that is, the mapping $a \mapsto a^{ec}$ geometrically corresponds to taking the germ at $W$ of $X$. In particular, the image of $\mathcal{J}(R_{\mathfrak{p}})$ under contraction consists precisely of $R$ together with those ideals in $\mathcal{J}(R)$ which are intersections of prime ideals contained in $\mathfrak{p}$.

*Proof.* Since $a \in \mathcal{J}(R)$ is a closed (radical) ideal, it can be written as an intersection of prime ideals:

$$a = \mathfrak{p}_1 \cap \mathfrak{p}_2 \cap \cdots \cap \mathfrak{p}_r,$$

where each $\mathfrak{p}_i$ is prime in $R$. (This is the prime decomposition of a radical ideal in a Noetherian ring.)

Now consider the behavior of each $\mathfrak{p}_i$ under extension and contraction:

- If $\mathfrak{p}_i \subset \mathfrak{p}$, then by Theorem 3.10 (a prime ideal is irreducible), we have $\mathfrak{p}_i^{ec} = \mathfrak{p}_i$.

- If $\mathfrak{p}_i \not\subset \mathfrak{p}$, then there exists an element $s \in \mathfrak{p}_i \setminus \mathfrak{p}$. In $R_{\mathfrak{p}}$, the element $s/1$ is a unit (since $s \notin \mathfrak{p}$), and $s/1 \in \mathfrak{p}_i^e$. Hence $\mathfrak{p}_i^e = R_{\mathfrak{p}}$, and consequently $\mathfrak{p}_i^{ec} = R$.

Since both extension $(\cdot)^e$ and contraction $(\cdot)^c$ preserve finite intersections (equation (13) and its analogue for contraction), we obtain

$$a^{ec} = \left( \bigcap_{i=1}^{r} \mathfrak{p}_i \right)^{ec} = \bigcap_{i=1}^{r} \mathfrak{p}_i^{ec} = \bigcap_{\substack{i=1 \\ \mathfrak{p}_i \subset \mathfrak{p}}}^{r} \mathfrak{p}_i,$$

where intersections over an empty set are interpreted as $R$. This is precisely the intersection of those prime ideals containing $a$ (since all $\mathfrak{p}_i$ in the decomposition contain $a$) that are contained in $\mathfrak{p}$.

Geometrically, if $a$ defines the subvariety $X = V(a) \subset V$, and $\mathfrak{p}$ defines the irreducible subvariety $W = V(\mathfrak{p})$, then $a^{ec}$ defines the union of those irreducible components of $X$ that contain $W$, which is precisely $X_{(W)}$. This is the algebraic counterpart of taking the germ at $W$.

For the final statement: the image of $\mathcal{J}(R_{\mathfrak{p}})$ under contraction consists of ideals of the form $a^{*c}$ where $a^* \in \mathcal{J}(R_{\mathfrak{p}})$. By (8), $a^* = (a^{*c})^e$, so $a^{*c} = a^{*c ec}$. Thus contracted ideals from $R_{\mathfrak{p}}$ are precisely the ideals of the form $b^{ec}$ for $b \in \mathcal{J}(R)$, which by the theorem are exactly $R$ and intersections of primes contained in $\mathfrak{p}$. $\square$
