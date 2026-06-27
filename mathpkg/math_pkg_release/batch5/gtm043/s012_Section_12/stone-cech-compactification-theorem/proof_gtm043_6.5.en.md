---
role: proof
locale: en
of_concept: stone-cech-compactification-theorem
source_book: gtm043
source_chapter: "6"
source_section: "6.5"
---

**Uniqueness.** By Theorem 6.4, if $T$ satisfies one of (I)--(V), it satisfies all of them. By (I), the identity mapping on $X$, which is a continuous mapping into the compact space $T$, has a Stone extension from all of $\beta X$ into $T$; similarly, it has a Stone extension from $T$ into $\beta X$. It follows, as was pointed out in 0.12(a), that these extensions are homeomorphisms onto.

**Construction of $\beta X$.** There is to be a one-one correspondence between the $z$-ultrafilters $A^p$ on $X$ and the points $p$ of $\beta X$, with $p$ corresponding to $A_p = Z[M_p]$. The topology on $\beta X$ will be defined in such a way that $p$ is the limit of the $z$-ultrafilter $A_p$ for every $p \in \beta X$, not only for $p \in X$.

In what follows, $Z$ will always stand for a zero-set in the given topological space $X$. Let us write

$$\bar{Z} = \{p \in \beta X : Z \in A_p\},$$

that is, $p \in \bar{Z}$ if and only if $Z \in A_p$. Since $X$ itself belongs to every $z$-ultrafilter, we have $\bar{X} = \beta X$.

We know that $Z_1 \cup Z_2 \in A_p$ if and only if $Z_1 \in A_p$ or $Z_2 \in A_p$; therefore

$$\bar{Z}_1 \cup \bar{Z}_2 = \overline{Z_1 \cup Z_2}.$$

And since $\emptyset$ belongs to no $z$-ultrafilter, $\bar{\emptyset} = \emptyset$. Thus, the family of sets $\bar{Z}$ is closed under finite union and contains the empty set.

$\beta X$ is made into a topological space by taking the family of all sets $\bar{Z}$ as a base for the closed sets.

**$X$ is a subspace.** $p \in \bar{Z} \cap X$ if and only if $Z \in A_p$, which is to say that $p \in Z$. So $\bar{Z} \cap X = Z$. Thus, the identity mapping on $X$ carries the family of basic closed sets in the relative topology onto a family of basic closed sets in the original completely regular topology (see Theorem 3.2); therefore it is a homeomorphism.

**$X$ is dense in $\beta X$.** We prove, more generally, that

$$\operatorname{cl}_{\beta X} Z = \bar{Z},$$

from which the conclusion $\operatorname{cl}_{\beta X} X = \bar{X} = \beta X$ follows. By Theorem 2.6(b), distinct $z$-ultrafilters contain disjoint zero-sets. By 1.15(a), there exist a zero-set $Z$ disjoint from $A$, and a zero-set $Z'$ disjoint from $A'$, such that $Z \cup Z' = X$. Evidently, $Z \notin A^p$ and $Z' \notin A^{p'}$; that is to say, $p \notin \operatorname{cl} Z$ and $p' \notin \operatorname{cl} Z'$. Since

$$\operatorname{cl} Z \cup \operatorname{cl} Z' = \beta X,$$

the neighborhoods $\beta X - \operatorname{cl} Z$ of $p$, and $\beta X - \operatorname{cl} Z'$ of $p'$, are disjoint.

**Compactness.** Consider any collection of basic closed sets $\operatorname{cl} Z$ with the finite intersection property, $Z$ ranging over some family $\mathcal{B}$. By (IV), already established, $\mathcal{B}$ itself also has the finite intersection property. Consequently, $\mathcal{B}$ is embeddable in a $z$-ultrafilter $A^p$, and we have

$$p \in \bigcap_{Z \in A^p} \operatorname{cl} Z \subset \bigcap_{Z \in \mathcal{B}} \operatorname{cl} Z,$$

so that the latter intersection is nonempty. Therefore $\beta X$ is compact.

**Equivalence of (I)--(V).** The equivalence follows from Theorem 6.4, since conditions (I)--(V) correspond to conditions (2), (1), (3), (4), (5) respectively, applied to $T = \beta X$.
