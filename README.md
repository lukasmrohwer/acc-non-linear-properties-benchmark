# adaptive-cruise-control-benchmark

This benchmark was designed to test queries with non-linear properties. The network being verified is a Adaptive Cruise Control network provided by [Samuel Teuber](https://teuber.dev/), which receives an input tensor of shape (1,2) describing the relation position and relative velocity of a car to the car in front of it. The output is a tensor of shape (1,1) describing the level of acceleration the car should apply given in the input.

The specifications were translated into VNN-LIB 2.0 from the original specification also provided by [Samuel Teuber](https://teuber.dev/). These specifications guarantee the safety of such neural networks given a control period of 0.1 seconds and a maximum acceleration/deceleration of 100 m/s^2. The input constraints set the variable bounds and verify that the initial state of the vehicle is safe, by comparing the relative position and the minimum distance required to zero the relative velocity.

The output constraints verify the safety of the output of the network. If the network advises to apply maximum deceleration, it is safe. If the network chooses zero acceleration and the relative position is still greater than the minimum stopping distance required after 0.1 seconds, it is safe. If it chooses any other valid acceleration level and the post-state is verified using kinematic equations, it is safe. This benchmark is satisfied when relevant output results in an unsafe outcome, and should output an example.

Prebet, E., Teuber, S., & Platzer, A. (2026). Verification of Autonomous Neural Car Control with KeYmaera X. In F. Ishikawa & M. Leuschel (Eds.), Lecture notes in computer science (Vol. 15728, pp. 288–307). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-94533-5_17
