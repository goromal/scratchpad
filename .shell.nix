let
  pkgs = import (builtins.fetchTarball "https://github.com/goromal/anixpkgs/archive/refs/heads/master.tar.gz") {};
  py = pkgs.python310; # should match the version used with sage
in pkgs.mkShell {
  buildInputs = with pkgs; with py.pkgs; [
    sage
    py
    numpy
    scipy
    geometry
    find_rotational_conventions
    (octaveFull.withPackages (ps: with ps; [
      control
    ]))
  ];
}

