---
role: proof
locale: en
of_concept: injective-resolution-of-cochain-complex
source_book: gtm004
source_chapter: "VIII"
source_section: "9"
---

# Proof of Injective Resolution of a Cochain Complex

Write $F_r$ for $FI_r$ and display the cocycles and coboundaries of the cochain-complex

$$F_0 \rightarrow F_1 \rightarrow F_2 \rightarrow \cdots$$

in the form

$$Z_0 \rightarrow F_0 \rightarrow B_1 \rightarrow Z_1 \rightarrow F_1 \rightarrow B_2 \rightarrow Z_2 \rightarrow F_2 \rightarrow \cdots. \tag{9.18}$$

We must construct a double complex $J$ of injectives together with an augmentation $FI \rightarrow J$ that is an injective resolution in the category of cochain complexes over $\mathfrak{B}$, relative to the class of monomorphisms that induce cohomology monomorphisms.

We already know (Lemma III.5.4; see also the proof of Theorem IV.6.1) how to resolve $Z_0 \rightarrow F_0 \rightarrow B_1$. Given the resolution of $B_1$, we choose an arbitrary resolution of $Z_1 / B_1$ and resolve $B_1 \rightarrow Z_1 \rightarrow Z_1 / B_1$. We thus obtain the first two rows of (9.19). Proceeding inductively, we construct the entire diagram

$$
\begin{array}{cccccc}
Z_0 & \rightarrow F_0 & \rightarrow B_1 & \rightarrow Z_1 & \rightarrow F_1 & \rightarrow B_2 \rightarrow \cdots\\
\downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow\\
K_{0,0} & \rightarrow J_{0,0} & \rightarrow L_{1,0} & \rightarrow K_{1,0} & \rightarrow J_{1,0} & \rightarrow L_{2,0} \rightarrow \cdots\\
\downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow\\
K_{0,1} & \rightarrow J_{0,1} & \rightarrow L_{1,1} & \rightarrow K_{1,1} & \rightarrow J_{1,1} & \rightarrow L_{2,1} \rightarrow \cdots\\
\downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots
\end{array}
\tag{9.19}
$$

where each column is an (augmented) injective resolution of the object appearing at its head.

By construction, the short exact sequences

$$L_{r,s} \rightarrowtail K_{r,s} \twoheadrightarrow \text{(something)}$$

are split, and consequently the horizontal sequences

$$K_{r,s} \rightarrow J_{r,s} \rightarrow L_{r+1,s}$$

are exact. In fact, the construction yields a direct-sum decomposition

$$J_{r,s} \cong L_{r,s} \oplus K_{r,s} \tag{9.20}$$

compatible with the horizontal differentials, and the exactness

$$K_{r,s} \rightarrow J_{r,s} \rightarrow L_{r+1,s} \tag{9.21}$$

follows because $L_{r,s} \hookrightarrow K_{r,s}$ splits.

Finally, we recall that by definition of the cocycles and coboundaries of the complex $FI$,

$$Z_r / B_r = R^r F(A). \tag{9.22}$$

The vertical differentials $\delta''_{r,s} : J_{r,s} \rightarrow J_{r,s+1}$ are defined so as to make the augmented columns injective resolutions. The horizontal differentials $d'_{r,s} : J_{r,s} \rightarrow J_{r+1,s}$ are induced by the horizontal maps in (9.19). With these differentials, $J$ becomes a double complex resolving $FI$, as required in (9.12) for the proof of Theorem 9.3. $\square$
