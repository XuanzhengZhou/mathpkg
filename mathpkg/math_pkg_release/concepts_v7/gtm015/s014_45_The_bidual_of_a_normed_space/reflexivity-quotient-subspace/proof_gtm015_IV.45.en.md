---
role: proof
locale: en
of_concept: reflexivity-quotient-subspace
source_book: gtm015
source_chapter: "IV"
source_section: "45"
---

# Proof of Reflexivity of Subspaces and Quotients

Let $E$ be a normed space and $M$ a closed linear subspace. We prove: $E$ is reflexive $\iff$ $M$ and $E/M$ are reflexive.

**($\Rightarrow$) Suppose $E$ is reflexive.**

*$M$ is reflexive:* Let $\varphi \in M''$. Compose with the restriction map $E' \to M'$ (dual of the inclusion $M \hookrightarrow E$) to get a functional on $E'$, which by reflexivity of $E$ corresponds to some $x \in E$. One checks that $x$ must belong to $M$ (using that $M$ is closed and $\varphi$ vanishes on $M^\perp$), so $\varphi$ is the canonical image of $x \in M$. Thus $M$ is reflexive.

*$E/M$ is reflexive:* The dual of $E/M$ is isometrically isomorphic to $M^\perp \subset E'$. The dual of $M^\perp$ is isometrically isomorphic to $E''/(M^\perp)^\perp$. Since $E$ is reflexive, $E'' = E_0$ (canonical image of $E$). Under this identification, $(M^\perp)^\perp = M$, so $(E/M)'' \cong E/M$, proving reflexivity of $E/M$.

**($\Leftarrow$) Suppose $M$ and $E/M$ are reflexive.**

Let $\varphi \in E''$. Consider the restriction $\varphi|_{M^\perp} \in (M^\perp)'$. By reflexivity of $E/M$, $(E/M)'' \cong E/M$, which gives a coset $x + M$ corresponding to $\varphi|_{M^\perp}$. Lift to some $x \in E$. Then $\varphi - x''$ vanishes on $M^\perp$, so it factors through $(E/M)' \cong M^\perp$? Actually a more precise argument: Since $M$ and $E/M$ are reflexive, the dual sequence $0 \to M^\perp \to E' \to M' \to 0$ yields by double dualization an isomorphism $E'' \cong M'' \oplus (E/M)'' \cong M \oplus E/M \cong E$, showing $E$ is reflexive. $\square$
