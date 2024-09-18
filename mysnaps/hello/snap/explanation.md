# Breakdown of snapcraft.yml

- name: The name of the snap
- base: A foundation snap that provides a run-time with a minimal set of librarires that are common to most applicants
- version: The current version of the snap.
- summary: A short, one-line summary or tag-line for your snap
- description: A longer description of the snap. It can span over a multiple lines if prefixed with the '|' character
- grade: can be used by the publisher to indicate the quality confidence in the build.
- confinement: A snap's level is the degree of isolation it has from your system and there are three levels: strict, classic and devmode. strict snaps run in complete isolation, classic snaps have open access to system resources and devmode snaps run as strict but with open access to the system. 
