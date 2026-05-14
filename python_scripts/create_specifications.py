# creates a VNN-LIB 2.0 file (list of text lines) according to a fixed template:
# Arguments:
#   min_rPos: minimum relative position
#   max_rPos: maximum relative position
#   min_rVel: minimum relative velocity
#   max_rVel: maximum relative velocity
def vnnlib_template_2(min_rPos, max_rPos, min_rVel, max_rVel):

    lines = []

    # intro comment
    lines.append("; Safety verification for adaptive cruise control network:")
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
    lines.append(f"(assert (and (>= X[0,0] {min_rPos}) (<= X[0,0] {max_rPos})))")
    lines.append(f"(assert (and (>= X[0,1] {min_rVel}) (<= X[0,1] {max_rVel})))")
    lines.append("(assert (and (> X[0,0] 0.0) (>= (* X[0,0] 200.0) (* X[0,1] X[0,1]))))") #it is physically possible to break before hitting the other car
    lines.append("")

    # output constraints
    lines.append("; Output Constraints")
    lines.append("(assert (or (or (< Y[0,0] -100.001) (> Y[0,0] 100.001)) (and (< Y[0,0] 100.0) (or (!= Y[0,0] 0.0) (<= (* (+ X[0,0] (* X[0,1] 0.1)) 200.0) (* X[0,1] X[0,1]))) (or (>= Y[0,0] 100.0) (< Y[0,0] -100.0) (== Y[0,0] 0.0) (<= (* 200.0 (+ X[0,0] (* X[0,1] 0.1) (* Y[0,0] 0.005))) (* (+ X[0,1] (* Y[0,0] 0.1)) (+ X[0,1] (* Y[0,0] 0.1)))) (and (and (or (<= Y[0,0] 0.0) (and (<= (- X[0,1]) (* 0.1 Y[0,0])) (>= (- X[0,1]) 0.0))) (or (>= Y[0,0] 0.0) (and (>= (- X[0,1]) (* 0.1 Y[0,0])) (<= (- X[0,1]) 0.0)))) (and (or (<= Y[0,0] 0.0) (<= (* (* X[0,0] 2.0) Y[0,0]) (* X[0,1] X[0,1]))) (or (>= Y[0,0] 0.0) (>= (* (* X[0,0] 2.0) Y[0,0]) (* X[0,1] X[0,1])))))))))")

    return lines