---
role: proof
locale: en
of_concept: grothendieck-spectral-sequence
source_book: gtm004
source_chapter: "VIII"
source_section: "9"
---

# Proof of Grothendieck Spectral Sequence

Take an injective resolution of $A$ in $\mathfrak{A}$,

$$I: I_0 \rightarrow I_1 \rightarrow I_2 \rightarrow \cdots. \tag{9.11}$$

Apply $F$ to obtain the cochain complex $FI$ in $\mathfrak{B}$,

$$FI_0 \rightarrow FI_1 \rightarrow FI_2 \rightarrow \cdots.$$

By Lemma 9.4, we construct an injective resolution of the cochain complex $FI$ in $\mathfrak{B}$, yielding a double complex $J$ together with an augmentation $FI \rightarrow J$ of the form

$$
\begin{array}{c}
J_{0,0} \rightarrow J_{1,0} \rightarrow J_{2,0} \rightarrow \cdots\\
\downarrow \quad \downarrow \quad \downarrow\\
J_{0,1} \rightarrow J_{1,1} \rightarrow J_{2,1} \rightarrow \cdots\\
\downarrow \quad \downarrow \quad \downarrow\\
J_{0,2} \rightarrow J_{1,2} \rightarrow J_{2,2} \rightarrow \cdots\\
\downarrow \quad \downarrow \quad \downarrow\\
\vdots \quad \vdots \quad \vdots
\end{array}
\tag{9.12}
$$

where each column is an injective resolution and the horizontal short sequences are exact.

Apply $G$ to obtain the double (cochain) complex $B$,

$$
\begin{array}{c}
GJ_{0,0} \xrightarrow{d'} GJ_{1,0} \xrightarrow{d'} GJ_{2,0} \xrightarrow{\cdots}\\
\downarrow \quad \downarrow \quad \downarrow\\
GJ_{0,1} \xrightarrow{d'} GJ_{1,1} \xrightarrow{d'} GJ_{2,1} \xrightarrow{\cdots}\\
\downarrow \quad \downarrow \quad \downarrow\\
GJ_{0,2} \xrightarrow{d'} GJ_{1,2} \xrightarrow{d'} GJ_{2,2} \xrightarrow{\cdots}\\
\downarrow \quad \downarrow \quad \downarrow
\end{array}
\tag{9.13}
$$

**First spectral sequence.** We study the spectral sequence based on the first filtration (9.4) of $\operatorname{Tot} B$. Thus $_1 E_0^{p,q}$ is computed by applying the vertical differential, so we consider $H_{\text{vert}}(B_{p,*})$. Since the vertical differential in $J$ is injective and $F(I)$ is $G$-acyclic, the homology of each column of (9.13) is concentrated in the bottom row:

$$
_1 E_0^{p,q} = \begin{cases}
GFI_q, & p = q,\\
0, & p \neq q.
\end{cases}
$$

Computing $_1 E_1^{p,q}$, which applies the horizontal differential to $_1 E_0$, we obtain the cohomology of the complex

$$\cdots \rightarrow GFI_{q-1} \rightarrow GFI_q \rightarrow GFI_{q+1} \rightarrow \cdots$$

which, by definition of the right derived functors, yields

$$
_1 E_1^{p,q} = \begin{cases}
R^q(GF)(A), & p = q,\\
0, & p \neq q.
\end{cases}
\tag{9.14}
$$

Now, by the dual of (2.11), $\deg d_r = (r+1, 1)$ for the $r^{\text{th}}$ differential $d_r$ of the spectral sequence. Since $_1 E_1^{p,q}$ is non-zero only on the diagonal $p = q$, any differential $d_r$ with $r \geq 1$ must map from a non-zero position to a zero position or vice versa. Thus

$$d_r = 0, \quad r \geq 1,$$

so that for all $r \geq 1$,

$$
_1 E_r^{p,q} = \begin{cases}
R^q(GF)(A), & p = q,\\
0, & p \neq q.
\end{cases}
$$

Consequently,

$$
_1 E_\infty^{p,q} = \begin{cases}
R^q(GF)(A), & p = q,\\
0, & p \neq q.
\end{cases}
\tag{9.17}
$$

Proposition 9.2 ensures that the (first) spectral sequence converges finitely, so $H^q(\operatorname{Tot} B)$ is (finitely) filtered by subobjects whose successive quotients are the terms $_1 E_\infty^{p,q}$ appearing on the line $p = q$. That is, $H^q(\operatorname{Tot} B)$ has a finite filtration

$$H^q(\operatorname{Tot} B) = \Phi^0 H^q \supseteq \Phi^1 H^q \supseteq \cdots \supseteq \Phi^q H^q \supseteq 0$$

with $\Phi^p H^q / \Phi^{p+1} H^q \cong R^q(GF)(A)$ when $p = q$ and zero otherwise, whence each $H^q(\operatorname{Tot} B)$ is (after refiltration) simply $R^q(GF)(A)$.

**Second spectral sequence.** We now turn to the spectral sequence $E = {}_2 E$ based on the filtration (9.5). This time $E_0^{p,q}$ is computed by applying the horizontal differential to (9.13). By Lemma 9.4, specifically the exactness (9.21) and the decompositions (9.20), the horizontal homology of $GJ_{*,p}$ satisfies

$$H^{q-p}(GJ_{*,p}, d') = GK_{q-p,p} / GL_{q-p,p} = G(K_{q-p,p} / L_{q-p,p}).$$

Since $G$ is left exact (being a right-exact functor's derived functor context is irrelevant here — the exactness of $K_{r,s} \rightarrow J_{r,s} \rightarrow L_{r+1,s}$ combined with left exactness of $G$ yields the identification), we have

$$E_0^{p,q} = G(K_{q-p,p} / L_{q-p,p}).$$

Now $E_1^{p,q}$ is obtained by applying the vertical differential. Since each column of $J$ is an injective resolution, the vertical differential computes $R^p G$ of the augmentation. By the construction in Lemma 9.4, the augmented object at the head of column $p$ is precisely $Z_{q-p} / B_{q-p}$. In view of (9.20), (9.21), and (9.22), we obtain

$$E_1^{p,q} = R^p G(Z_{q-p} / B_{q-p}) = (R^p G)(R^{q-p}F)(A).$$

This is precisely the $E_1$-term claimed in (9.10).

Since the double complex (9.13) is positive (concentrated in non-negative indices), Proposition 9.2 guarantees good convergence of the second spectral sequence to the associated graded object of $H^*(\operatorname{Tot} B)$. But we have already determined, via the first spectral sequence, that $H^q(\operatorname{Tot} B) \cong R^q(GF)(A)$ (after appropriate filtration). Therefore the second spectral sequence converges to the graded object associated with $\{R^q(GF)(A)\}$, suitably filtered, and we have

$$E_1^{p,q} = (R^p G)(R^{q-p}F)(A) \Rightarrow R^q(GF)(A).$$

This completes the proof of Theorem 9.3. $\square$
