let
  pkgs = import (builtins.fetchTarball "https://github.com/goromal/anixpkgs/archive/refs/tags/v5.19.2.tar.gz") {};
  py = pkgs.python310; # should match the version used with sage
in pkgs.mkShell {
  buildInputs = with pkgs; with py.pkgs; [
    sage
    py
    numpy
    scipy
    geometry
    pysignals
    pyceres_factors
    mesh-plotter
    find_rotational_conventions
  ];
}

