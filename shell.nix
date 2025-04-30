with import <nixpkgs> {};
pkgs.mkShell {
  packages = with pkgs; [
    imagemagick

    (python3.withPackages(p: with p; [
      pillow
      pywal
      tabulate
    ]))
  ];
}
