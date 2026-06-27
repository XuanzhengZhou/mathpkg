---
role: proof
locale: en
of_concept: spectral-sequence-double-limit
source_book: gtm004
source_chapter: "VIII"
source_section: "5"
---

# Proof of Double Limits of Spectral Sequences Commute

We work with an exact couple in an abelian category $\mathfrak{A}$:

$$
\begin{CD}
D @>{\alpha}>> D \\
@V{\gamma}VV @AA{\beta}A \\
E
\end{CD}
$$

and the associated spectral sequence $\{E_{m,n}\}$ (with the notations of Sections VIII.1 and VIII.4). Recall the maps

$$
\sigma_n: D_n \longrightarrow D_{n+1}, \qquad \varrho_n: D_{n+1} \longrightarrow D_n, \qquad \eta_n: D \longrightarrow D_n,
$$

and the $Q$-process $Q_\eta$, $Q^\nu$ defined in Section 4 (see (4.14), (4.15)). The goal is to establish that the double limit

$$
E_{\infty,\infty} = \lim_m \lim_n E_{m,n}
$$

is well-defined, that the two limiting processes commute, and that the limit terms fit into exact sequences as claimed.

*Proof.* We carry out the process in two stages, applying Theorem 5.2 and its dual.

**Step 1: The limit over $n$ (colimit direction).** Execute the process $Q^\nu$: this produces, for each fixed $m$, a tower of objects $\{E_{m,n}\}_{n \geq 0}$ linked by the differentials of the spectral sequence. The dual of Theorem 5.2 (applied to the colimit of a co-tower of pushout squares) establishes that

$$
E_{m,\infty} = \lim_n E_{m,n}
$$

exists and coincides with the description given in Section 1, namely $E_{m,\infty} = \bigcap_n E_{m,n}$ (interpreted as a limit in the abelian category). Moreover, for each $m$ we obtain an exact sequence

$$
D_m \xrightarrow{\alpha_m} D_m \xrightarrow{\beta_{m,\infty}} E_{m,\infty} \xrightarrow{\gamma_{m,\infty}} I \xrightarrow{\alpha''} I,
\tag{5.18}
$$

where the exactness follows exactly as in the proof of Theorem 4.5, adapted to the limit context.

**Step 2: The limit over $m$ (limit direction).** Now apply the process $Q_\eta$ to the system $\{E_{m,\infty}\}_{m \geq 0}$. Execute $Q_\eta^\nu$ as the composition $Q_\eta \circ Q^\nu$. We obtain the diagram

$$
\begin{array}{c}
U \xrightarrow{\alpha'} U \xrightarrow{\beta_{\infty,\infty}} E_{\infty,\infty} \xrightarrow{\gamma_{\infty,\infty}} I \xrightarrow{\alpha''} I \\[4pt]
D \xrightarrow{\alpha'} D \xrightarrow{\beta_{0,\infty}} E_{0,\infty} \xrightarrow{\gamma_{0,\infty}} I \xrightarrow{\alpha''} I \\[4pt]
D \xrightarrow{\alpha'} D \xrightarrow{\beta} E \xrightarrow{\gamma} D \xrightarrow{\alpha'} D
\end{array}
\tag{5.14}
$$

By Theorem 5.2 (applied directly, not dually),

$$
E_{0,\infty} = \lim_n E_{0,n} = \bigcap_n E_{0,n},
$$

which is precisely the subobject of $E$ designated as $E_{0,\infty}$ in Section 1. The identical argument applied to the $m$-th derived couple yields $E_{m,\infty}$ as defined in (4.19), coinciding with the earlier description.

Now we apply $Q_\eta$. Theorem 5.2 (in its original form) now establishes the top row of (5.14), yielding

$$
E_{\infty,\infty} = \lim_m E_{m,\infty} = \lim_m \lim_n E_{m,n},
$$

provided we verify the compatibility condition

$$
\begin{array}{c}
D_{n+1} \xrightarrow{\beta_{n+1,\infty}} E_{n+1,\infty} \\[4pt]
D_n \xrightarrow{\beta_{n,\infty}} E_{n,\infty}
\end{array}
\tag{5.15}
$$

which follows from the naturality of the $Q^\nu$-construction with respect to the maps $\varrho_n: D_{n+1} \to D_n$.

The exactness of the top row of (5.14) follows exactly as in the proof of Theorem 4.5: the kernel-cokernel exact sequence associated with the $Q$-process remains exact after passage to the limit because the limit functor is left exact, and the relevant constructions ($\operatorname{Ker}$, $\operatorname{Coker}$, $\operatorname{Im}$) are preserved under the limits in question.

**Step 3: The remaining limit terms.** The determinations of $E_{m,\infty}$, $E_\infty$, and $E_{\infty,n}$ (originally stated as (4.22), (4.23), (4.26)) now follow from the appropriate exact sequences:

$$
\begin{aligned}
D_m &\xrightarrow{\alpha_m} D_m \xrightarrow{\beta_{m,\infty}} E_{m,\infty} \xrightarrow{\gamma_{m,\infty}} I \xrightarrow{\alpha''} I, \\[4pt]
U &\xrightarrow{\alpha'} U \xrightarrow{\beta_\infty} E_\infty \xrightarrow{\gamma_\infty} I \xrightarrow{\alpha''} I, \\[4pt]
U &\xrightarrow{\alpha'} U \xrightarrow{\beta_{\infty,n}} E_{\infty,n} \xrightarrow{\gamma_{\infty,n}} D_n \xrightarrow{\alpha_n} D_n.
\end{aligned}
$$

These are obtained by passing to the limit starting from any derived couple of the given exact couple and applying Theorem 5.2 (or its dual) as appropriate. The key point is that the two limiting processes commute:

$$
\lim_m \lim_n E_{m,n} \cong \lim_n \lim_m E_{m,n} = E_{\infty,\infty},
$$

as established by the interchange theorem (Theorem 5.1). $\square$

**Remark.** Theorem 5.3 is valid in any abelian category in which the appropriate limits exist. No arguments essentially involving elements and diagram-chasing are required. The exact couple (1.1) ceases to be an exact couple "in the limit" but remains an exact sequence (5.18). This is because we are carrying out both limiting and colimiting processes; the remarkable fact, embedded in (5.11), is that these two processes commute in this special case arising from an exact couple. Trivial modifications of detail are needed in the case of a graded category (as explained at the end of Section 4), but these are straightforward and are omitted.
