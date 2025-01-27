let
  pkgs = import (builtins.fetchTarball "https://github.com/goromal/anixpkgs/archive/refs/heads/dev/nano-pgo.tar.gz") {};
  py = pkgs.python311; # should match the version used with sage TODO tightly couple these to anix version
in pkgs.mkShell {
  buildInputs = with pkgs; with py.pkgs; [
    sage
    py
    numpy
    scipy
    geometry
    pysignals
    pyceres
    pyceres_factors
    mesh-plotter
    find_rotational_conventions
    symforce
    graphviz
    (octaveFull.withPackages (ps: with ps; [
      control
    ]))
  ];
}

