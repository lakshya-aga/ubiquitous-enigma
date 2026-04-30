
sed stands for stream editor. Convenient way to edit files like txt etc. based on pattern matching
example usage 
```bash
sed -e "s,old,new,g" /etc/yum.repos.d/epel.repo
```

This command edits file to `s`ubstitute `old` for `new` `g`lobally across file

without `g` only edits the first occurence of each line not first occurence of file

---

Topics: [[Linux]]
Reference:
Type: #atom