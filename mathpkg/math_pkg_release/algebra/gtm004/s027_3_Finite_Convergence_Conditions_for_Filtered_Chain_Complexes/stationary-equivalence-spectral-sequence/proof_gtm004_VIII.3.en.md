---
role: proof
locale: en
of_concept: stationary-equivalence-spectral-sequence
source_book: gtm004
source_chapter: "VIII"
source_section: "3"
---

# Proof of Equivalence of Stationarity, Grading, and Dual Stationarity in Exact Couples

We prove the equivalence of the three conditions:

* (i) $\alpha$ is positively stationary,
* (ii) $E$ is negatively graded,
* (iii) $\bar{\alpha}$ is positively stationary.

---

**(i) $\Rightarrow$ (ii):** In the course of proving Theorem 3.1 we observed that if $\alpha$ is positively stationary, then from the exact sequence

$$D^{p-1,q} \xrightarrow{\alpha} D^{p,q} \xrightarrow{\beta} E^{p,q} \xrightarrow{\gamma} D^{p-1,q-1} \xrightarrow{\alpha} D^{p,q-1},$$

the map $\alpha: D^{p-1,q} \to D^{p,q}$ is an isomorphism for $p$ sufficiently large, and likewise $\alpha: D^{p-1,q-1} \to D^{p,q-1}$ is an isomorphism for $p$ sufficiently large. Exactness forces $E^{p,q} = 0$ for all such large $p$. Hence, given $q$, $E^{p,q}$ can be non-zero only for $p$ bounded above; this means precisely that $E$ is negatively graded.

---

**(ii) $\Rightarrow$ (i):** Conversely, assume $E$ is negatively graded. Consider the exact sequence

$$E^{p,q+1} \xrightarrow{\gamma} D^{p-1,q} \xrightarrow{\alpha} D^{p,q} \xrightarrow{\beta} E^{p,q},$$

which is a segment of the exact couple (2.9). If $E$ is negatively graded, then for given $q$ (and $q+1$) there exists $p_0$ such that $E^{p,q+1} = 0 = E^{p,q}$ for all $p \le p_0$. For such $p$, exactness of the above sequence forces the middle map $\alpha: D^{p-1,q} \to D^{p,q}$ to be an isomorphism. Reindexing, $\alpha: D^{p,q} \to D^{p+1,q}$ is an isomorphism for all $p \le p_0 - 1$. This means $\alpha$ is positively stationary.

Thus (i) $\Leftrightarrow$ (ii).

---

**Equivalence with (iii):** The equivalence with (iii) follows by duality. The exact couple formed from $\bar{D}$,

$$\bar{D} \xrightarrow{\bar{\alpha}} \bar{D} \xrightarrow{\bar{\beta}} E,$$

with $\deg \bar{\alpha} = (1,0)$, $\deg \bar{\beta} = (-1,-1)$, $\deg \bar{\gamma} = (0,0)$, has the same formal properties as the original exact couple (2.9) with $D$ replaced by $\bar{D}$. Applying the already established equivalence (i) $\Leftrightarrow$ (ii) to this dual exact couple yields the equivalence between $\bar{\alpha}$ being positively stationary and $E$ being negatively graded. Hence (ii) $\Leftrightarrow$ (iii).

Combining both equivalences gives (i) $\Leftrightarrow$ (ii) $\Leftrightarrow$ (iii).

---

**Remark.** Of course, by interchanging "positive" and "negative" throughout, one obtains the dual statement: $\alpha$ is negatively stationary $\Leftrightarrow$ $E$ is positively graded $\Leftrightarrow$ $\bar{\alpha}$ is negatively stationary. $\square$
