---
role: proof
locale: en
of_concept: plh-maps-2-cell-in-simplex-boundary-to-face
source_book: gtm047
source_chapter: ""
source_section: "21"
---

**Proof.** First we take a (rectilinear) triangulation $K$ of $\operatorname{Bd} \sigma^3$, such that $D$ forms a subcomplex of $K$, and sufficiently fine so that for each $\tau^2 \in K$, $|\operatorname{St} \tau^2|$ avoids a 2-face of $\sigma^3$. (Here $\operatorname{St} \tau^2$ is the set of all simplexes of $K$ that intersect $\tau^2$, together with their faces.) Thus $|\operatorname{St} \tau^2|$ lies in a set of the type

$$d(\tau^2) = \operatorname{Cl}\left( \operatorname{Bd} \sigma^3 - \sigma^2 \right) \quad (\sigma^2 \in \sigma^3).$$

We take points $v, v'$, lying close to the "central vertex" of $d(\tau^2)$, with $v \in \operatorname{Int} \sigma^3$ and $v' \in \mathbb{R}^3 - \sigma^3$. Thus the union

$$N = v d(\tau^2) \cup v' d(\tau^2)$$

of the joins of $v$ and $v'$ with $d(\tau^2)$ forms a closed neighborhood of $\operatorname{Int} d(\tau^2)$ in $\mathbb{R}^3$; and if

$$f: d(\tau^2) \leftrightarrow d(\tau^2)$$

is a PLH that realizes the required mapping locally, then composing such maps and passing through the construction

$$f = f_2^{-1}f_1 : \mathbb{R}^3 \leftrightarrow \mathbb{R}^3,$$

we obtain $\sigma^3 \leftrightarrow \sigma^3$, and $D \leftrightarrow \sigma_0^2$, as desired.

All homeomorphisms used here differ from the identity only in arbitrarily small neighborhoods of $\operatorname{Bd} \sigma^3$. It follows that $f$ can be chosen so as to differ from the identity only in the given open neighborhood $W$ of $\sigma^3$.
