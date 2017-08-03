def sequence(tasks, names, results, missing, recursive, nest):
    for name in names:
        if name in results:
            continue
        if name not in tasks:
            missing.append(name)
        else:
            node = tasks[name]
            if name in nest:
                nest.append(name)
                recursive.append(nest[:])
                nest.pop()
            elif node['dep']:
                nest.append(name)
                sequence(tasks, node['dep'], results, missing, recursive, nest)
                nest.pop()
        results.append(name)

def sequencify(tasks, names):
    results = []
    missing = []
    recursive = []

    sequence(tasks, names, results, missing, recursive, [])

    if missing or recursive:
        results = []

    return {
        'sequence': results,
		'missingTasks': missing,
		'recursiveDependencies': recursive,
    }

__all__ = ('sequencify',)
