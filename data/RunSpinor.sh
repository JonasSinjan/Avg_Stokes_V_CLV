#module load openmpi_intel
#/data/gbso/home/riethmue/spinor_Michiel/spinor/src/inv                  # to run on a single core
module load openmpi_intel/2.1.2_2019.4
mpiexec -n 40 /data/gbso/home/riethmue/spinor_Michiel/spinor/src/inv    # to run in parallel on 40 cores
