---
role: proof
locale: en
of_concept: serre-duality-for-differential-forms
source_book: gtm052
source_chapter: "III"
source_section: "7"
---

Indeed, for any $p$, we have $\Omega^{n-p} \cong (\Omega^p)^\vee \otimes \omega_X$ by (II, Ex. 5.16b), where $\omega_X$ is the canonical sheaf. Applying Serre duality (7.7) to the coherent sheaf $\Omega^p$ gives

$$H^q(X, \Omega^p) \cong \operatorname{Ext}^{n-q}(\Omega^p, \omega_X)^\vee \cong H^{n-q}(X, (\Omega^p)^\vee \otimes \omega_X)^\vee \cong H^{n-q}(X, \Omega^{n-p})^\vee,$$

where the middle isomorphism uses (6.3) and (6.7), and the last follows from the identification $\Omega^{n-p} \cong (\Omega^p)^\vee \otimes \omega_X$.
