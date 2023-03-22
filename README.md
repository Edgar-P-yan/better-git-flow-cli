# Better Git Flow Helper CLI 👾

Automatically manages hotfix branches, increments tag versions, pushes to remote and etc.
The standard git-flow extension is not good enough 💩.

## How to use
Just copy the `git-flow` (https://github.com/Edgar-P-yan/better-git-flow-cli/blob/main/git-flow) file into the root folder of your repo, then make it executable:
```bash
chmod +x ./git-flow
```
And then use it like:
```
./git-flow fix start
```

## Available commands

- `./git-flow fix start [name]` - Creates new `hotfix/*` branch with next-patch-version name, or with the specified name.
- `./git-flow fix finish` - Merges current `hotfix/*` branch into `main` and `develop`, sets tags, and pushes to remote.
- `./git-flow help` - Show help message.

## Why not to use the standard git-flow extension?
The standard extension does not provide straight forward way of automatically incrementing tags,
does not automatically push changes to remote, so you have to type more commands. In contrast, this simple python
script automatically increments patch version from your latest tag, automatically merges fixes into `main` and `develop` branches,
and automatically pushes changes to remote.

In future, I might also add autmatic creation of Pull Requests via GitHub's CLI tool. But for now, this simple script will do the job. 
