---
role: proof
locale: en
of_concept: lemma-7-2
source_book: gtm040
source_chapter: "7"
source_section: "2"
---

**Proof:** It suffices to prove the lemma for the case where $\mu$ is a measure, since the general case follows by taking differences. Let $K_n$ denote the closed ball about the origin of radius $n$, and form

$$\int_{K_n} g(x)dx = \frac{1}{2\pi} \int_{K_n} \int_{R^3} \frac{1}{|x - y|} d\mu(y)dx.$$

By Fubini's Theorem we may interchange the order of integration to get

$$\int_{K_n} g(x)dx = \frac{1}{2\pi} \int_{R^3} \left[ \int_{K_n} \frac{1}{|x - y|} dx \right] d\mu(y).$$

The inside integral on the right is bounded by its value at the origin, which is some finite number $c$. Thus the right side does not exceed

$$\frac{1}{2\pi} c\mu(R^3) < \infty,$$

and $g$ must be finite a.e. on $K_n$. Since the countable union of the sets $K_n$ is $R^3$, we conclude that $g$

The class of theorems relating charges and potentials and quantities definable in terms of them and properties of $R^3$ is called classical potential theory. The operator transforming a charge into its potential is called the potential operator. The kernel of the potential operator is called the Green's function.

As we have defined it, potential theory contains the subject known in physics as electrostatics. Our definition includes the notions of distance, charge, and potential, and all the quantities commonly arising in electrostatics are definable in terms of these three notions. As an illustration, Table 7-1 shows how some of the quantities arising in electrostatics are related dimensionally to distance, charge, and potential. The table uses the notation

$$\text{distance} = x \quad \text{distance} = x$$
$$\text{time} = t \quad \text{and} \quad \text{charge} = q$$
$$\text{mass} = m \quad \text{potential} = V$$
$$\text{charge} = q$$

Table 7-1. Dimensions of Electrostatic Concepts

| Concept | Dimensions | Potential-Theoretic Dimensions |
| :--- | :--- | :--- |
| Capacity | $q^2 t^2/mx^2$ | $q/V$ |
| Charge | $q$ | $q$ |
| Energy | $mx^2/t^2$ | $Vq$ |
| Field | $mx/t^2q$ | $V/x$ |
| Force | $mx/t^2$ | $Vq/x$ |
| Potential | $mx^2/t^2q$ | $V$ |

We give four examples to illustrate how concepts may be defined explicitly in terms of distance, charge, and potential.

(1) We can reasonably ask what the total amount of work required to assemble a charge distribution is if only an "infinitesimal" amount of charge is brought into position at one time. The way to compute this amount of work is to integrate the potential function against the charge distribution, provided the integral exists. Thus we define the energy of a charge distribution to be the integral of its potential with respect to the charge, provided the integral exists.

(2) The total charge of a charge distribution $\mu$ is $\mu(R^3)$.

(3) If a

among all charges $\mu$ with total charge $q$ and with $\mu$ vanishing away from the set where the metal is, and this situation is referred to as equilibrium. We define an equilibrium potential for a closed set $E$ to be a potential which is 1 on $E$ and which comes from a charge distribution which has all its charge on $E$. An equilibrium set is a set which has an equilibrium potential.

(4) The capacity of a conductor in $R^3$ is defined as the total amount of charge needed to produce a unit potential on the set where the conductor is. We thus define the capacity of any equilibrium set to be the total charge of a charge distribution producing an equilibrium potential.

To indicate the directions in which classical potential theory leads, we shall state without proof some of the theorems in the subject. The support of a charge is defined to be the complement of the union of all open sets $U$ with the property that the charge vanishes on $U$ and every measurable subset of $U$.

(1) Uniqueness of charge: A potential uniquely determines its charge.

(2) Determination of potential: A potential is completely determined by its values on the support of its charge.

(3) Uniqueness of equilibrium potential: A set $E$ has at most one equilibrium potential. (This assertion is a corollary of (2).)

(4) Characterization of equilibrium potential: The equilibrium potential for an equilibrium set $E$ is equivalent to the pointwise infimum of all potentials which have non-negative charges and which dominate the constant function 1 on $E$.

(5) Principle of domination: Let $h$ and $g$ be potentials arising from non-negative charges $\bar{\mu}$ and $\mu$, respectively. If $h$ dominates $g$ on the support of $\mu$, then $h$ dominates $g$ everywhere and $\bar{\mu}(R^3) \geq \mu(R^3)$.
