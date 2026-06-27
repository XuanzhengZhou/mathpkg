---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Dirichlet kernel $D_N(x) = \sin((N+\frac{1}{2})x)/\sin(\frac{1}{2}x)$ is the convolution kernel that produces the $N$-th symmetric partial sum of a Fourier series. It arises by summing the geometric series of exponentials: $\sum_{n=-N}^N e^{inx} = D_N(x)$. The kernel encapsulates the approximation properties of Fourier partial sums: convolving a function with $D_N$ yields its $N$-th Fourier partial sum $u_N = D_N * u$. While $D_N$ itself is not an approximate identity in the $L^1$ sense (its $L^1$ norm grows logarithmically), it is the central object in the study of pointwise convergence of Fourier series, including the Dirichlet-Jordan and Dini criteria.
