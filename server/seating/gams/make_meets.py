"""
There are two things to solve:
1) there must be a way to select exactly one penalty level, 
by defining some function f such that we can find a 
penalty threshold T where 
f(T) >= 1, f(T-1) <1.

2) indirect meetup count is definitely wrong.
e.g 1,19 lists:
1,19,13 = 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
whereas only 5 and 15 are the players that both 1 and 19 meet directly. 
"""
import os
import subprocess
import importlib

def optimize_meets(seats, hanchan_count):
    table_count = len(seats[0])
    N = table_count * 4
    indirect_meetup_min = int(N ** 0.5)

    # Write seats data to GDX
    gdx_file = f"seats_{N}.gdx"
    with open(f"seats_{N}.gms", "w") as f:
        f.write(f"""
Set
    h hanchan / 1*{len(seats)} /
    t tables / 1*{table_count} /
    p players / 1*{N} /;

Parameter seats(h,t,p) /
""")
        for h, hanchan in enumerate(seats, 1):
            for t, table in enumerate(hanchan, 1):
                for i, p in enumerate(table, 1):
                    f.write(f"{h}.{t}.{p} 1\n")
        f.write("/;\n")
        f.write(f"execute_unload '{gdx_file}', seats;")

    # Run GAMS to create GDX
    result = subprocess.run(["gams", f"seats_{N}.gms"], capture_output=True, text=True)

    if not os.path.exists(gdx_file):
        print(f"Error: GDX file {gdx_file} was not created.")
        print("GAMS output:", result.stdout)
        print("GAMS error:", result.stderr)
        return None

    # Create optimize_{N}.gms file
    gams_file = f"optimize_{N}.gms"
    with open(gams_file, "w") as f:
        f.write(f"""
$set gdxincurdir 1
$gdxin {gdx_file}
$if not exist {gdx_file} $abort 'GDX file does not exist'

$offsymxref offsymlist
Option limrow = 0, limcol = 0;
Option solprint = off;

Sets
    h hanchan / 1*{len(seats)} /
    t tables / 1*{table_count} /
    p players / 1*{N} /
    ;

Alias (p, p1, p2, p3);
Alias (h, h1, h2);
Alias (t, t1, t2);

Parameters
    seats(h,t,p) original seating arrangement
    
$loaddc seats
$gdxin

Scalar hanchan_count / {hanchan_count} /;
Scalar indirect_meetup_min / {indirect_meetup_min} /;

Binary Variables 
    x(h) 'binary variable for selecting hanchan'
    meets(p1,p2,h) 'binary variable indicating if p1 and p2 meet in hanchan h'
    meets_any(p1,p2) 'binary variable indicating if p1 and p2 meet in any selected hanchan'
    indirect_meet(p1,p2,p3) 'binary variable indicating if p1 and p2 meet indirectly through p3'
    ;

Variables
    z 'objective function value'
    ;

Positive Variables
    indirect_meetups(p1,p2) 'indirect meetups for each pair of players'
    penalty(p1,p2) 'penalty for indirect meetings being less than minimum'
    penalty2(p1,p2) 'penalty for indirect meetings being 2 or fewer'
    penalty1(p1,p2) 'penalty for indirect meetings being 1 or fewer'
    penalty0(p1,p2) 'penalty for indirect meetings being zero'
    ;

Equations
    obj 'define objective function'
    select_hanchan 'select exactly hanchan_count hanchan'
    define_meets(p1,p2,h) 'define the meets variable'
    define_meets_any(p1,p2) 'define the meets_any variable'
    define_meets_any2(p1,p2) 'symmetry'
    define_indirect_meet1(p1,p2,p3) 'define the indirect_meet variable (condition 1)'
    define_indirect_meet2(p1,p2,p3) 'define the indirect_meet variable (condition 2)'
    define_indirect_meet3(p1,p2,p3) 'define the indirect_meet variable (condition 3)'
    count_indirect_meetups(p1,p2) 'count indirect meetups for each pair of players'
    calculate_penalty(p1,p2) 'calculate main penalty'
    calculate_penalty2(p1,p2) 'calculate penalty2'
    calculate_penalty1(p1,p2) 'calculate penalty1'
    calculate_penalty0(p1,p2) 'calculate penalty0'
    limit_penalty(p1,p2) 'ensure penalty is non-negative'
    limit_penalty2(p1,p2) 'ensure penalty2 is non-negative'
    limit_penalty1(p1,p2) 'ensure penalty1 is non-negative'
    limit_penalty0(p1,p2) 'ensure penalty0 is non-negative'
    ;

obj.. z =e= sum((p1,p2)$(ord(p1) < ord(p2)), penalty(p1,p2) + penalty2(p1,p2) + penalty1(p1,p2) + penalty0(p1,p2));

select_hanchan.. sum(h, x(h)) =e= hanchan_count;

define_meets(p1,p2,h)$(ord(p1) < ord(p2)).. 
    meets(p1,p2,h) =e= sum(t, seats(h,t,p1) * seats(h,t,p2)) * x(h);

define_meets_any(p1,p2)$(ord(p1) < ord(p2))..
    meets_any(p1,p2) =e= sum(h, meets(p1,p2,h));

define_meets_any2(p1,p2)$(ord(p1) > ord(p2))..
    meets_any(p1,p2) =l= 0;

define_indirect_meet1(p1,p2,p3)$(ord(p1) < ord(p2) and ord(p3) <> ord(p1) and ord(p3) <> ord(p2))..
    indirect_meet(p1,p2,p3) =l= meets_any(p1,p3);

define_indirect_meet2(p1,p2,p3)$(ord(p1) < ord(p2) and ord(p3) <> ord(p1) and ord(p3) <> ord(p2))..
    indirect_meet(p1,p2,p3) =l= meets_any(p2,p3);

define_indirect_meet3(p1,p2,p3)$(ord(p1) < ord(p2))..
    indirect_meet(p1,p2,p3) =g= meets_any(p1,p3) + meets_any(p2,p3) - 1;

count_indirect_meetups(p1,p2)$(ord(p1) < ord(p2)).. 
    indirect_meetups(p1,p2) =e= sum(p3$(ord(p3) <> ord(p1) and ord(p3) <> ord(p2)), indirect_meet(p1,p2,p3));

calculate_penalty(p1,p2)$(ord(p1) < ord(p2))..
    penalty(p1,p2) =g= (indirect_meetup_min - indirect_meetups(p1,p2) - 1000 * meets_any(p1,p2)) * 1000;

calculate_penalty2(p1,p2)$(ord(p1) < ord(p2))..
    penalty(p1,p2) =g= (3 - indirect_meetups(p1,p2) - 10 * meets_any(p1,p2)) * 3000;

calculate_penalty1(p1,p2)$(ord(p1) < ord(p2))..
    penalty(p1,p2) =g= (2 - indirect_meetups(p1,p2) - 10 * meets_any(p1,p2)) * 1e4;

calculate_penalty0(p1,p2)$(ord(p1) < ord(p2))..
    penalty(p1,p2) =g= (1 - indirect_meetups(p1,p2) - 10 * meets_any(p1,p2)) * 1e7;

limit_penalty(p1,p2)$(ord(p1) < ord(p2))..
    penalty(p1,p2) =g= 0;

limit_penalty2(p1,p2)$(ord(p1) < ord(p2))..
    penalty2(p1,p2) =g= 0;

limit_penalty1(p1,p2)$(ord(p1) < ord(p2))..
    penalty1(p1,p2) =g= 0;

limit_penalty0(p1,p2)$(ord(p1) < ord(p2))..
    penalty0(p1,p2) =g= 0;

Model seating /all/;

Option reslim = 600;
Option threads = 1;
Option solvelink = 5;

Option sysout = on;
seating.optfile = 1;

Solve seating using mip minimizing z;

file results / 'results_{N}.txt' /;

put results;
if(seating.modelstat = 4,
    put "Model status: Infeasible" /;
    put "IIS information in the LST file" /;
else
    put 'Selected hanchan:'/;
    loop(h$(x.l(h) > 0.5),
        put h.tl /;
    );
);
put 'done' /;
putclose;
""")

    # Run GAMS optimization
    result = subprocess.run(["gams", gams_file], capture_output=False, text=True)

    # Load and return results
    if not os.path.exists(f"results_{N}.txt"):
        print(f"Error: Results file results_{N}.txt was not created.")
        return None

    with open(f"results_{N}.txt", "r") as f:
        content = f.read()

    if "Model status: Infeasible" in content:
        print("The problem is infeasible. Check the LST file for IIS information.")
        return None
    
    # Read results
    selected_hanchan = []
    for line in content.split('\n'):
        if line.startswith("Selected hanchan:"):
            continue
        elif line.strip() == "done":
            break
        else:
            selected_hanchan.append(int(line))

    # Create new_seats based on selected hanchan
    new_seats = [seats[h-1] for h in selected_hanchan]

    # Write new seats to Python file
    with open(f"meets/{N}x{hanchan_count}.py", "w") as f:
        out = f"{new_seats}\n".replace("],", "],\n")
        f.write(f"seats = {out}\n")

    # Clean up temporary files
    for file in [gams_file, f"seats_{N}.gms", f"seats_{N}.gdx", f"seats_{N}.lst",
                f"optimize_{N}.lst",
                f"results_{N}.txt"]: 
        if os.path.exists(file):
            os.remove(file)

    return new_seats

if __name__ == "__main__":
    from stats import make_stats
    tst = importlib.import_module("sgp.60").seats
    seats = optimize_meets(tst, 6)
    out = make_stats(seats)
    out = out[out.find("Indirect Meetup frequencies:"):]
    print(f"optimised: {out}\n\n")
    out1 = make_stats(tst[0:6])
    out1 = out1[out1.find("Indirect Meetup frequencies:"):]
    print(f"baseline: {out1}")
