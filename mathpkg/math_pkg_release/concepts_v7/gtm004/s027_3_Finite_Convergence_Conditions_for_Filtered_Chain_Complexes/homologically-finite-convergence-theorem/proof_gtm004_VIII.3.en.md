---
role: proof
locale: en
of_concept: homologically-finite-convergence-theorem
source_book: gtm004
source_chapter: "VIII"
source_section: "3"
---

# Proof of Homologically Finite Filtration Implies Finite Convergence of the Spectral Sequence

Assume that the filtration of the chain complex $C$ is homologically finite, i.e., for each $q$ there exist $p_0, p_1$ such that

* (3.9)(i) $H_q(C^{(p)}) = 0$ for $p \le p_0$,
* (3.9)(ii) $H_q(C^{(p)}) = H_q(C)$ for $p \ge p_1$.

We prove the three conclusions in order.

---

**Proof of (i) — finite convergence.** Recall that the bigraded object $D$ is given by $D^{p,q} = H_{p+q}(C^{(p)})$ in the convention of (2.9) (or with suitable index adjustment). Condition (3.9) then implies that $D$ is both positively and negatively graded (in each total degree). By Proposition 3.2, $\alpha$ is stationary, and by Theorem 3.1, the associated spectral sequence converges finitely. This establishes (i).

---

**Proof of (ii) — finiteness of the induced filtration on $H(C)$.** The induced filtration on $M = H(C)$ is defined by

$$M^{(p)} = \operatorname{im}\bigl(H(C^{(p)}) \to H(C)\bigr).$$

From (3.9)(i), there exists $p_0$ such that $H_q(C^{(p)}) = 0$ for all $p \le p_0$ and all $q$; hence $M^{(p)} = 0$ for $p \le p_0$. From (3.9)(ii), there exists $p_1$ such that $H_q(C^{(p)}) = H_q(C)$ for all $p \ge p_1$ and all $q$; the inclusion then induces the identity on homology, so $M^{(p)} = H(C)$ for $p \ge p_1$. Thus the induced filtration

$$\cdots \subseteq M^{(p-1)} \subseteq M^{(p)} \subseteq M^{(p+1)} \subseteq \cdots$$

is finite.

---

**Proof of (iii) — the isomorphism $E_\infty \cong \operatorname{Gr} \circ H(C)$.** We fix $p, q$ and work with the $n$-th derived exact couple for $n$ sufficiently large, so that $E_n^{p,q} = E_\infty^{p,q}$ by (i).

Recall from the iterated construction of the exact couple that

$$D_n^{p+n,q} = \alpha^n D^{p,q} = \operatorname{im} H_q(C^{(p)}) \subseteq H_q(C^{(p+n)}).$$

By (3.9)(ii), for $n$ sufficiently large, $H_q(C^{(p+n)}) = H_q(C)$, and therefore

$$D_n^{p+n,q} = \operatorname{im} H_q(C^{(p)}) \subseteq H_q(C).$$

Similarly, for $n$ large,

$$D_n^{p+n-1,q} = \operatorname{im} H_q(C^{(p-1)}) \subseteq H_q(C),$$

and the map $\alpha_n: D_n^{p+n-1,q} \to D_n^{p+n,q}$ is then just the inclusion

$$\operatorname{im} H_q(C^{(p-1)}) \subseteq \operatorname{im} H_q(C^{(p)}),$$

i.e., the inclusion $H_q(C)^{(p-1)} \subseteq H_q(C)^{(p)}$ in the induced filtration.

Furthermore,

$$D_n^{p-1,q-1} = \alpha^n D^{p-n-1,q-1} = \operatorname{im} H_{q-1}(C^{(p-n-1)}) \subseteq H_{q-1}(C^{(p-1)}).$$

For $n$ large, $p-n-1 \le p_0$ (the bound from (3.9)(i)), so $H_{q-1}(C^{(p-n-1)}) = 0$, and hence $D_n^{p-1,q-1} = 0$.

Now consider the exact sequence of the $n$-th derived couple:

$$D_n^{p+n-1,q} \xrightarrow{\alpha_n} D_n^{p+n,q} \xrightarrow{\beta_n} E_n^{p,q} \xrightarrow{\gamma_n} D_n^{p-1,q-1}.$$

Since $\gamma_n$ maps into the zero object $D_n^{p-1,q-1} = 0$, the map $\beta_n$ is surjective. Its kernel is the image of $\alpha_n$, which is precisely $\operatorname{im} H_q(C^{(p-1)})$. Therefore $\beta_n$ induces an isomorphism

$$\frac{\operatorname{im} H_q(C^{(p)})}{\operatorname{im} H_q(C^{(p-1)})} \;\cong\; E_n^{p,q} = E_\infty^{p,q}.$$

But the left-hand side is by definition

$$(\operatorname{Gr} \circ H_q(C))_p = H_q(C)^{(p)} / H_q(C)^{(p-1)}.$$

Thus we obtain

$$E_\infty^{p,q} \cong (\operatorname{Gr} \circ H_q(C))_p,$$

which completes the proof of (iii) and of the theorem. $\square$
