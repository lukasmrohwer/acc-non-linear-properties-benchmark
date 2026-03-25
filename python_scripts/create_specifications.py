"""
(
  (0<= rPos & rPos <= 100 & -200 <= rVel & rVel <= 200 & -A-0.001 <= rAccpost & rAccpost <= A+0.001)&
  (rPos > 0 & rPos >= rVel^2/(2*A))
) ->
(0 <= T & cpost = 0 & rAccpost >= A & rPospost = rPos & rVelpost = rVel |
rAccpost >= -B &
rAccpost  <  A &
rAccpost != 0 &

(
  (-rVel/rAccpost  > T | -rVel/rAccpost  <  0) &
  rPos + rVel * T + rAccpost * T^2 / 2 > (rVel + rAccpost * T)^2 / (2 * A) |
  rPos + rVel * T + rAccpost * T^2 / 2 > (rVel + rAccpost * T)^2 / (2 * A) &
  (rPos - rVel^2/rAccpost + rVel^2/(2*rAccpost)) > 0
) &
0 <= T & cpost = 0 & rPospost = rPos & rVelpost = rVel |
rPos + rVel * T > rVel^2 / (2 * A) &
0 <= T & cpost = 0 & rAccpost = 0 & rPospost = rPos & rVelpost = rVel)
"""

# creates a VNN-LIB 2.0 file (list of text lines) according to a fixed template:
# Arguments:
# - eps_in: allowed distance from original network's output
def vnnlib_template_2(eps_in):

    assert eps_in >= 0.0

    lines = []

    # intro comment
    lines.append("; Safety verifcation for adaptive cruise control network:")
    lines.append("; a VNN-COMP benchmark with non-linear properties.")
    lines.append("; Author: Lukas Rohwer")
    lines.append("")

    # tell the verifier to use VNN-LIB 2.0
    lines.append("(vnnlib-version <2.0>)")
    lines.append("")

    # neural network declaration
    lines.append("(declare-network f")
    lines.append("    (declare-input X real [1,2])") # [rPos, rVel]
    lines.append("    (declare-output Y real [1,1])") # [rAccpost]
    lines.append(")")
    lines.append("")

    # input constraints
    lines.append("; Input Constraints")
    lines.append("(assert (and (>= X[0,0] 0.0) (<= X[0,0] 100.0)))")
    lines.append("(assert (and (>= X[0,1] -200.0) (<= X[0,1] 200.0)))")
    lines.append("(assert (and (> X[0,0] 0.0) (>= (* X[0,0] 200.0) (* X[0,1] X[0,1]))))") #it is physically possible to break before hitting the other car
    lines.append("")

    # output constraints
    lines.append("; Output Constraints")
    lines.append("(assert (and (>= Y[0,0] -100.001) (<= Y[0,0] 100.001)))") 
    lines.append("(assert (or")

    lines.append("(>= Y[0,0] 100.0)") #case one: the car chose to fully break (safe)

    lines.append("(and (== Y[0,0] 0.0) (> (* (+ X[0,0] (* X[0,1] 0.1)) 200.0) (* X[0,1] X[0,1])))") #case two: the car chose to keep change of the distance between cars constant, and after 0.1 seconds it is still physically possible to break before hitting the other car

    lines.append("(and (< Y[0,0] 100.0) (>= Y[0,0] -100.0) (!= Y[0,0] 0.0) (> (* 200.0 (+ X[0,0] (* X[0,1] 0.1) (* Y[0,0] 0.005))) (* (+ X[0,1] (* Y[0,0] 0.1)) (+ X[0,1] (* Y[0,0] 0.1)))) (or (or (and (> Y[0,0] 0.0) (or (> (- X[0,1]) (* 0.1 Y[0,0])) (< (- X[0,1]) 0.0))) (and (< Y[0,0] 0.0) (or (< (- X[0,1]) (* 0.1 Y[0,0])) (> (- X[0,1]) 0.0)))) (or (and (> Y[0,0] 0.0) (> (* (* X[0,0] 2.0) Y[0,0]) (* X[0,1] X[0,1]))) (and (< Y[0,0] 0.0) (< (* (* X[0,0] 2.0) Y[0,0]) (* X[0,1] X[0,1]))))))") #case three

    lines.append("))")

    return lines