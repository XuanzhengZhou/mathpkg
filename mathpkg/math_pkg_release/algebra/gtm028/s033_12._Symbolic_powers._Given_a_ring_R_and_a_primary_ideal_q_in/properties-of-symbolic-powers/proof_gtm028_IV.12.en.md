---
role: proof
locale: en
of_concept: properties-of-symbolic-powers
source_book: gtm028
source_chapter: "IV"
source_section: "12"
---

**Proof of (1).** The ideal $\mathfrak{q}^{(n)} = (\mathfrak{q}^n)^{ec}$ is the contraction of the ideal $(\mathfrak{q}^n)^e$ of $R_{\mathfrak{p}}$. Since contraction preserves the primary property and the associated prime (when the contracted ideal is proper), and $(\mathfrak{q}^n)^e$ is primary for $\mathfrak{p}^e$ in $R_{\mathfrak{p}}$, it follows that $\mathfrak{q}^{(n)}$ is primary for $\mathfrak{p}$ in $R$. The element-wise description follows from the definition of extension and contraction: an element $x$ belongs to $(\mathfrak{q}^n)^{ec}$ if and only if $x/1 \in (\mathfrak{q}^n)^e$ in $R_{\mathfrak{p}}$, which means there exists $d \notin \mathfrak{p}$ such that $dx \in \mathfrak{q}^n$. If $\mathfrak{q}^n$ is itself primary, then $\mathfrak{q}^n = (\mathfrak{q}^n)^{ec} = \mathfrak{q}^{(n)}$ by the properties of primary ideals under localization. In particular, if $\mathfrak{p}$ is maximal, every primary ideal belonging to $\mathfrak{p}$ has primary powers.

**Proof of (2).** If $\mathfrak{q}^n = \bigcap \mathfrak{q}_i$ is a finite intersection of primary ideals, then by the uniqueness theorems for primary decomposition, $\mathfrak{p}$ is the only isolated prime ideal of $\mathfrak{q}^n$. Under extension to $R_{\mathfrak{p}}$, all primary components belonging to imbedded primes become the unit ideal, and the isolated component corresponding to $\mathfrak{p}$ survives. Hence $(\mathfrak{q}^n)^e$ is the extension of that component, and its contraction $\mathfrak{q}^{(n)}$ is precisely that isolated primary component.

**Proof of (3).** If $\mathfrak{p}$ has a finite basis, then $\mathfrak{p}^n$ is contained in every primary ideal belonging to $\mathfrak{p}$ (for sufficiently large $n$), hence every such primary ideal contains $\mathfrak{p}^{(n)}$. In the noetherian case, the intersection $\bigcap_{n=1}^{\infty} \mathfrak{p}^{(n)}$ equals the intersection of all primary ideals belonging to $\mathfrak{p}$, which by primary decomposition theory is the intersection of primary components of $(0)$ contained in $\mathfrak{p}$. When $R$ is a noetherian domain, $(0)$ is prime, and its only primary component contained in $\mathfrak{p}$ is $(0)$ itself, so $\bigcap_{n=1}^{\infty} \mathfrak{p}^{(n)} = (0)$. The strict decreasing property follows from the fact that in a noetherian domain $\mathfrak{p}^{(n+1)} \subsetneq \mathfrak{p}^{(n)}$ for all $n$.

**Proof of (4).** We must show $(\mathfrak{q}^{(n)} \cdot \mathfrak{q}^{(m)})^{ec} = (\mathfrak{q}^{n+m})^{ec}$. Since $\mathfrak{q}^{(n)e} = (\mathfrak{q}^n)^e$, $\mathfrak{q}^{(m)e} = (\mathfrak{q}^m)^e$, we have $(\mathfrak{q}^{(n)} \cdot \mathfrak{q}^{(m)})^e = (\mathfrak{q}^n)^e \cdot (\mathfrak{q}^m)^e = (\mathfrak{q}^{n+m})^e$. Contracting both sides gives the desired equality.
