---
role: proof
locale: en
of_concept: character-space-compactness
source_book: gtm015
source_chapter: "52"
source_section: "52.9"
---

# Proof of Compactness of the character space

**Proof.** (i) By (52.7), every character $f \in \mathcal{X}$ satisfies $\|f\| = 1$, so $\mathcal{X}$ is a subset of the closed unit ball of $A'$. The weak* topology on the unit ball is compact by Alaoglu's theorem. It remains to show that $\mathcal{X}$ is weak* closed.

Suppose $(f_\alpha)$ is a net in $\mathcal{X}$ converging weak* to $f \in A'$. Then $f(1) = \lim f_\alpha(1) = 1$, and for any $x, y \in A$, $f(xy) = \lim f_\alpha(xy) = \lim f_\alpha(x)f_\alpha(y) = f(x)f(y)$. Thus $f$ is an algebra homomorphism with $f \neq 0$, so $f$ is a character (since $\mathbb{C}$ is a field, any nonzero homomorphism to $\mathbb{C}$ is surjective). Hence $\mathcal{X}$ is weak* closed, therefore compact.

(ii) Every character $f$ has kernel $M = \ker f$, which is a maximal ideal (since $A/M \cong \mathbb{C}$ is a field). Conversely, every maximal ideal $M$ is closed (52.3) and $A/M$ is a Banach algebra which is a field; by Gelfand-Mazur, $A/M \cong \mathbb{C}$, giving the character $f_M$.
