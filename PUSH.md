# Pushing this repo to github.com/Azaan-Raza

The repo is committed locally on branch `main`. From the unzipped folder:

Option A (GitHub CLI, logged in as Azaan-Raza):

    gh auth status                      # must show Azaan-Raza
    gh repo create Azaan-Raza/compbio-fair-winners --public --source=. --remote=origin --push

Option B (plain git): create an empty public repo named `compbio-fair-winners` at
https://github.com/new (no README, no license, no .gitignore), then:

    git remote add origin https://github.com/Azaan-Raza/compbio-fair-winners.git
    git push -u origin main

After the first push, GitHub Actions runs `scripts/validate.py` and checks that the
generated tables are current on every push and pull request.

To add your partner: Settings > Collaborators > Add people.

Delete this file after pushing, or keep it; it is not referenced anywhere.
