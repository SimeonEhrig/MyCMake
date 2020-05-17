import hpccm
from hpccm.primitives import baseimage, shell
from hpccm.building_blocks.packages import packages
from hpccm.building_blocks.cmake import cmake
from hpccm.building_blocks.llvm import llvm

def main():
    ############################################################################
    # setup basics
    ############################################################################
    hpccm.config.set_container_format('singularity')
    hpccm.config.set_singularity_version('3.3')

    stage0 = hpccm.Stage()
    stage0 += baseimage(image='ubuntu:bionic')

    stage0 += packages(ospackages=['git', 'g++', 'wget', 'pkg-config', 'less',
                                   'uuid-dev', 'gdb', 'locales', 'gpg-agent',
                                   'gnupg2', 'locales-all', 'unzip'])
    # set language to en_US.UTF-8 to avoid some problems with the cling output system
    stage0 += shell(commands=['locale-gen en_US.UTF-8',
                              'update-locale LANG=en_US.UTF-8'])

    ############################################################################
    # install clang/llvm
    ############################################################################
    stage0 += llvm(version='9', extra_repository=True)

    ############################################################################
    # install ninja build system
    ############################################################################
    stage0 += shell(commands=['cd /opt',
                              'wget --no-check-certificate ' +
                              'https://github.com/ninja-build/ninja/releases/download/v1.9.0/ninja-linux.zip',
                              'unzip ninja-linux.zip',
                              'mv ninja /usr/local/bin/',
                              'rm ninja-linux.zip',
                              'cd -'])

    ############################################################################
    # install cmake
    ############################################################################
    stage0 += cmake(eula=True, version='3.16.1')

    ############################################################################
    # write recipe.def
    ############################################################################
    with open('recipe.def', 'w') as filehandle:
        filehandle.write(stage0.__str__())

if __name__ == '__main__':
    main()
