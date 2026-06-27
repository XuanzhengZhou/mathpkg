---
role: proof
locale: en
of_concept: transformation-property-of-discriminant
source_book: gtm041
source_chapter: "4"
source_section: "4.7"
---
Recall that $\Delta = g_2^3 - 27g_3^2$, where $g_2$ and $g_3$ are Eisenstein series of weights $4$ and $6$ respectively.
For any $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma$, the Eisenstein series satisfy
$$g_2\left(\frac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^4 g_2(\tau), \qquad g_3\left(\frac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^6 g_3(\tau).$$
Hence
$$\Delta\left(\frac{a\tau+b}{c\tau+d}\right) = \left[(c\tau+d)^4 g_2(\tau)\right]^3 - 27\left[(c\tau+d)^6 g_3(\tau)\right]^2 = (c\tau+d)^{12}\left(g_2(\tau)^3 - 27g_3(\tau)^2\right) = (c\tau+d)^{12}\Delta(\tau).$$
The special cases follow immediately:
$$\Delta(\tau+1) = \Delta(\tau) \quad (\text{take } a=b=d=1, c=0),$$
$$\Delta\left(-\frac{1}{\tau}\right) = \tau^{12}\Delta(\tau) \quad (\text{take } a=d=0, b=-1, c=1).$$
