---
role: proof
locale: en
of_concept: kaplansky-walker-direct-sum-c-generated
source_book: gtm013
source_chapter: "5"
source_section: "26"
---

Let $M = \oplus_A M_\alpha$ and suppose that each $M_\alpha$ is $c$-generated. Suppose also that $M = K \oplus L$ and let

$$(K_\beta)_{\beta \in B} \quad \text{and} \quad (L_\gamma)_{\gamma \in C}$$

denote the $c$-generated submodules of $K$ and $L$ respectively. Set

$$A' = \{\alpha \in A \mid M_\alpha \leq K_\beta \text{ or } M_\alpha \leq L_\gamma \text{ for some } \beta, \gamma\},$$

$$B' = \{\beta \in B \mid K_\beta \text{ is a direct summand of } K\},$$

$$C' = \{\gamma \in C \mid L_\gamma \text{ is a direct summand of } L\}.$$

We claim that $A = A'$. Suppose $A' \neq A$, and let $\alpha \in A \setminus A'$. By Lemma (25.7) each $c$-generated submodule of $M$ is contained in a sum of at most $c$ of the $M_\alpha$. In particular, if $D \subseteq A$ is of cardinality at most $c$, then both

$$(\oplus_D M_\delta)e \quad \text{and} \quad (\oplus_D M_\delta)f$$

are $c$-generated submodules of $M$ (where $e$ and $f$ are the projections onto $K$ and $L$), so their sum, also $c$-generated, is contained in a sum of at most $c$ of the $M_\alpha$. So by a standard induction argument it follows that there exists an increasing sequence

$$D_1 \subseteq D_2 \subseteq \ldots$$

of subsets of $A$ each of cardinality at most $c$ such that

$$M_\alpha \leq M_\alpha e + M_\alpha f \leq \oplus_{D_1} M_\delta,$$

$$\oplus_{D_1} M_\delta \leq (\oplus_{D_1} M_\delta)e + (\oplus_{D_1} M_\delta)f \leq \oplus_{D_2} M_\delta,$$

$$\vdots$$

$$\oplus_{D_n} M_\delta \leq (\oplus_{D_n} M_\delta)e + (\oplus_{D_n} M_\delta)f \leq \oplus_{D_{n+1}} M_\delta.$$

Set $D = \cup_{n=1}^{\infty} D_n$. Since the $M_\delta$ are independent and $\alpha \notin A'$, it is clear that $D \not\subseteq A'$. Note also that

$$(\oplus_D M_\delta)e \leq \oplus_D M_\delta \quad \text{and} \quad (\oplus_D M_\delta)f \leq \oplus_D M_\delta$$

and that $\oplus_D M_\delta$ is $c^2$-generated $= c$-generated. Now set

$$M' = \oplus_{A'} M_\alpha, \quad K' = \oplus_{B'} K_\beta, \quad L' = \oplus_{C'} L_\gamma.$$

Then by hypothesis $M' = K' \oplus L'$. Also set $N = \oplus_D M_\delta$. Then as above $N = Ne \oplus Nf$, so that $Ne$ and $Nf$ are $c$-generated submodules of $K$ and $L$ respectively. Moreover, $M_\alpha \leq Ne + Nf$ and $\alpha \notin A'$, which contradicts the definition of $A'$. Thus $A = A'$ as claimed, and it follows that every direct summand of $M$ is a direct sum of $c$-generated submodules.
