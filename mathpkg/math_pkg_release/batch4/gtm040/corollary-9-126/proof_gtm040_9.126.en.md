---
role: proof
locale: en
of_concept: corollary-9-126
source_book: gtm040
source_chapter: "9"
source_section: "126"
---

**Proof:** Existence follows from Proposition 9-125 and uniqueness follows from Theorem 8-41.

Shortly we shall show exactly how general the class of chains that represent circuits is. But first we shall exhibit the connection between the currents and voltages of this section and the charges and potentials of Markov chain potential theory. In so doing, what we will be showing is that electric circuits provide a model for the discrete potential theory associated with the class of chains that represent circuits.

In physics, current is the time rate at which charge flows past a point—that is, the derivative of charge with respect to time. Markov chains, however, have a time scale that is discrete and not continuous, and the proper analog of the time rate at which charge flows past a point is the amount of charge that moves past the point in unit time. With discrete time the charge moves to some point, stays for unit time, and then moves to another point. Hence the magnitude of the current at a point is equal to the magnitude of the accumulated charge at that point.

Now in a standard voltage problem, current flows in and out of the circuit through the terminals which are attached to the outside source. The above considerations lead us to define the **charge at terminal** $i$ to be the current $\mu_i$ which flows into the circuit; $\mu_i$ is taken to be negative

if the current flows out. By Kirchhoff's Law (2), the charge will be zero on the set $F - E$. For $i$ in $E \cup \tilde{F}$ the charge is given by

$$\mu_i = \sum_k (v_i - v_k) c_{ik}.$$

Before we can connect $\mu$ and $v$ in terms of the representing chain, we need one preliminary result.
