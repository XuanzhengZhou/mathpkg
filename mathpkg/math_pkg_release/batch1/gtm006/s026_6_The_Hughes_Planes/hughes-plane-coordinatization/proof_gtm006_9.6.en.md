---
role: proof
locale: en
of_concept: hughes-plane-coordinatization
source_book: gtm006
source_chapter: "9"
source_section: "6"
---

Let $(\infty)$ be $\langle (0,0,1) \rangle$, $(0)$ be $\langle (1,0,0) \rangle$, $(0,0)$ be $\langle (0,1,0) \rangle$, and $(1)$ be $\langle (1,0,-1) \rangle$. The line $l_{\infty}$ is, in the original representation, the line $y = 0$, and the new $x$-axis and $y$-axis are the original lines $z = 0$ and $x = 0$ respectively.

We label the points of the new $y$-axis by letting $\langle (0,1,v) \rangle$ be $(0,v)$ in our new system. Every line through $(1) = \langle (1,0,-1) \rangle$ is a line of the form $x + yt + z = 0$.

The point $(v,0)$ on the $x$-axis will be the point $\langle (u,1,0) \rangle$ which is collinear with $\langle (1,0,-1) \rangle$ and $\langle (0,1,v) \rangle$. But $\langle (1,0,-1) \rangle$ and $\langle (0,1,v) \rangle$ are on the line $L(-v)$, if $v \notin F$, from which it follows that $u + 1(-v) + 0 = 0$ or $u = v$. If $v \in F$, then it is obvious that $u = v$ and thus $(v,0)$ is the point $\langle (v,1,0) \rangle$.

Since the point $(m)$ is on $l_{\infty}$, it will be a point of the form $\langle (1,0,v) \rangle$. Furthermore $(m)$ is the point on $l_{\infty}$ which is collinear with $\langle (1,1,0) \rangle$ and $\langle (0,1,m) \rangle$. Let
$$xa + yb + zc + (xa' + yb' + zc')t = 0$$
be the line joining $\langle (1,1,0) \rangle$ and $\langle (0,1,m) \rangle$. Evaluating at these two points and solving yields $(m) = \langle (1,0,-m) \rangle$.

Finally, for an arbitrary point $(u,v)$, we verify by collinearity that its homogeneous coordinates are $\langle (u,1,v) \rangle$. Indeed, examining the line through $(1,0,-m)$ and $(u,1,v)$ and checking the intersection with the $y$-axis, in all cases we find that $(u,v)$ corresponds to $\langle (u,1,v) \rangle$.
