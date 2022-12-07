# GIT Tutorial

## make a commit

Add the new file or the file that has changes:

```bash
git add mydir/myfile.py
```

add commit message:

```bash
git commit -m "my first commit"
```

push

```bash
git push
```

## Tagging

Tags are specific stages in your code and refer typically to the version of your code/package.

### add a tag

```bash
git tag -a v0.1.0 -m "my first tag"
```

push to origin:

```bash
git push origin v0.1.0
```

### delete a tag

... locally:

```bash
git tag -d v0.1.0
```

... remotely:

```bash
git push --delete origin v0.1.0
```