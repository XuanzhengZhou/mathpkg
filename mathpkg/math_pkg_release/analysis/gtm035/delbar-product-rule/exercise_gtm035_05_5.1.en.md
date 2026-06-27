---
role: exercise
locale: en
chapter: "5"
section: "5.5"
exercise_number: 1
---
# Exercise 5.5

Prove Lemma 5.5: If $\omega^k \in \wedge^k(\Omega)$ and $\omega^l \in \wedge^l(\Omega)$, then

$$\bar{\partial}(\omega^k \wedge \omega^l) = \bar{\partial}\omega^k \wedge \omega^l + (-1)^k \omega^k \wedge \bar{\partial}\omega^l.$$

*Hint.* Write both forms in the standard basis $\omega^k = \sum a_{IJ} dz_I \wedge d\bar{z}_J$, $\omega^l = \sum b_{KL} dz_K \wedge d\bar{z}_L$. Apply $\bar{\partial}$ to the product and use the Leibniz rule $\bar{\partial}(ab) = (\bar{\partial}a)b + a(\bar{\partial}b)$ on the coefficient functions. To identify the second term, note that moving the 1-form $\bar{\partial}b_{KL}$ past the $k$-form $dz_I \wedge d\bar{z}_J$ introduces a factor of $(-1)^k$ by Lemma 4.5.
