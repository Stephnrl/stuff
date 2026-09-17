abc --version
abc --help | grep -Ei "print|output-format|permission|mcp-config|settings|session-id|resume|model|max-(budget|turns)|append-system-prompt|add-dir"
ls -la ~/.abc                                   # symlinks? size? subdirectories?
du -sh ~/.abc && find ~/.abc -type l | head     # against the 32 MiB / 4096-file / no-links snapshot budget
