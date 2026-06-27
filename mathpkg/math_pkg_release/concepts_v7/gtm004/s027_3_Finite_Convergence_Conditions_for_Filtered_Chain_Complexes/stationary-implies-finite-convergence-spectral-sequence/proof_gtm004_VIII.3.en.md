---
role: proof
locale: en
of_concept: stationary-implies-finite-convergence-spectral-sequence
source_book: gtm004
source_chapter: "VIII"
source_section: "3"
---

# Proof of Stationary Exact Couple Implies Finite Convergence of the Spectral Sequence

Consider the exact sequence derived from the exact couple (2.9):

$$D^{p-1,q} \xrightarrow{\alpha} D^{p,q} \xrightarrow{\beta} E^{p,q} \xrightarrow{\gamma} D^{p-1,q-1} \xrightarrow{\alpha} D^{p,q-1}. \tag{3.1}$$

Fix a pair $(p, q)$. Since $\alpha$ is stationary, there exists $p_0$ such that for all $p \ge p_0$, the map $\alpha: D^{p,q} \to D^{p+1,q}$ is an isomorphism, and similarly there exists $p_1$ such that for all $p \le p_1$, the map $\alpha: D^{p,q} \to D^{p+1,q}$ is an isomorphism (the negative stationarity condition, applied at degree $q-1$, gives the analogous statement for $D^{p-1,q-1} \to D^{p,q-1}$).

Consequently, from the exact sequence (3.1), if both $\alpha|_{D^{p-1,q}}$ and $\alpha|_{D^{p-1,q-1}}$ are isomorphisms, then $E^{p,q} = 0$. It follows that $E^{p,q} \ne 0$ only for $p$ in a bounded range (depending on $q$). In particular, the bigraded object $E$ has only finitely many non-zero entries in each row $q$ and each column $p$.

Now recall that the differential on the $r$-th page is

$$d_r: E_r^{p,q} \longrightarrow E_r^{p+r, q-r+1}.$$

Since $E_r^{p,q}$ is a subquotient of $E^{p,q}$ and $E_r^{p+r,q-r+1}$ is a subquotient of $E^{p+r,q-r+1}$, and since for fixed $(p,q)$ and sufficiently large $r$, the target $E^{p+r,q-r+1}$ lies outside the bounded non-zero region of $E$, we must have $E_r^{p+r,q-r+1} = 0$ for $r$ sufficiently large. Hence $d_r^{p,q} = 0$ for all sufficiently large $r$. Similarly, the source of the incoming differential $d_r^{p-r,q+r-1}$ vanishes for large $r$.

Therefore, for sufficiently large $r$, the differentials into and out of $E_r^{p,q}$ are zero, and

$$E_r^{p,q} = E_{r+1}^{p,q} = \cdots = E_\infty^{p,q}.$$

This establishes that the spectral sequence converges finitely. $\square$
