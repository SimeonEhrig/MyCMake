# About

This example shows, how to make a cmake project reusable for other project. Two different methods are supported: `add_subdirectory` and `find_package`.

# Usage

## add_subdirectory

```bash
cd add_subdirectory/build
cmake ../source -DCMAKE_INSTALL_PREFIX="../install"
cmake --build .
cmake --install .
../install/bin/testAddSubdirectory
```

## find_package

```bash
cd lib/build
cmake ../source -DCMAKE_INSTALL_PREFIX="../install"
cmake --build .
cmake --install .
cd ../install
install_path=$(pwd)
cd ../../find_package/build
cmake ../source -Dtestlib_DIR="${install_path}/share/testlib/cmake/" -DCMAKE_INSTALL_PREFIX="../install"
cmake --build .
cmake --install .
../install/bin/testFindPackage
```
