---
role: proof
locale: en
of_concept: determinant-of-incidence-matrix-product
source_book: gtm006
source_chapter: "3"
source_section: "5"
---

We compute $\det(AA')$. From the previous result, $AA' = nI + J$, so

$$\det(AA') = \begin{vmatrix}
n + 1 & 1 & \dots & 1 \\
1 & n + 1 & \dots & 1 \\
\vdots & \vdots & \ddots & \vdots \\
1 & 1 & \dots & n + 1
\end{vmatrix} = \det(nI + J).$$

Subtracting the first row from each of the other rows yields

$$\begin{vmatrix}
n + 1 & 1 & \dots & 1 \\
-n & n & 0 & \dots & 0 \\
-n & 0 & n & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
-n & 0 & 0 & \dots & n
\end{vmatrix}.$$

Now adding each of columns $2$ through $v$ to the first column gives

$$\det(AA') = \begin{vmatrix}
(n+1)^2 & 1 & \dots & 1 \\
0 & n & 0 & \dots & 0 \\
0 & 0 & n & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & n
\end{vmatrix} = (n+1)^2 \, n^{v-1}.$$

Since $v = n^2 + n + 1$, we have $v-1 = n^2 + n$, and therefore

$$\det(AA') = (n+1)^2 \, n^{n^2+n}.$$
