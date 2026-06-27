---
role: proof
locale: en
of_concept: classification-locally-finite-homogeneous-geometry
source_book: gtm053
source_chapter: "6 Geometric Stability Theory"
source_section: "6.5 Theorem"
---

The proof of Theorem 6.5 is based, as is the proof of Theorem 6.4, on a combinatorial-geometric analysis using delicate calculations with model-theoretic ranks. The main steps are:

\begin{enumerate}
\item \textbf{Exclude pseudoplanes.} The primary goal is to show that a locally finite homogeneous geometry cannot contain a definable pseudoplane. One develops an intersection theory on a pseudoplane, analogous to B\'ezout's theorem in algebraic geometry. By counting intersections and using the rank (dimension) calculations, one arrives at a numerical contradiction if a pseudoplane were present.
\item \textbf{Apply the weak trichotomy.} Once pseudoplanes are excluded, the geometry must be locally modular (by the weak trichotomy theorem, Theorem 6.4). Together with local finiteness, this forces the geometry to be of one of the three listed types.
\item \textbf{Local finiteness excludes fields.} The local finiteness condition $\operatorname{cl}(U)$ finite for finite $U$ eliminates algebraically closed fields (type 6.3(3)), since in ACF the algebraic closure of a finite set is infinite.
\item \textbf{Classification of locally modular locally finite geometries.} The remaining locally modular geometries are classified as either trivial, projective over a finite field, or affine over a finite field. The finiteness of the field follows from local finiteness of the geometry.
\end{enumerate}

A refinement of this method led to a similar classification of all finite homogeneous geometries starting from dimension 7.
