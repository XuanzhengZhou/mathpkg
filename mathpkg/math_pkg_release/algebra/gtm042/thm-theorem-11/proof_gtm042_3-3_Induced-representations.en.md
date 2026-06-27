---
role: proof
locale: en
of_concept: thm-theorem-11
source_book: gtm042
source_chapter: "3.3"
source_section: "Induced representations"
---

Let us first prove the existence of the induced representation $\rho$. In view of example 3, above, we may assume that $\theta$ is irreducible. In this case, $\theta$ is isomorphic to a subrepresentation of the regular representation of $H$, which can be induced to the regular representation of $G$ (cf. example 1). Applying example 4, we conclude that $\theta$ itself can be induced.

It remains to prove the uniqueness of $\rho$ up to isomorphism. Let $(V, \rho)$ and $(V', \rho')$ be two representations induced by $(W, \theta)$. Applying Lemma 1 to the injection of $W$ into $V'$, we see that there exists a linear map $F: V \rightarrow V'$ which is the identity on $W$ and satisfies $F \circ \rho_s = \rho_s' \circ F$ for all $s \in G$. Consequently the image of $F$ contains all the $\rho_s'$ $W$, and thus is equal to $V'$. Since $V'$ and $V$ have the same dimension $(G: H) \cdot \dim(W)$, we see that $F$ is an isomorphism, which proves the theorem. (For a more natural proof of Theorem 11, see 7.1.)

Character of an induced representation

Suppose $(V, \rho)$ is induced by $(W, \theta)$ and let $\chi_\rho$ and $\chi_\theta$ be the corresponding characters of $G$ and of $H$. Since $(W, \theta)$ determines $(V, \rho)$ up to isomorphism, we ought to be able to compute $\chi_\rho$ from $\chi

where $R_u$ denotes the set of $r \in R$ such that $r_u = r$ and $\rho_{u,r}$ is the restriction of $\rho_u$ to $\rho_r W$. Observe that $r$ belongs to $R_u$ if and only if $ur$ can be written $rt$, with $t \in H$, i.e., if $r^{-1}ur$ belongs to $H$.

It remains to compute $\text{Tr}_{\rho_r W}(\rho_{u,r})$, for $r \in R_u$. To do this, note that $\rho_r$ defines an isomorphism of $W$ onto $\rho_r W$, and that we have

$$\rho_r \circ \theta_t = \rho_{u,r} \circ \rho_r, \quad \text{with } t = r^{-1}ur \in H.$$

The trace of $\rho_{u,r}$ is thus equal to that of $\theta_t$, that is, to $\chi_\theta(t) = \chi_\theta(r^{-1}ur)$. We indeed obtain:

$$\chi_\rho(u) = \sum_{r \in R_u} \chi_\theta(r^{-1}ur).$$

The second formula given for $\chi_\rho(u)$ follows from the first by noting that all elements $s$ of $G$ in the left coset $rH (r \in R_u)$ satisfy $\chi_\theta(s^{-1}us) = \chi_\theta(r^{-1}ur).$

The reader will find other properties of induced representations in part II. Notably:

(i) The Frobenius reciprocity formula

$$\left(f_H | \chi_\theta\right)_H = \left(f | \chi_\rho\right)_G$$

where $f$ is a class function of $G$, and $f_H$ is its restriction to $H$, and the scalar products are calculated on $H$ and $G$ respectively.

(ii) Mackey's criterion, which tells us when an induced representation is irreducible.

(iii) Artin's theorem (resp. Brauer's theorem), which says that each character of a group $G$ is a linear combination with rational (resp. integral) coefficients of characters of representations induced from cyclic subgroups (resp. from "elementary" subgroups)
