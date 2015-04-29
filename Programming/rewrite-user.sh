# prepare the intro for printing, by making a custom copy for each user
# one page per user, with a different username filled in for each
# call pandoc on the resulting .md file
set -x
rm intro-ssh-raspi-multiple.md
for user in fluttershy blossomforth cloudchaser thunderlane stellar-eclipse soarin whiplash bluebell; do
    cat intro-ssh-raspi.md | sed "s/%user%/${user}/g" >> intro-ssh-raspi-multiple.md
done
pandoc -f markdown -t latex intro-ssh-raspi-multiple.md -o intro-ssh-raspi.pdf
