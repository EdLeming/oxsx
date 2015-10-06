import os
import glob

try:
    from subprocess import check_output
    
except:
    print "import check_output failed: are you running python 2.7"
    

def get_root_flags():
    root_incs = check_output("root-config --cflags", shell=True)
    root_libs = check_output("root-config --libs", shell=True)
    return root_incs, root_libs


def get_arma_flags():
    try:
        armadillo_lib     = os.environ["ARMA_LIB"]
        armadillo_include = os.environ["ARMA_HEADER"]
        return armadillo_include, armadillo_lib

    except:
        print "Can't find armadillo - if non-standard install location please update pointer in env.sh"


def get_gsl_flags():
    try:
        gsl_lib     = os.environ["GSL_LIB"]
        gsl_include = os.environ["GSL_HEADER"]
        return gsl_include, gsl_lib

    except:
        print "Can't find armadillo - if non-standard install location please update pointer in env.sh"
        

def write_compile_script(env, dir):
    includes  = " ".join(["-I" + os.path.abspath(x) for x in env["CPPPATH"]])
    lib_paths = " ".join(["-L" + os.path.abspath(x) for x in env["LIBPATH"]])
    libs      = " ".join(["-l" + x for x in env["LIBS"]])

    with open(os.path.join(dir, "compile.sh"), "w") as f:
        f.write(
            ''' # This file is auto generated by scons
g++ -o $(basename "$1" .cpp) -O2 {0} {1} {2} $1
'''.format(includes, lib_paths, libs)
)
